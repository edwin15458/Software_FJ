from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta para representar un servicio.
    """

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def descripcion(self):
        """Devuelve una descripción del servicio."""
        pass