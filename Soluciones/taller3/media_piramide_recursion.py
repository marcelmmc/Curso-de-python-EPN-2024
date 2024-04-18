while True:
    try:
        filas = int(input('Numero de filas: '))
        break
    except ValueError:
        print('Valor invalido')


def media_piramide(no_filas):
    if no_filas == 0:
        return
    else:
        media_piramide(no_filas-1)
        print('*'*no_filas)
        return

media_piramide(filas)
