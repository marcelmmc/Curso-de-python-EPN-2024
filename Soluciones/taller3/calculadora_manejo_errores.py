def entrada_de_datos(texto):
    while True:
        try:
            numero = float(input(texto))
            return numero
        except ValueError:
            print('Valor invalido')

operador = input('Ingrese operador: ')

# numero_1 = input('Primer numero: ')
# numero_2 = input('Segundo numero: ')
numero_1 = entrada_de_datos('Primer numero: ')
numero_2 = entrada_de_datos('Segundo numero: ')

# numero_1 = float(numero_1)
# numero_2 = float(numero_2)

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
    try:
        resultado = numero_1 / numero_2
        print('Resultado es', resultado)
    except Exception:
        print('Error: No es posible dividir para zero')
else:
    print('Operador invalido')
