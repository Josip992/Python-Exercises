# 2. Odredit sve potencije broja 3 u nekom intervalu(npr. 0 do 100)
#  i omogucit ponovni unos ako je doslo do krivog unosa.
#dodat provjeru krivog unosa

dg = int(input("Unesite donju granicu: \n"))
gg = int(input("Unesite gornju granicu: \n"))
rez = 0

for i in range(dg,gg):
    rez = pow(3,i)
    if rez>= gg:
        break
    print(rez)
    


