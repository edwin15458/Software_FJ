from modelos.servicio import Servicio
# Servicio especializado para la reserva de salas.

class ReservaSala(Servicio):

    def __init__(self, precio, capacidad):
        super().__init__("Reserva de Sala", precio)
        self.capacidad = capacidad

    def calcular_costo(self, descuento=0):
        return self.precio - descuento

    def descripcion(self):
        return f"Sala para {self.capacidad} personas."