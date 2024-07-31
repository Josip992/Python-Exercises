# Napisati program koji od korisnika čita brojeve. Program čita brojeve dok
# god je upisani broj veći od svih prethodnih brojeva.

prbr=0

while(1):
    br=int(input("Unesite neki broj: "))
    if(br>prbr):
       prbr=br
    else:
        break