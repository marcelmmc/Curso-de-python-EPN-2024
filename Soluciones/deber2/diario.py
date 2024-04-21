# Autores: 
# - Alexis Rodriguez
# - Marcel Moran Calderon
from datetime import datetime
import os

def entrada_de_datos(texto, valores_validos):
    while True:
        entrada = input(texto)
        if entrada in valores_validos:
            print('')
            return entrada
        else:
            print(entrada + ' no es un valor valido, por favor seleccione otro\n')


def manejar_accion_escribir():
    fecha_actual = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    print('La nueva entrada usara la siguiente fecha y hora:', fecha_actual)

    # Ask user for data
    print('Por favor escribe tu entrada y para terminar deja 3 lineas en blanco')
    print()

    lineas_en_blanco = 0
    nueva_entrada = ''
    while True:
        nueva_linea = input()

        if nueva_linea == '':
            lineas_en_blanco += 1
        else:
            lineas_en_blanco = 0

        if lineas_en_blanco == 3:
            break

        # Add to nueva_entrada
        nueva_entrada +=  nueva_linea + '\n'

    # Save to file
    ruta_nuevo_archivo = os.path.join(diario_directorio, fecha_actual + '.txt')

    # with open('readme.txt', 'w') as file:
    with open(ruta_nuevo_archivo, 'w') as file:
        file.write(nueva_entrada)


def manejar_accion_leer():
    print('Estas son las entradas guardadas, Por favor seleccione el numero de entrada que le gustaria abrir:')
    # Get entries
    entradas = os.listdir(diario_directorio)
    for numero, entrada in enumerate(entradas):
        print('\t' + str(numero+1) + ':   ' + entrada)

    valores_validos = [str(numero+1) for numero in range(len(entradas))]
    seleccion = int(entrada_de_datos('seleccion: ', valores_validos))

    # Open the selected file
    entrada_seleccionada = entradas[seleccion-1]

    ruta_entrada_seleccionda = os.path.join(diario_directorio, entrada_seleccionada)
    with open(ruta_entrada_seleccionda) as file:
        lineas = file.readlines()
        for linea in lineas:
            print(linea, end='')


diario_directorio = os.path.normpath('diario_entradas')
os.makedirs(diario_directorio, exist_ok=True)

while True:
    acciones_validas = ['leer', 'escribir']
    accion = entrada_de_datos("Desea escribir o leer el diario? (opciones validas  'leer' o 'escribir'): ", acciones_validas)

    if accion == 'escribir':
        manejar_accion_escribir()
    else:
        manejar_accion_leer()

    print('')
    continuar = entrada_de_datos("Desea leer o escribir en el diario una vez mas? (opciones validas  'si' o 'no'): ", ['si', 'no'])
    if continuar == 'no':
        break
    print('')
