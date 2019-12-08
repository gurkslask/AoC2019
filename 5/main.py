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

def calc(stringen):
    l = stringen.split(",")
    inp = 1
    for c, i in enumerate(l):
        l[c] = int(l[c])
    done = False
    i = 0
    while not done:
        seq = opcode(l[i])
        print(seq)
        if seq[-2:] == "01":
            print("plus: {}".format(seq))
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            # p3 = parparse(l, seq[0], 3, i)
            p3 = l[i+3]
            print(i)
            print(p1, p2, p3)

            l[p3] = p1 + p2
            i += 4
        elif seq[-2:] == "99":
            done = True
        elif seq[-2:] == "02":
            print("times: {}".format(seq))
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = parparse(l, seq[0], 3, i)
            l[p3] = p1 * p2
            i += 4
        elif seq[-2:] == "03":
            print("input: {}".format(seq))
            # Input
            p1 = parparse(l, seq[2], 1, i)
            l[p1] = inp
            i += 2
        elif seq[-2:] == "04":
            print("Output: {}".format(seq))
            # Input
            p1 = parparse(l, seq[2], 1, i)
            print(l[p1])
            i += 2
    print(l)
    return l[0]

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.readlines()
        print(calc(d[0]))
        # print(calcAdv(d[0]))


