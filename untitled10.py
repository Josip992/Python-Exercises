#    Napisati funkciju koja prima dva broja. Funkcija ispisuje sve brojeve do
#    1000 koji dijele oba primljena broja.

broj1=int(input("unesite 1. broj: "))
broj2=int(input("unesite 2. broj: "))
for i in range(1,1000):
    if(i%broj1==0 & i%broj2==0):
        print(i)
        
        