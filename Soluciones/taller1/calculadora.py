operador = input('Ingrese operador: ')

numero_1 = input('Primer numero: ')
numero_2 = input('Segundo numero: ')

numero_1 = float(numero_1)
numero_2 = float(numero_2)

if operador == '+':
    resultado = numero_1 + numero_2
    print('Resultado es', resultado)
elif operador == '-':
    resultado = numero_1 - numero_2
    print('Resultado es', resultado)
elif operador == '*':
    resultado = numero_1 * numero_2
    print('Resultado es', resultado)
elif operador == '/':
    resultado = numero_1 / numero_2
    print('Resultado es', resultado)
else:
    print('Operador invalido')
