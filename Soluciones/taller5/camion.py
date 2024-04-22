from vehiculo import Vehiculo
class Camion(Vehiculo):
    def __init__(self, color, marca, num_pasajeros, gasolina, carga):
        super().__init__(color, marca, num_pasajeros, gasolina)
        self.carga = carga
    def conducir(self):
        print("Conduciendo" + " ... " + self.__str__())
    def __str__(self):
        return "Camion marca " + self.marca + " color " + self.color + " de " + str(self.num_pasajeros) + " pasajeros que funciona a gasolina " + self.gasolina + " y tiene una capacidad de " + str(self.carga) + " toneladas"
    