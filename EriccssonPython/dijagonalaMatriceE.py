# matrica i ispisi dijagonalu i izracunaj sumu i prosjek

matrica=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
suma=0
prosjek=0
brEl=0

for i in range(0,len(matrica)):
    for j in range(0,len(matrica)):
        if i == j:
            suma+=matrica[i][j]
            brEl+=1

prosjek=suma/brEl
print(f"suma: {suma}")
print(f"projek el dijagonale: {prosjek}")