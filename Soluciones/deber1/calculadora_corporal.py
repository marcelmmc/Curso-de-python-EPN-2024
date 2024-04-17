def calculator_corporal(nombre, peso_kg, altura_m):
  bmi = peso_kg / (altura_m ** 2)
  print("el peso corporal es de: ", bmi)
  if bmi >= 25 :
    return nombre + " tiene sobrepeso"
  else :
    return nombre + " no tiene sobrepeso"

while(True):
  kg = float(input("Peso en kilogramos: "))
  m = float(input("Estatura en metros: "))
  nombre = input("Nombre de persona: ")
  print(calculator_corporal(nombre,kg,m))
  print("****************************")
