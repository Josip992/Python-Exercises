# Napisati rekurzivnu funkciju koja vraća zbroj svih znamenaka broja.

def zbrajanje(broj,zbroj):
    while(broj != 0):
        return(zbrajanje(broj//10,zbroj=zbroj+broj%10))
    return zbroj    

broj=int(input("unesite neki broj: "))
zbroj=0

print(zbrajanje(broj,zbroj))    