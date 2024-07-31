# Napisati funkciju koja kao parametar prima broj i vraća True ako su prva
# i zadnja znamenka broja jednake. U suprotnom vraća False.

br1 = int(input("unesite prvi broj: "))

zznam=br1%10
pznam=0

while(br1 != 0):
    pznam=br1%10
    br1=br1//10
if(pznam==zznam):
    print("True")
else:
    print("False")    