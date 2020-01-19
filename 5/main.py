"""1: Add
2: Multiply
3: Input
4: Output
99: End"""
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

def calc(stringen, inpp):
    l = stringen.split(",")
    inp = inpp
    output = 42
    for c, i in enumerate(l):
        l[c] = int(l[c])
    done = False
    i = 0
    while not done:
        seq = opcode(l[i])
        print(  [str("{} : {}".format(r,k)) for r, k in enumerate(l)] )
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
            p1 = l[i+1]
            print("P1: ", p1)
            l[p1] = inp
            i += 2

        elif seq[-2:] == "04":
            p1 = parparse(l,seq[2] , 1, i)
            print("Output: ", i, p1)
            output = p1
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
            print("equals seq: ", seq)
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            print("Equals: ", p1, p2 , p3)
            if p1 == p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4

    return output

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.readlines()
        print(calc(d[0], 5))
