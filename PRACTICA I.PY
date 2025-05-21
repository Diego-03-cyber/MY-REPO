import math

class Figura:
    """
    Clase que contiene métodos para calcular el área y el perímetro
    de figuras geométricas regulares: cuadrado, triángulo equilátero y pentágono regular.
    """

    @staticmethod
    def cuadrado(lado):
        """
        Calcula el área y perímetro de un cuadrado.
        """
        if lado < 6:
            return "El lado debe ser mayor a 6"
        area = lado ** 2
        perimetro = 4 * lado
        return f"El área del cuadrado es: {area} y su perímetro es: {perimetro}"

    @staticmethod
    def triangulo_equilatero(lado):
        """
        Calcula el área y perímetro de un triángulo equilátero.
        """
        if lado < 6:
            return "El lado debe ser mayor o igual a 6"
        area = (math.sqrt(3) / 4) * lado ** 2
        perimetro = 3 * lado
        return f"El área del triángulo es: {area:.2f} y su perímetro es: {perimetro}"

    @staticmethod
    def pentagono_regular(lado):
        """
        Calcula el área y perímetro de un pentágono regular.
        """
        if lado < 6:
            return "El lado debe ser mayor o igual a 6"
        apotema = lado / (2 * math.tan(math.pi / 5))
        area = (5 * lado * apotema) / 2
        perimetro = 5 * lado
        return f"El área del pentágono es: {area:.2f} y su perímetro es: {perimetro}"


def main():
    """
    Función principal para pedir al usuario el lado y mostrar los resultados.
    """
    try:
        lado = float(input("Ingrese el lado de la figura: "))
        if lado >= 6:
            print(Figura.cuadrado(lado))
            print(Figura.triangulo_equilatero(lado))
            print(Figura.pentagono_regular(lado))
        else:
            print("El lado debe ser mayor o igual a 6.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
