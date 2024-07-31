# Napisati program koji ispisuje sve brojeve od 10 do 100. Za svaki broj koji
# koji ima jednake znamenke, program ispisuje "buzz" umjesto broja



 
for i in range(10,100):
    zznam=i%10
    pznam=i//10
    
    if(zznam==pznam):
        print("Buzz")
    else:
        print(i)