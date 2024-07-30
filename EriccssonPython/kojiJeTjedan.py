# u kojem tjednu smo
# pretpostavka da je 52 tj u god

import datetime
from datetime import date


pocetakGod = date(2024,1,1)

today = date.today()

razlikaDani = today - pocetakGod

print(f"U {razlikaDani.days//7}. tj smo")


# import datetime
# from datetime import datetime
# datum = datetime(2021, 9, 12)

# rj = {1: 31,
#       2: 28,
#       3: 31,
#       4: 30,
#       5: 31,
#       6: 30,
#       7: 31,
#       8: 31,
#       9: 30,
#       10: 31,
#       11: 30,
#       12: 31}

# rez = 0
# mj = datum.month
# for key, value in rj.items():
#     if(key < mj):
#         rez = rez+rj[key]

# krajnjirez = rez+datum.day
# print("tjedan je: ", krajnjirez/7)