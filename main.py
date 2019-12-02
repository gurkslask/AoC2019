def calcMass(mass):
    return int(mass/3)-2

if __name__ == '__main__':
    summ = 0
    with open('input.txt', 'r') as f:
        d = f.readlines()
    for i in d:
        res =calcMass(int(i))
        print(res)
        summ += res 

    print(summ)
