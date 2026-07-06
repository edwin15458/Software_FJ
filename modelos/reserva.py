"""
Clase Reserva del sistema Software FJ.
"""

from modelos.excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero.")

        self.duracion = duracion

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        if self.estado == "Cancelada":
            raise ReservaError("No se puede procesar una reserva cancelada.")

        return self.servicio.calcular_costo()

    def __str__(self):
        return (
            f"Cliente: {self.cliente}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}"
        )