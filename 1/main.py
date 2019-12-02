def calcMass(mass):
    return int(mass/3)-2

def calcAdv(mass):
    summ = 0
    res = calcMass(int(mass))
    summ += res 
    while res > 0 :
        res = calcMass(int(res))
        if res > 0:
            summ += res 
    return summ

if __name__ == '__main__':
    summ = 0
    with open('input.txt', 'r') as f:
        d = f.readlines()
    for i in d:
        res =calcMass(int(i))
        summ += res 

    print("Answer basic: ", summ)
    summ = 0 

    for i in d:
        res =calcAdv(int(i))
        summ += res 
    print("Answer 2: ", summ)
