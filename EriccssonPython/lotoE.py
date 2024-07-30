# 1. Igra se loto 6/45.
#  Korisnk unosi sam 6 brojeva.
# Izvlači se 6 nasumicnih brojeva.(nema ponavljanja)
#  Onda se provjerava koliko je pogodenih.
# Ako je pogodeno manje od tri ili svih 6 igra staje.
#  Ukoliko je pogodeno 3 4 ili 5, korisnik opet upisuje brojeve i izvlace se nasumicno novi.
#  Ponavljanja izvlacenja može bit maximalno 100

import random

odabraniBrojevi = []
randBrojevi = set()
brojac = 0
maxBrIgara = 100

while(maxBrIgara != 0):
    while len(odabraniBrojevi) != 6:
        tmp= input("Upisite broj: \n")
        odabraniBrojevi.append(tmp)


    while len(randBrojevi) !=6:
        slucajnoGeneriraniBr = random.randint(1,45)
        randBrojevi.add(slucajnoGeneriraniBr)

    for x in randBrojevi:
        if x in odabraniBrojevi:
            brojac+=1
    if (brojac < 3) or (brojac == 6):
        print(f"Pogodeno je {brojac} brojeva. Igra prestaje!\n")
        break