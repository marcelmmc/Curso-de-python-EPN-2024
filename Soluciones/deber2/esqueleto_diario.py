import os
from datetime import datetime

def manejar_accion_escribir():
    pass

def manejar_accion_leer():
    pass

diario_directorio = os.path.normpath('diario_entradas')

# Aqui deberas crear la carpeta 'diario_entradas' si no existe


while True:

    # Aqui deberas preguntar al usuario que accion desea realizar
    accion = ...

    if accion == 'escribir':
        manejar_accion_escribir()
    else:
        manejar_accion_leer()

    print('')

    # Aqui deberas preguntar al usuario si desea realizar otra accion
    continuar = ...

    if continuar == 'no':
        break
    print('')
