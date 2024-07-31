# Napisati funkciju koja čita dva po dva broja dok god korisnik ne unese dva broja koja su oba veća od prethodna dva broja. Funkcija nakon toga
# vraća ta dva broja. Prva dva unesena broja se ne vraćaju

# Napisati funkciju koja čita dva po dva broja dok god korisnik ne unese
# dva broja koja su oba veća od prethodna dva broja. Funkcija nakon toga
# vraća ta dva broja. Prva dva unesena broja se ne vraćaju.

def unos():
    prviUnos=0
    pr1=0
    pr2=0
    while(1):
        br1 = int(input("unesite prvi broj: "))
        br2 = int(input("unesite drugi broj: "))

        if(prviUnos==0):
            prviUnos+=1

        else:
            if(br1 > pr1 and br2 > pr2):
                return (br1, br2)
        pr1 = br1
        pr2 = br2
print(unos())