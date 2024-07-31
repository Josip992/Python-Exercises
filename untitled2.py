# Napisati rekurzivnu funkciju koja vraća zbroj svih znamenaka broja.

def zbroj(broj):
    zbroj=0
    while(broj != 0):
        zbroj=zbroj+broj%10
        broj=broj//10
    return(zbroj)

broj=int(input("unesite neki broj: "))


print(zbroj(broj))    