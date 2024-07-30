# unesi datum rodenja dvi osobe
# izracunaj razliku godina, dana i miseci
# ispisi koja osoba je starija i za kolko
# samo poz rjesenje

import datetime
from datetime import time
from datetime import date

def izracunaj_starost(broj_dana):
    godine = broj_dana // 365
    preostali_dani = broj_dana % 365
    mjeseci = preostali_dani // 30
    preostali_dani %= 30

    return godine, mjeseci, preostali_dani


datRod1 = input("Prva osoba DD:MM:YYYY  ").split(":")
datRod2 = input("Druga osoba DD:MM:YYYY  ").split(":")

danRodenja1 = int(datRod1[0])
mjesecRodenja1 = int(datRod1[1])
godinaRodenja1 = int(datRod1[2])

danRodenja2 = int(datRod2[0])
mjesecRodenja2 = int(datRod2[1])
godinaRodenja2 = int(datRod2[2])

today = date.today()
danasnjiDan = today.day
danasnjiMjesec = today.month
danasnjaGodina = today.year

if danasnjiMjesec > mjesecRodenja1:
    brGod1 = danasnjaGodina - godinaRodenja1
elif danasnjiMjesec < mjesecRodenja1:
     brGod1 = danasnjaGodina - godinaRodenja1 - 1
     
if danasnjiMjesec > mjesecRodenja1:
    brGod2 = danasnjaGodina - godinaRodenja2
elif danasnjiMjesec < mjesecRodenja2:
     brGod2 = danasnjaGodina - godinaRodenja2 - 1


o1 = date(godinaRodenja1,mjesecRodenja1,danRodenja1)
o2 = date(godinaRodenja2,mjesecRodenja2,danRodenja2)



if brGod1 >= brGod2:
    razlika = o1 - o2
    broj_dana = razlika.days
    godine, mjeseci, preostali_dani = izracunaj_starost(broj_dana)
    print(f"Prva osoba je starija {godine} godina, {mjeseci} mjeseca i {preostali_dani} dana.")      
elif brGod2 >= brGod1:
    razlika = o2 - o1
    broj_dana = razlika.days
    godine, mjeseci, preostali_dani = izracunaj_starost(broj_dana)
    print(f"Druga osoba je starija {godine} godina, {mjeseci} mjeseca i {preostali_dani} dana.")  

