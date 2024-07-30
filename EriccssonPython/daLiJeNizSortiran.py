# provjeri je li niz sortiran ili ne, ako je ok, ako nije sortiraj ispisi

def sortiraj(niz):
    noviNiz=[]
    tmp = None
    for i in range(len(niz)-1):
        for j in range(i+1,len(niz)):
            if niz[j] < niz[i]:
                tmp = niz[i]
                niz[i] = niz[j]
                niz[j] = tmp
    print(niz)

def najveciEl(niz):
    max = niz[0]
    for i in range(1,len(niz)):
        if niz[i] > max:
            max = niz[i]
    return max

def najmanjiEl(niz):
    min = niz[0]
    for i in range(1,len(niz)):
        if niz[i] < min:
            min = niz[i]
    return min

def jeLiSortiran(niz):
    for i in range(len(niz)-1):
        if niz[i] > niz[i+1]:
            print("niz nije sortiran")
            return niz
    print("sortiran")
    return niz

niz=[11,4,3,4,1]

print(jeLiSortiran(niz))

print(najveciEl(niz))

print(najmanjiEl(niz))

sortiraj(niz)