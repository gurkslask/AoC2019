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
        # print(seq)
        if seq[-2:] == "01":
            # # print("plus: {}".format(seq))
            # print(l)
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            # p3 = l[i+3]
            # print(p1, p2 ,p3)
            # print(i)
            # print("Plus: ", p1, p2, p3)

            l[p3] = p1 + p2
            i += 4
        elif seq[-2:] == "99":
            done = True
        elif seq[-2:] == "02":
            # print("times: {}".format(seq))
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = l[i+3]
            # print("Times: ", p1, p2, p3)
            l[p3] = p1 * p2
            i += 4
        elif seq[-2:] == "03":
            # print("input: {}".format(seq))
            # print("lista vid input: ", l)
            # Input
            p1 = l[i+1]
            # print("P1: ", p1)
            l[p1] = inp
            # l[255] = inp
            
            i += 2
        elif seq[-2:] == "04":
            # print("Output: {}".format(seq))
            # Input
            p1 = l[i+1]
            print("Output: ", l[p1])
            output = l[p1]
            i += 2
        elif seq[-1] == "5":
            #Jump if true
            # print("Jump true: ", p1, p2 )
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            # print("Jump true: ", p1, p2 )
            if p1 != 0:
                i = p2
            else:
                i += 4

        elif seq[-1] == "6":
            #Jump if false
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            # print("Jump false: ", p1, p2 )
            if p1 == 0:
                i = p2
            else:
                i += 4

        elif seq[-1] == "7":
            #Less than
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = parparse(l, seq[0], 3, i)
            # p3 = l[i+3]

            # print("Less than: ", p1, p2 , p3)
            if p1 > p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4
        elif seq[-1] == "8":
            #equals
            p1 = parparse(l, seq[2], 1, i)
            p2 = parparse(l, seq[1], 2, i)
            p3 = parparse(l, seq[0], 3, i)
            # p3 = l[i+3]
            # print("Equals: ", p1, p2 , p3)
            if p1 == p2:
                l[p3] = 1
            else:
                l[p3] = 0
            i += 4

    return l[0]

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.readlines()
        print(calc(d[0], 5))
        # print(calcAdv(d[0]))


