# korisnik upisuje broje 0-9 i slova A-J
# ako je unio 1 to je a , ako je unio a to je 0

dict={0:"A",
      1:"B",
      2:"C",
      3:"D",
      4:"E",
      5:"F",
      6:"G",
      7:"H",
      8:"I",
      9:"J"}

unos = int(input("Upisite 1 za broj(0-9) ili 2 za slovo(A-J): \n"))

if unos == 1:
    unos = int(input("Upisite broj(0-9): \n"))
    for key,value in dict.items():
        if key == unos:
            print(dict[key])

elif unos == 2:
    unosStr = input("Upisite slovo(A-J): \n")
    for key,value in dict.items():
        if dict[key] == unosStr:
            print(key)
