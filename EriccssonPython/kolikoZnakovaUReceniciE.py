# 8. Uneses proizvoljnu recenicu
#  i program ispisuje od kojih se znakova recenica sastoji
#  i koliko se puta pojavia.
#  Recenica zavrsava sa . ! Ili sa ?

recnica = input("Upisite recenicu: \n")
brojac = 0
dict = {}

for i in recnica:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
    brojac+=1
print(dict)
print(f"Broj znakova: {brojac}")