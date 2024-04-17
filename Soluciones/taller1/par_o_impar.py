num = int(input("numero de usuario: "))
# modulus = num % 2
bit_operation = num & 1
if bit_operation == 1:
# if modulus == 1:
    print("Este numero es impar")
else:
    print("Este numero es par")
