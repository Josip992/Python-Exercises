# 4. Korisnik unese rodendan u formatu DD:MM:YYYY
# program racuna koliko dana još ima do rodendana i koliko će imat godina.

import datetime
from datetime import timedelta
from datetime import date

today = date.today()

trenutniDan = today.day
trenutniMj = today.month
trenutnaGod = today.year

tmp = input("dd:mm:yyyy: ").split(":")

danRod, mjesRod,godRod = map(int,tmp)


if(trenutnaGod > godRod and trenutniMj >= mjesRod and trenutniDan >= danRod):
    brGod = trenutnaGod - godRod
    print(f"Korisnik ima {brGod} godina")
elif(trenutnaGod > godRod and trenutniMj < mjesRod):
    brGod = trenutnaGod - godRod - 1  
    print(f"Korisnik ima {brGod} godina")



next_birthday = date(today.year, mjesRod, danRod)

if today > next_birthday:
    next_birthday = date(today.year + 1, mjesRod, danRod)

difference = next_birthday - today

remaining_months = difference.days 
remaining_days = difference.days % 30