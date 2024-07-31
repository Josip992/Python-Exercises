# Napisati program koji u beskonačnoj petlji ispisuje proste brojeve. Program se oslanja na funkciju prost() (napisati je).

brojac=1

while(1):
    djeljiv=0 #jel broj prost
    for i in range(2, brojac//2):
        if(brojac % i == 0):
            djeljiv=1
            break
    if(djeljiv!=1):
        print(brojac)
    brojac+=1