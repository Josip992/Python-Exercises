# postoji string. uzeti svako drugu recenicu i ispisati u toj recenici rici obrnuto
# i velika slova u mala, itd.
#svakoDruga = re.split(r'[.!?]', string)
import re

string = "ukradeni! mat crni cayenne. Carpe Diem. sudoku je igra? otorinolaringologija pas macka"

svakoDruga = re.split(r"[!.?]",string)
svakoDrugaPravaObrnuta = []
svakoDrugaPrava=[]

for x in range(0,len(svakoDruga),2):
    if x%2 ==0:
        svakoDrugaPrava.append(svakoDruga[x])

print(svakoDruga)
print(svakoDrugaPrava)

for i in svakoDrugaPrava:
    for j in range(len(i)-1,-1,-1):
        if i[j].islower():
            uVeliko = i[j].upper()
            svakoDrugaPravaObrnuta.append(uVeliko)
        elif i[j].isupper():
            uMalo = i[j].lower()
            svakoDrugaPravaObrnuta.append(uMalo)
    svakoDrugaPravaObrnuta.append(" ")
#print("".join(svakoDrugaPravaObrnuta))
    
print(svakoDrugaPravaObrnuta)
    
