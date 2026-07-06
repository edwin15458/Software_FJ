"""
Clase Reserva del sistema Software FJ.
"""
# Clase que relaciona un cliente con un servicio.
# Permite confirmar, cancelar y procesar una reserva.

from modelos.excepciones import ReservaError
from utils.logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

        if duracion <= 0:# Valida que la duración sea mayor que cero.
            raise ReservaError("La duración debe ser mayor que cero.")
          
        self.duracion = duracion

    def confirmar(self):
        self.estado = "Confirmada"
        registrar_log("Reserva confirmada.")

    def cancelar(self):# Cambia el estado de la reserva a "Cancelada" y registra el evento en el log.
        self.estado = "Cancelada"
        registrar_log("Reserva cancelada.")

    def procesar(self):
        # Se procesa la reserva controlando posibles errores.
        try:
            costo = self.servicio.calcular_costo()

        except Exception as e:
            raise ReservaError("Error al procesar la reserva.") from e

        else:
            registrar_log("Reserva procesada correctamente.")
            return costo

        finally:
            registrar_log("Fin del procesamiento de la reserva.")

    def __str__(self):# Devuelve una representación en cadena de la reserva, incluyendo el cliente, el servicio, la duración y el estado.
        
        return (
            f"Cliente: {self.cliente}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}"
        )