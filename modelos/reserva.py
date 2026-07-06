"""
Clase Reserva del sistema Software FJ.
"""

from modelos.excepciones import ReservaError
from utils.logger import registrar_log


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
        registrar_log("Reserva confirmada.")

    def cancelar(self):
        self.estado = "Cancelada"
        registrar_log("Reserva cancelada.")

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo()

        except Exception as e:
            raise ReservaError("Error al procesar la reserva.") from e

        else:
            registrar_log("Reserva procesada correctamente.")
            return costo

        finally:
            registrar_log("Fin del procesamiento de la reserva.")

    def __str__(self):
        return (
            f"Cliente: {self.cliente}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}"
        )