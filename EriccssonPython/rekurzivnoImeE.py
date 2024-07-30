# ispisi svoje ime 10 puta
# ne koristi petlje, vec rekurziju
# prvo bazni slucaj koji prekida rekurziju
# onda parametar u rekurzivnom pozivu koji konvergira prema baznom slucaju

def rekurzivnoIme(ime,n):
    if n == 0:
        return 1
    print(ime)
    return rekurzivnoIme(ime,n-1)
print(rekurzivnoIme("Josip",10))