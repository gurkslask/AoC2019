# 0 black
# 1 White
# 2 Transparent
def countocc(lista, num):
        inc = 0
        for row in lista:
            for col in row:
                if col == num:
                    inc+=1
        return inc

def calc(inp, inpx, inpy, result):
    # Layer, row
    # Generate image
    layers =  int(len(inp)/(inpx * inpy) )
    # print(layers)
    # print(len(inp))
    ll = [[[inp[col + (row * inpx) + (layer * ( inpx + inpy  ))] for col in range(inpx)] for row in range(inpy)] for layer in range(layers)]

    # Setup be4 comparison
    smallestocc = 999999
    smallestlayer = []

    # Compare occurences
    for layer in ll:
        occ = countocc(layer, "0")
        if occ < smallestocc:
            smallestlayer = layer
            smallestocc = occ

    if result:
        return countocc(smallestlayer, "1") * countocc(smallestlayer, "2")
    else:
        return ll

def genimg(lista, inpx, inpy):
    print("lista: ", lista)
    img = [["2" for col in range(inpx)] for row in range( inpy )]
    print("\nInit img: ", img)
    i = 0
    for row in range(inpy):
        for col in range(inpx):
            for layer in range(len(lista)):
                color = lista[layer][row][col]
                print(i, color, row, col)
                i+=1
                # if color != 2 and img[row][col] == 2:
                if color != "2" and img[row][col] == "2":
                    print("dnsjkandksa",color)
                    img[row][col]=color
    print("\nDone img: ", img)
    with open("out.txt", "w") as f:
        for row in img:
            for col in row:
                if col == "0":
                    f.write("0")
                if col == "1":
                    f.write("#")
                if col == "2":
                    f.write("r")
            f.write("\n")
    return img


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        d = f.read()
        print(genimg(calc(d, 25, 6, False), 25, 6))
