def taxi(p1, p2, q1, q2):
    res =abs((p1-q1)) + abs((p2-q2))
    return res

def calc(string1, string2):
    mapp1 = []
    mapp2 = []
    mapp = []
    curr_pos = (0, 0)
    moven = 0


    def moveright(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0] + 1, cur_pos[1]) 
            m.append(cur_pos)
        return m, cur_pos
    
    def moveleft(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0] - 1, cur_pos[1]) 
            m.append(cur_pos)
        return m, cur_pos
    def moveup(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0], cur_pos[1] + 1) 
            m.append(cur_pos)
        return m, cur_pos
    def movedown(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0], cur_pos[1] - 1) 
            m.append(cur_pos)
        return m, cur_pos
    d = {
            "R": moveright,
            "U": moveup,
            "L": moveleft,
            "D": movedown,
        }
    string1 = string1.split(",")
    string2 = string2.split(",")
    # print(string1, string2)
    for i in string1:
        moven = int(i[1:])
        mapp, curr_pos = d[i[0]](mapp, curr_pos, moven)
        
    mapp1 = mapp
    mapp = []
    curr_pos = (0, 0)
    for i in string2:
        moven = int(i[1:])
        mapp, curr_pos = d[i[0]](mapp, curr_pos, moven)
    mapp2 = mapp
    # print("här kommer mapparna", mapp1,"2an\n",  mapp2)
    overlap = {}
    for i in mapp1:
        if i in mapp2:
            overlap[taxi(i[0],i[1],0,0)] = i
            print(overlap)

    return min(overlap)


def calcAdv(string1, string2):
    mapp1 = []
    mapp2 = []
    mapp = []
    curr_pos = (0, 0)
    moven = 0
    steps = 0


    def moveright(m, org_pos, move, steps):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0] + 1, cur_pos[1]) 
            m.append(cur_pos)
        return m, cur_pos
    
    def moveleft(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0] - 1, cur_pos[1]) 
            m.append(cur_pos)
        return m, cur_pos
    def moveup(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0], cur_pos[1] + 1) 
            m.append(cur_pos)
        return m, cur_pos
    def movedown(m, org_pos, move):
        cur_pos = org_pos
        for i in range( move ):
            cur_pos = (cur_pos[0], cur_pos[1] - 1) 
            m.append(cur_pos)
        return m, cur_pos
    d = {
            "R": moveright,
            "U": moveup,
            "L": moveleft,
            "D": movedown,
        }
    string1 = string1.split(",")
    string2 = string2.split(",")
    # print(string1, string2)
    for i in string1:
        moven = int(i[1:])
        mapp, curr_pos = d[i[0]](mapp, curr_pos, moven)
        
    mapp1 = mapp
    mapp = []
    curr_pos = (0, 0)
    for i in string2:
        moven = int(i[1:])
        mapp, curr_pos = d[i[0]](mapp, curr_pos, moven)
    mapp2 = mapp
    # print("här kommer mapparna", mapp1,"2an\n",  mapp2)
    overlap = {}
    for i in mapp1:
        if i in mapp2:
            overlap[taxi(i[0],i[1],0,0)] = i
            print(overlap)

    return min(overlap)
if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.readlines()
        print(calc(d[0], d[1]))


