"""
Proyecto: Software FJ
Sistema de gestión de clientes, servicios y reservas.

Autor: edwin daniel suarez gomez

"""
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria


def main():

    servicios = [
        ReservaSala(150000, 20),
        AlquilerEquipo(80000, "Video Beam"),
        Asesoria(120000, "Python")
    ]

    for servicio in servicios:
        print(servicio.nombre)
        print(servicio.descripcion())
        print("Costo:", servicio.calcular_costo())
        print("----------------")


if __name__ == "__main__":
    main()