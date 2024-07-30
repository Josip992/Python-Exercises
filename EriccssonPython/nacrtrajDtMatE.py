#Donje trokutasta matrica (za gornju je samo uvjet j<i)

matrica=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(0,len(matrica)):
    print(i)
    for j in range(0,len(matrica)):
        if(j>i):
            matrica[i][j]=0
print(matrica)