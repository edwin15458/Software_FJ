"""
Clase principal del sistema Software FJ.
"""

from modelos.excepciones import ClienteError, ServicioError, ReservaError


class Sistema:# Clase que representa el sistema Software FJ, gestionando clientes, servicios y reservas.

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    # ---------------- CLIENTES ----------------

    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

    # ---------------- SERVICIOS ----------------

    def agregar_servicio(self, servicio):

        self.servicios.append(servicio)

    # ---------------- RESERVAS ----------------

    def agregar_reserva(self, reserva):

        self.reservas.append(reserva)

    # ---------------- CONSULTAS ----------------

    def listar_clientes(self):

        return self.clientes

    def listar_servicios(self):

        return self.servicios

    def listar_reservas(self):

        return self.reservas