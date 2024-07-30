def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

def decimal_to_hex(decimal_number):
    hex_representation = hex(decimal_number)[2:]
    return hex_representation

def decimal_to_octal(decimal_number):
    octal_representation = oct(decimal_number)[2:]
    return octal_representation

def binary_to_decimal(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

def binary_to_octal(binary_string):
    octal_number = int(binary_string, 8)
    return octal_number

def binary_to_hex(binary_string):
    hex_number = int(binary_string, 16)
    return hex_number

decimal_number = 10
binary_representation = decimal_to_binary(decimal_number)
print(f"Decimal {decimal_number} to binary: {binary_representation}")

decimal_number = 10
hex_representation = decimal_to_hex(decimal_number)
print(f"Decimal {decimal_number} to hex: {hex_representation}")

decimal_number = 10
octal_representation = decimal_to_octal(decimal_number)
print(f"Decimal {decimal_number} to oct: {octal_representation}")

binary_string = "1010"
decimal_number = binary_to_decimal(binary_string)
print(f"Binary {binary_string} to decimal: {decimal_number}")

binary_string = "1010"
hex_number = binary_to_hex(binary_string)
print(f"Binary {binary_string} to hex: {hex_number}")

binary_string = "1010"
oct_number = binary_to_octal(binary_string)
print(f"Binary {binary_string} to oct: {oct_number}")
