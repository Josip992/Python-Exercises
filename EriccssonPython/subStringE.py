# pronaci rici u kojima je an i izbacit iz nji

string = "danas je dan ana dobar"
rijeci = string.split()  

novi_niz = []
for rijec in rijeci:
    if "an" in rijec:
        nova_rijec = ""
        i = 0
        while i < len(rijec):
            if rijec[i:i+2] == "an":
                i += 2 
            else:
                nova_rijec += rijec[i]
                i += 1
        novi_niz.append(nova_rijec)
    else:
        novi_niz.append(rijec)

novi_string = ' '.join(novi_niz)  
print(novi_niz)
