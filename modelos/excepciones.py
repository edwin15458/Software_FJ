"""
Excepciones personalizadas del sistema Software FJ.
"""

class ClienteError(Exception):
    """Error relacionado con los clientes."""
    pass


class ServicioError(Exception):
    """Error relacionado con los servicios."""
    pass


class ReservaError(Exception):
    """Error relacionado con las reservas."""
    pass