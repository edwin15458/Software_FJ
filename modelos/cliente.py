"""
Clase Cliente del sistema Software FJ.
"""

from modelos.excepciones import ClienteError


class Cliente:
    """Representa un cliente del sistema."""

    def __init__(self, documento, nombre, telefono):
        self.set_documento(documento)
        self.set_nombre(nombre)
        self.set_telefono(telefono)

    # Encapsulación mediante getters y setters

    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        if not str(documento).isdigit():
            raise ClienteError("El documento debe contener solo números.")
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        if not str(telefono).isdigit():
            raise ClienteError("El teléfono debe contener solo números.")
        self.__telefono = telefono

    def __str__(self):
        return f"{self.__nombre} - {self.__documento}"