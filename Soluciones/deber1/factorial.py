def factorial(num):
    # para calcular el factorial tenemos que recordar la formula factorial
    # n! = n x (n - 1)! = n x (n-1) x (n-2) x ... x 1
    # 1! = 1
    # 2! = 2x1! = 2x1
    # 3! = 3x2! = 3x2x1! = 3x2x1
    # el truco en resolver el problema es darnos cuenta que el factorial tiene
    # sequencia de numeros son multiplicados en este caso ayudenemos
    # de for in range(inicio, fin, aumento) para genera esta sequencia
    # RECUERDA EL FIN DE UN for in ES EXCLUIDO
    res = 1
    for n in range(num,0,-1):
        res *= n
    print("El factorial de " + str(num) + " es: " + str(res))

while(True):
  try:
      num = int(input("Ingresa tu numero: "))
      if num < 0 :
          print("Este programa solo acepta valores numericos no negativos")
          continue
      else:
          factorial(num)
          break
  except Exception:
      print("Este programa solo acepta valores numericos no negativos")
