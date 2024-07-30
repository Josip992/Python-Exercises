# unesi npr 4
# 1
# 12
# 123
# 1234

unosStr = input("Upisite broj: ")
unosInt = int(unosStr)

for i in range(1,unosInt+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
