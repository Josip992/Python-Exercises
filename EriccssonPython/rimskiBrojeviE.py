# za uneseni broj ispisuje se rimski(manji od 100)
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# 1,4,5,9,10,40,50,90,100,400,500,900,1000 (1,4,5,9...)

def rimski(unos):
    rimski = ""
    rimskiDict ={
                 100:"C",
                 90:"XC",
                 50:"L",
                 40:"XL",
                 10:"X",
                 9:"IX",
                 5:"V",
                 4:"IV",
                 1:"I"
                 }
    for key,value in rimskiDict.items():
        while key <= unos:
            rimski = rimski + value
            unos = unos - key
    return rimski

print(rimski(76))


