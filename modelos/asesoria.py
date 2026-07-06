from modelos.servicio import Servicio


class Asesoria(Servicio):

    def __init__(self, precio, tema):
        super().__init__("Asesoría", precio)
        self.tema = tema

    def calcular_costo(self, descuento=0):
        return self.precio - descuento

    def descripcion(self):
        return f"Asesoría sobre {self.tema}"