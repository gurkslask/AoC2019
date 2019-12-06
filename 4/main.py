def calc(number):
    same = False
    rise = True
    number = str(number)
    for pos, tal in enumerate(  number  ):
        tal = int(tal)
        if pos < 5:
            if tal == int( number[pos+1] ):
                same = True

            if tal > int(  number[pos+1] ):
                rise = False

    return same and rise


def calcAdv(number):
    same = False
    rise = True
    number = str(number)
    removed = True
    for pos, tal in enumerate(number):
        tal = int(tal)
        try:
            if tal > int(  number[pos+1] ):
                rise = False
        except IndexError:
            pass

    while removed:
        removed = False
        for pos, tal in enumerate(number):
            tal = int(tal)
            try:
                if tal == int( number[pos+1] ):
                    c = 0
                    for i in number[pos:]:
                        if int(i) == tal:
                            c += 1
                        else:
                            break
                    if c == 2:
                        same = True
                    if c > 2:
                        number = number.replace(number[pos:pos+c], '')
                        removed = True
            except IndexError:
                pass

    return same and rise

if __name__ == "__main__":
    c = 0
    c2 = 0
    for i in range(240920, 789857):
        if calc(i):
            c += 1
        if calcAdv(i):
            c2 += 1
    print(c)
    print("Advanced: ", c2)


