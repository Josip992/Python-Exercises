# mnozi brojeve rekurzivno do N
# za rekurziju - prvo odredujemo osnovni tj bazni slucaj (slucaj kada se rekurzija prekida (u nasem slucaju kada nema vise brojeva za mnozite))
#              - u rekurzivnom pozivu parametar odredujemo tako da se konvergira prema baznom slucaju (u nasemm zadatku, smanjujemo parametar do 1)
def rekMnozenje(n):
    if n <= 1:
        print("Kraj")
        return 1
    result = n*rekMnozenje(n-1)
    print(result)
    return result

print(rekMnozenje(10))