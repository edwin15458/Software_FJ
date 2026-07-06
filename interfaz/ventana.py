import tkinter as tk
from tkinter import ttk, messagebox

from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria
from modelos.sistema import Sistema
from utils.logger import registrar_log


class Ventana:

    def __init__(self):

        self.sistema = Sistema()

        self.ventana = tk.Tk()
        self.ventana.title("Software FJ")
        self.ventana.geometry("650x500")

        tk.Label(self.ventana, text="Nombre").pack()

        self.nombre = tk.Entry(self.ventana)
        self.nombre.pack()

        tk.Label(self.ventana, text="Documento").pack()

        self.documento = tk.Entry(self.ventana)
        self.documento.pack()

        tk.Label(self.ventana, text="Teléfono").pack()

        self.telefono = tk.Entry(self.ventana)
        self.telefono.pack()

        tk.Label(self.ventana, text="Servicio").pack()

        self.combo = ttk.Combobox(
            self.ventana,
            values=[
                "Reserva Sala",
                "Alquiler Equipo",
                "Asesoría"
            ]
        )

        self.combo.current(0)
        self.combo.pack()

        tk.Label(self.ventana, text="Duración").pack()

        self.duracion = tk.Entry(self.ventana)
        self.duracion.pack()

        tk.Button(
            self.ventana,
            text="Registrar Reserva",
            command=self.registrar
        ).pack(pady=10)

        self.lista = tk.Listbox(self.ventana, width=70, height=10)
        self.lista.pack()
        
        tk.Button(
        self.ventana,
    text="Simular Pruebas",
    command=self.simular_pruebas
).pack(pady=5)

        self.ventana.mainloop()

    def registrar(self):

        try:

            cliente = Cliente(
                self.documento.get(),
                self.nombre.get(),
                self.telefono.get()
            )

            opcion = self.combo.get()

            if opcion == "Reserva Sala":

                servicio = ReservaSala(150000, 20)

            elif opcion == "Alquiler Equipo":

                servicio = AlquilerEquipo(80000, "Video Beam")

            else:

                servicio = Asesoria(120000, "Python")

            reserva = Reserva(
                cliente,
                servicio,
                int(self.duracion.get())
            )

            reserva.confirmar()

            self.sistema.agregar_cliente(cliente)
            registrar_log("Cliente registrado.")

            self.sistema.agregar_servicio(servicio)

            self.sistema.agregar_reserva(reserva)
            registrar_log("Reserva creada.")
            
            

            self.lista.insert(
                tk.END,
                f"{cliente} | {servicio.nombre} | {reserva.estado}"
            )

            registrar_log("Reserva registrada correctamente.")

            messagebox.showinfo(
                "Éxito",
                "Reserva registrada correctamente."
            )
            
        except Exception as e:

           registrar_log(f"Error: {e}")

           messagebox.showerror(
            "Error",
           str(e)
         )
           
        else:
         registrar_log("Proceso completado correctamente.")
         
        finally:
          registrar_log("Fin del proceso de registro.")

    def simular_pruebas(self):
        
        self.lista.delete(0, tk.END)

        pruebas = [

            lambda: Cliente("12345", "Juan", "3001234567"),

            lambda: Cliente("ABC", "Pedro", "3001234567"),

            lambda: Cliente("67890", "", "3001234567"),

            lambda: Cliente("11111", "Ana", "telefono"),

            lambda: ReservaSala(150000, 20),

            lambda: AlquilerEquipo(80000, "Video Beam"),

            lambda: Asesoria(120000, "Python"),

            lambda: Reserva(
                Cliente("22222", "Laura", "3011111111"),
                ReservaSala(150000, 20),
                3
            ),

            lambda: Reserva(
                Cliente("33333", "Carlos", "3022222222"),
                ReservaSala(150000, 20),
                -5
            ),

            lambda: Reserva(
                Cliente("44444", "María", "3033333333"),
                Asesoria(100000, "Redes"),
                2
            ).procesar()

        ]

        for i, prueba in enumerate(pruebas, start=1):

            try:

                prueba()

                registrar_log(f"Prueba {i}: Correcta")

                self.lista.insert(
                    tk.END,
                    f"Prueba {i}: Correcta"
                )

            except Exception as e:

                registrar_log(f"Prueba {i}: {e}")

                self.lista.insert(
                    tk.END,
                    f"Prueba {i}: Error -> {e}"
                )

        messagebox.showinfo(
            "Pruebas",
            "Las 10 operaciones se ejecutaron."
        )
   
