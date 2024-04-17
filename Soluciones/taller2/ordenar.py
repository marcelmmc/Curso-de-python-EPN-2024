cantidad_numeros = int(input('Cuantos numeros deseas ordenar? '))
descendiente = input('Deseas ordenarlos de forma descendiente? ')
numeros = []
for indice in range(cantidad_numeros):
    numero = int(input('Ingresa el numero ' + str(indice+1) + ': '))
    numeros.append(numero)

reverse = descendiente == 'si'
numeros.sort(reverse=reverse)
print('Numeros ordenados son: ', end='')
for numero in numeros:
    print(numero, end=' ')
