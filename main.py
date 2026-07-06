"""
Proyecto: Software FJ
Sistema de gestión de clientes, servicios y reservas.

Autor: edwin daniel suarez gomez

"""
from modelos.cliente import Cliente
from modelos.reserva_sala import ReservaSala
from modelos.reserva import Reserva
from modelos.excepciones import ClienteError, ReservaError


def main():

    try:

        cliente = Cliente("12345", "Edwin", "3001234567")

        servicio = ReservaSala(150000, 20)

        reserva = Reserva(cliente, servicio, 3)

        reserva.confirmar()

        print(reserva)

        print("Costo:", reserva.procesar())

    except (ClienteError, ReservaError) as e:

        print("Error:", e)

    finally:

        print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()