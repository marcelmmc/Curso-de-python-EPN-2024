from vehiculo import Vehiculo
from automovil import Automovil
from camion import Camion
camion_uno = Camion("rojo", "Chevrolet", 4, "extra",20)
camion_dos = Camion("azul", "Hino", 2, "diesel",30)
camion_tres = Camion("blanco", "Toyota", 4, "extra",40)
automovil_uno = Automovil("rojo", "Chevrolet", 4, "extra")
automovil_dos = Automovil("azul", "Hino", 2, "diesel")
automovil_tres = Automovil("blanco", "Toyota", 4, "extra")


print(automovil_uno)
print(automovil_dos)
print(automovil_tres,end="\n\n")
print("Conduzcamos nuestros camions ...")
automovil_uno.conducir()
automovil_dos.conducir()
automovil_tres.conducir()
print("")

print(camion_uno)
print(camion_dos)
print(camion_tres,end="\n\n")
print("Conduzcamos nuestros camions ...")
camion_uno.conducir()
camion_dos.conducir()
camion_tres.conducir()
