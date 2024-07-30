# unesi heksa i izvuci jedan dekadski(random)
# njihov razlika / zbroj i napisi ko oktalni


def decToHex(dec):
    hexZnakovi = "0123456789ABCDEF"
    hex = ""
    ostatak = 0

    while(dec>0):
        ostatak = dec%16
        dec = dec //16
        hex = hexZnakovi[ostatak] + hex

    return hex


def hexToDec(hex):
    hexZnakovi = "0123456789ABCDEF"
    dec = 0

    for i in hex:
        dec = dec * 16 + hexZnakovi.index(i)

    return dec

def decToOct(dec):
    octZnakovi = "01234567"
    oct = ""
    ostatak = 0

    while(dec>0):
        ostatak = dec % 8
        dec = dec //8
        oct = octZnakovi[ostatak] + oct
    
    return oct

def octToDec(oct):
    octZnakovi="01234567"
    dec=0

    for i in oct:
        dec = dec * 8 + octZnakovi.index(i)

    return dec

def decToBin(dec):
    binZnakovi="01"
    bin = ""
    ostatak = 0

    while(dec>0):
        ostatak = dec %2
        dec = dec//2    
        bin = binZnakovi[ostatak] + bin
    return bin

def binToDec(bin):
    binZnakovi="01"
    dec = 0

    for i in bin:
        dec = dec * 2 + binZnakovi.index(i)
    return dec
print("Dec u hex: ", decToHex(123))
print("Hex u dec: ", hexToDec("7B"))

print("Dec to octal: ", decToOct(123))
print("Oct to dec: ", octToDec("173"))

print("Dec u bin: ", decToBin(10))
print("Bin u dec: ", binToDec("1010"))