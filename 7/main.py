"""1: Add
2: Multiply
3: Input
4: Output
99: End"""
import itertools
def opcode(i):
    s = str("{0:0>5.0f}".format(i))
    return s
def parparse(l, b, num, i):
    if b == "1":
        #Immediate mode
        return l[i+num]
    if b == "0":
        #Position mode
        return l[l[i+num]]

def geni():
    for i in range(99999):
        toolarge = False
        s = opcode(i)
        for ss in s:
            if int(ss) >= 5:
                toolarge = True
        if not toolarge:
            yield int(s)
    


def calc(stringen, input1, input2):
    l = stringen.split(",")
    output = 42
    for c, i in enumerate(l):
        l[c] = int(l[c])
    done = False
    i = 0
    input1_done = False
    # print(input1, input2)
    while not done:
        seq = opcode(l[i])
        # print(  [str("{} : {}".format(r,k)) for r, k in enumerate(l)] )
        if seq[-2:] == "01":
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            l[p3] = p1 + p2
            i += 4

        elif seq[-2:] == "99":
            done = True

        elif seq[-2:] == "02":
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            l[p3] = p1 * p2
            i += 4

        elif seq[-2:] == "03":
            # Input
            # Receive new input to generator
            input2 = yield
            yield -1
            p1 = l[i+1]
            # print("P1: ", p1)
            # print(input1_done)
            if input1_done:
                l[p1] = input2
            else:
                l[p1] = input1
            input1_done = True
            i += 2

        elif seq[-2:] == "04":
            p1 = parparse(l,seq[2] , 1, i)
            # print("Output: ",  p1)
            output = p1
            input2 = yield
            yield output
            i += 2

        elif seq[-1] == "5":
            #Jump if true
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            if p1 != 0:
                i = p2
            else:
                i += 3

        elif seq[-1] == "6":
            #Jump if false
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            if p1 == 0:
                i = p2
            else:
                i += 3

        elif seq[-1] == "7":
            #Less than
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            if p1 < p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4

        elif seq[-1] == "8":
            #equals
            # print("equals seq: ", seq)
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            # print("Equals: ", p1, p2 , p3)
            if p1 == p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4

    # print(output)
    # print(type(output))

    return int(output)

def runner(stringen):
    res = 0

    for i in itertools.permutations(range(5)):
        out = 0
        s = "".join(map(str,i))
        funcs = [calc(stringen, int(s[i]), out) for i in range(5)]
        for i in range(5):
            received = -1
            while received == -1:
                next(funcs[i])
                received = funcs[i].send(out)
            out = received
            # # print(out)
            # input("dsnajkdsa")

        if res < out:
            res = out
    return res

def runner2(stringen):
    res = 0
    for i in itertools.permutations(range(5, 10)):
        out = 0
        iterdone = False
        s = "".join(map(str,i))
        funcs = [calc(stringen, int(s[i]), out) for i in range(5)]
        while not iterdone:
            for i in range(5):
                received = -1
                while not iterdone and received == -1:
                    try:
                        next(funcs[i])
                    except StopIteration: iterdone = True
                    try:
                        received = funcs[i].send(out) 
                    except StopIteration: iterdone = True
                    
                if received != -1:
                    out = received

        if res < out:
            res = out
    return res


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.read()
        print(runner(d))
        print(runner2(d))
