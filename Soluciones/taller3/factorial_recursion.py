def factorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num*factorial(num-1)

num_fact = int(input("Ingrese numero: "))

print("Numero factorial es " , factorial(num_fact ))
