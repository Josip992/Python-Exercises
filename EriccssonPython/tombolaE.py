import random

# tombola, 3reda po 4 broja,svaki krug se generira po 15 brojeva
# koliko je proslo krugova dok se nije dobila cinkvina
# (brojevi su 1 do 90 na listicu) ->rand

def drawn_numbers():
    return [random.randint(1, 90) for _ in range(15)]


def generirajListic():
    return [[random.randrange(1,91) for i in range(0,3)] for j in range(0,4)]



listicTombola = generirajListic()
dobitniListic = drawn_numbers()

print(listicTombola)
print(dobitniListic)