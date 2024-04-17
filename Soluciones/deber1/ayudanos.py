def calcular_media(num, entradas):
    media = num/entradas
    print("la media de los numeros ingresados es: " + str(media))

def main():
    num_registrados = 0
    suma_total = 0
    while True:
      num = int(input('Ingresa un numero: '))
      if(num < 0):
          print("Error: Programa solo espera numeros positivos enteros")
          break
      num_registrados += 1.0
      suma_total += num
      print("la sumatoria de los numeros es: " + str(suma_total))
      calcular_media(suma_total, num_registrados)
      actualizar_numero_mayor(num)

def actualizar_numero_mayor(num):
    global numero_mayor
    if(num > numero_mayor):
        numero_mayor = num
        print("El mayor numero visto ha sido: " + str(numero_mayor))

numero_mayor = 0
main()
