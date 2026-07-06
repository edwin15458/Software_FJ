from modelos.servicio import Servicio


class AlquilerEquipo(Servicio):

    def __init__(self, precio, equipo):
        super().__init__("Alquiler de Equipo", precio)
        self.equipo = equipo

    def calcular_costo(self, descuento=0):
        return self.precio - descuento

    def descripcion(self):
        return f"Equipo: {self.equipo}"