"""1: Add, 2: Multiply, 99: End"""
def calc(stringen, prod):
    l = stringen.split(",")
    if prod:
        l[1] = 12
        l[2] = 2
    for c, i in enumerate(l):
        l[c] = int(l[c])
    # print("splittad: ", l)
    done = False
    i = 0
    while not done:
        # print("Start Loop: ", i)
        if l[i] == 1:
            # print("{} = {} + {}".format(l[l[c+3]],l[l[c+1]], l[l[c+2]] ))
            l[l[i+3]] = l[l[i+1]] +l[l[i+2]] 
        elif l[i] == 99:
            done = True
        elif l[i] == 2:
            # print("{} = {} + {}".format(l[l[c+3]],l[l[c+1]], l[l[c+2]] ))
            l[l[i+3]] = l[l[i+1]] *l[l[i+2]] 
        # print("Efter loop: ", l)
        i += 4
    print(l)
    return l[0]

def calcAdv(stringen ):
    l = stringen.split(",")
    for c, i in enumerate(l):
        l[c] = int(l[c])
    # print("splittad: ", l)
    done = False
    i = 0
    while not done:
        ll = l
        # print("Start Loop: ", i)
        if l[i] == 1:
            # print("{} = {} + {}".format(l[l[c+3]],l[l[c+1]], l[l[c+2]] ))
            l[l[i+3]] = l[l[i+1]] +l[l[i+2]] 
        elif l[i] == 99:
            done = True
        elif l[i] == 2:
            # print("{} = {} + {}".format(l[l[c+3]],l[l[c+1]], l[l[c+2]] ))
            l[l[i+3]] = l[l[i+1]] *l[l[i+2]] 
        # print("Efter loop: ", l)
        i += 4
    print(l)
    return l[0]

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.readlines()
        print(calc(d[0], True))


