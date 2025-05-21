from enum import Enum

class Dias(Enum):
    """
    Enum que representa los días de la semana.
    """
    LUNES = "Lunes"
    MARTES = "Martes"
    MIERCOLES = "Miércoles"
    JUEVES = "Jueves"
    VIERNES = "Viernes"
    SABADO = "Sábado"
    DOMINGO = "Domingo"


def verificar_dia(dia):
    """
    Verifica si el día ingresado está dentro del Enum Dias.

    Args:
        dia (str): Día de la semana a verificar.

    Raises:
        TypeError: Si el argumento no es un string.
        ValueError: Si el día no es válido.
    """
    try:
        if not isinstance(dia, str):
            raise TypeError("Se esperaba un valor de tipo string.")

        dia = dia.capitalize()

        if dia in [d.value for d in Dias]:
            print(f"Día válido: {dia}")
        else:
            raise ValueError("El día ingresado no es válido. Debe ser un día de la semana.")

    except TypeError as e:
        print(f"Error de tipo: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Ejecución finalizada.")


if __name__ == "__main__":
    # Pruebas de la función verificar_dia
    verificar_dia("Lunes")      # Día válido
    verificar_dia("domingo")    # Día válido
    verificar_dia("Feriado")    # Error: Día no válido
    verificar_dia(123)          # Error de tipo
