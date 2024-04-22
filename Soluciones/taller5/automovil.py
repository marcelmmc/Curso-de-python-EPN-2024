from vehiculo import Vehiculo
class Automovil(Vehiculo):
    def __init__(self, color, marca, num_pasajeros, gasolina):
        super().__init__(color, marca, num_pasajeros, gasolina)

    def conducir(self):
        print("Conduciendo" + " ... " + self.__str__())

    def __str__(self):
        return super().__str__()
