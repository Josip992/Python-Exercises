# 6. Funkcija rotiraj( niz, brojKoraka) koja ovisno o brojuKoraka ciklički pomice niz u desno.
# Pr.Rotiraj ({1,2,3,4}, 2 ) => { 3,4,1,2 }

def rotacioni(OGniz,brKoraka):
    niz=[]
    for i in range(brKoraka, len(OGniz)):
        niz.append(OGniz[i])
    for i in range(0,brKoraka):
        niz.append(OGniz[i])
    print(niz)

def main():
    orgNiz=[1,2,3,4]
    rotacioni(orgNiz,2)

if __name__ == "__main__":
    main()