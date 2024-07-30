# od unesenog stringa ispisi samo velika slova

rez =""
unosStr = input("Upiste string: ")

for c in unosStr:
    if c.isupper():
        rez=rez+str(c)

print(rez)