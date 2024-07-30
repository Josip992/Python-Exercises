# korisnik upisuje brojeve od 3 do 27
# odredi je li paran il neparan bez koristenja djeljenja i modula

while(1):
    brojStr = input("Unesite broj izmedu 3 i 27: \n")
    brojInt = int(brojStr)
    if brojInt > 2 and brojInt < 28:
        if brojInt == 3 or brojInt == 5 or brojInt == 7 or brojInt == 9:
            print(f"{brojInt} je neparan broj")
        elif brojInt == 4 or brojInt == 6 or brojInt == 8:
            print(f"{brojInt} je paran broj")
        elif len(brojStr) > 1:
            zadnjaZnam = int(brojStr[len(brojStr)-1])
            if zadnjaZnam == 1 or zadnjaZnam == 3 or zadnjaZnam == 5 or zadnjaZnam == 7 or zadnjaZnam == 9:
                print(f"{brojInt} je neparan broj")
            elif zadnjaZnam== 2 or zadnjaZnam == 4 or zadnjaZnam == 6 or zadnjaZnam == 8 or zadnjaZnam == 0:
                print(f"{brojInt} je paran broj")
    else:
        print("Pogresan unos")