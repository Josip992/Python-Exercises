# napisati 2 razlomka i napisati ih u oblik brojnik i nazivnik
# svak svoja varijabla
# zbrojiiti ih
# ako je rjesenje 6/9, triba skratit da ispane 2/3

prviBrojnik = int(input("Upisite brojnik prvoga razlomka\n"))
prviNaz = int(input("Upisite nazivnik prvoga razlomka\n"))

drugiBrojnik = int(input("Upisite brojnik drugog razlomka\n"))
drugiNaz = int(input("Upisite nazivnik drugog razlomka\n"))

rezNaz = 0
rezBrojnik = 0

rezNaz = prviNaz * drugiNaz
rezBrojnik = int((rezNaz/prviNaz) * prviBrojnik + (rezNaz/drugiNaz) * drugiBrojnik)

print(f"Neskraceni rezultat: {rezBrojnik}/{rezNaz}")

while(1):
    if rezNaz%2 == 0 and rezBrojnik%2==0:
        rezNaz = rezNaz//2
        rezBrojnik = rezBrojnik//2
    elif rezNaz%3 == 0 and rezBrojnik%3==0:
        rezNaz = rezNaz//3
        rezBrojnik = rezBrojnik//3
    elif rezNaz%5 == 0 and rezBrojnik%5==0:
        rezNaz = rezNaz//5
        rezBrojnik = rezBrojnik//5
    elif rezNaz%7 == 0 and rezBrojnik%7==0:
        rezNaz = rezNaz//7
        rezBrojnik = rezBrojnik//7
    else:
        print("Broj maksimalno skracen!")
        break

print(f"Skraceni rezultat: {rezBrojnik}/{rezNaz}")