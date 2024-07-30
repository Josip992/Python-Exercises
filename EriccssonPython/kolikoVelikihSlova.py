# recenica i triba ispisat kolko rici pocinje s velikim slovom i ispisat te rici


def velika(recenica):
    velika_lista = []

    for rijec in recenica:
        print(rijec)
        if rijec[0].isupper():
            velika_lista.append(rijec)

    print(velika_lista)
    return velika_lista

recenica = "Ovo je recENICA s Velikim SLOVIMA"
recenicaNiz = recenica.split()

rez = velika(recenicaNiz)
print(f"Rici koje pocinju sa velikim slovom ima {len(rez)}")
