# pretvori x i y u binarni zapis pa izracunaj x AND y
# x or y (ne triba kod)


def decToBin(dec):
    ostatak=0
    binBrObrnuto=[]
    binBr = []
    while dec>0:
        ostatak = dec %2
        dec//=2
        binBrObrnuto.append(ostatak)
    for i in range(len(binBrObrnuto)-1,-1,-1):
        binBr.append(str(binBrObrnuto[i]))
    binBroj = int("".join(binBr))
    return binBroj

x=13
y=22

print(decToBin(x))
