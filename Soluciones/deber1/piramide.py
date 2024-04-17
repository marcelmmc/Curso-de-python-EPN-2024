filas = int(input('Numero de filas: '))
# filas = 2
for fila in range(filas):
    for col in range(fila+1):
        print('* ', end='')
    print('')
