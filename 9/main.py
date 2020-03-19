"""1: Add
2: Multiply
3: Input
4: Output
99: End"""
import itertools
def opcode(i):
    # print(i)
    s = str("{0:0>5.0f}".format(i))
    return s
def parparse(l, b, num, i, relative_base):
    if b == "1":
        #Immediate mode
        return l[i+num]
    if b == "0":
        #Position mode
        return l[l[i+num]]
    if b == "2":
        # Relative mode
        print("This is relative_base: {}, and the other: {}".format(relative_base, b))
        return l[l[i+num] + relative_base]

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
    for i in range(10000):
        l.append(0)
    done = False
    i = 0
    relative_base = 0
    input1_done = False
    # print(input1, input2)
    while not done:
        seq = opcode(l[i])
        # print(  [str("{} : {}".format(r,k)) for r, k in enumerate(l)] )
        if seq[-2:] == "01":
            p1 = parparse(l, seq[2], 1, i, relative_base)
            p2 = parparse(l, seq[1], 2, i, relative_base)
            p3 = l[i+3]
            l[p3] = p1 + p2
            i += 4

        elif seq[-2:] == "99":
            done = True

        elif seq[-2:] == "02":
            p1 = parparse(l, seq[2], 1, i, relative_base)
            p2 = parparse(l, seq[1], 2, i, relative_base)
            p3 = l[i+3]
            l[p3] = p1 * p2
            i += 4

        elif seq[-2:] == "03":
            # Input
            # Receive new input to generator
            #input2 = yield
            #yield -1
            p1 = l[i+1]
            # print("P1: ", p1)
            # print(input1_done)
            """if input1_done:
                l[p1] = input2
            else:
                l[p1] = input1"""
            l[p1] = input1
            input1_done = True
            i += 2

        elif seq[-2:] == "04":
            print(seq[3])
            p1 = parparse(l,seq[2] , 1, i, relative_base)
            print("Output: ",  p1)
            output = p1
            #ninput2 = yield
            #yield output
            i += 2

        elif seq[-1] == "5":
            #Jump if true
            p1 = parparse(l, seq[2], 1, i, relative_base)
            p2 = parparse(l, seq[1], 2, i, relative_base)
            if p1 != 0:
                i = p2
            else:
                i += 3

        elif seq[-1] == "6":
            #Jump if false
            p1 = parparse(l, seq[2], 1, i, relative_base)
            p2 = parparse(l, seq[1], 2, i, relative_base)
            if p1 == 0:
                i = p2
            else:
                i += 3

        elif seq[-1] == "7":
            #Less than
            p1 = parparse(l, seq[2], 1, i, relative_base)
            p2 = parparse(l, seq[1], 2, i, relative_base)
            p3 = l[i+3]
            if p1 < p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4

        elif seq[-1] == "8":
            #equals
            # print("equals seq: ", seq)
            p1 = parparse(l, seq[2], 1, i, relative_base)
            p2 = parparse(l, seq[1], 2, i, relative_base)
            p3 = l[i+3]
            # print("Equals: ", p1, p2 , p3)
            if p1 == p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4
        elif seq[-1] == "9":
            # change relative_base
            p1 = parparse(l, seq[2], 1, i, relative_base)
            relative_base += p1
            i += 2

    # print(output)
    # print(type(output))

    return int(output)


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.read()
        # print(runner(d))
        # print(runner2(d))
        res = calc(d, 1, 0)
        print("Result: ", res)

