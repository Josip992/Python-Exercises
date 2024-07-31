# apisati program koji od korisnika čita 10 pozitivnih brojeva. Nakon
# svakog unosa, program ispisuje sve djelitelje unesenog broja. Program
# ignorira negativne brojeve. Ako korisnik unese 0, program ispisuje "kraj"
# i prekida se. /*/*

brojac=0

while(brojac<10):
    broj=int(input("Unesite neki pozitivan broj: "))
    if(broj>0):
        for i in range(1,broj):
            if(broj%i == 0):
                print(i)
        brojac+=1
    elif(broj==0):
        print("kraj")
        break
    
                   