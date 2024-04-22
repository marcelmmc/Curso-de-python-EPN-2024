from abc import ABC, abstractmethod
class Vehiculo(ABC):
    def __init__(self, color, marca, num_pasajeros, gasolina):
        self.color = color
        self.marca = marca
        self.num_pasajeros = num_pasajeros  
        self.gasolina = gasolina
    @abstractmethod
    def __str__(self):
        return "Vehiculo marca " + self.marca + " color " + self.color + " de " + str(self.num_pasajeros) + " pasajeros que funciona a gasolina " + self.gasolina