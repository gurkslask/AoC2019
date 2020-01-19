from collections import defaultdict

def minFunc(dic):
    p = 9999999999
    res = None

    for i in dic:
        if dic[i]["dist"] < p and not dic[i]["visited"]:
            res = i
    return res
def checkFunc(dic):
    for i in dic:
        if not dic[i]["visited"]:
            return True
    return False


def calc(l):
    d=defaultdict(list)
    #print(l)
    for entry in l:
        entry = entry.split(")")
        d[entry[1]].append(entry[0])
    orbit_counter = 0
    for orbit in d:
        orbit_counter += 1
        #print("Orbit: {}, counter: {} \n".format(orbit, orbit_counter))
        while d[orbit][0] != "COM":
            orbit_counter += 1
            orbit = d[orbit][0]
    print(orbit_counter)
    return orbit_counter

def calcAdv(l):
    d=defaultdict(list)
    d2=defaultdict(list)
    fd=defaultdict(list)
    dd = defaultdict(dict)
    #print(l)
    for entry in l:
        entry = entry.split(")")
        # Key is node, values are the nodes orbiting it, neighbors
        d[entry[0]].append(entry[1])
        # Key is node, value are the next node
        d2[entry[1]].append(entry[0])

        if entry[1] == "YOU":
            dd[entry[1]] = {"dist": 0, "prev": [], "visited": False}
        else:
            dd[entry[1]] = {"dist": 9999999999, "prev": [], "visited": False}

        if entry[0] == "YOU":
            dd[entry[0]] = {"dist": 0, "prev": [], "visited": False}
        else:
            dd[entry[0]] = {"dist": 9999999999, "prev": [], "visited": False}
    for i in d:
        d2[i] = d2[i] + d[i]

    length = 0
    #print("WHILE!!!!")
    #print(len(dd))
    while checkFunc(dd):
        # print("WHILE!!!!")
        #print("before", len(dd))
        m = minFunc(dd)
        #print("m", m)
        u = dd[m]
        dd[m]["visited"] = True
        #print("u", u)
        neighbors = d2[m]
        length = dd[m]["dist"] +1
        #print("neighbors", neighbors)
        for i in neighbors:
            #print("i in loooooooop: ", i)
            dd[i]["prev"] = m
            if dd[i]["dist"] < length or dd[i]["dist"] == 9999999999:
                dd[i]["dist"]=length
        #print("before", len(dd))
        #print("dd", dd)


    # print("RESULT_____!!!!: ", dd["SAN"]["dist"] - 2)
    # print(dd)
    return dd["SAN"]["dist"] - 2

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.readlines()
        for i, j in enumerate(d):
            d[i] = j.replace("\n","")
        print(calc(d))
        print(calcAdv(d))


