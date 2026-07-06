from datetime import datetime


def registrar_log(mensaje):
    """
    Guarda eventos y errores en el archivo logs.txt
    """
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        archivo.write(f"[{fecha}] {mensaje}\n")