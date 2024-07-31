# Napisati program koji od korisnika čita brojeve. Program čita brojeve dok
# god su upisani brojevi naizmjenice parni i neparni.

brojac=0 #provjerava je li prvi unos
prethodni=0 #pamti prethodni unos
while(1): #beskonacna petlja
    br1=int(input("unesite prvi broj: ")) #unos broja
    if(brojac == 0): #provjerava je li ovo prvi unos, jer u prvom unosu nista ne usporeduje
        prethodni=br1 #prethodni postavlja na trenutno uneseni broj(ako smo unili 7, prethodni postaje 7)
        brojac+=1 #brojac se postavlja na 1, imali smo prvi unos
        continue #preskace sav kod ispod sebe i vraca se u while
    if(br1&1 ^ prethodni&1): #provjerava jesu li trenutni unos i prijasnji parni ili neparni
        prethodni=br1 #postavlja prethodni na trenutni
        continue #tehnicki nebitno al eto reda radi
    else: #ako su oba parna ili neparna
        break #prekini petlju, zavrsava se program