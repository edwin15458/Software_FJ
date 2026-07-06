from abc import ABC, abstractmethod
# Clase abstracta que define el comportamiento común
# para todos los servicios ofrecidos por Software FJ.

class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass