"""
Demostración de los pilares de la Programación Orientada a Objetos (POO) en Python:
- Encapsulamiento
- Herencia
- Polimorfismo
- Abstracción
"""

# ==================================
# Encapsulamiento
# ==================================

class Cliente:
    """
    Clase que representa a un cliente con atributos y métodos encapsulados.
    """
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print('Cuenta de procesamiento')

    def get_codigo(self):
        """
        Método getter para acceder al código privado.
        """
        return self.__codigo


persona = Cliente()
# Acceso a atributos y métodos privados usando name mangling (no recomendado fuera de pruebas o debugging)
print(persona._Cliente__codigo)
persona._Cliente__cuenta()


# ==================================
# Herencia
# ==================================

class Pokemon:
    """
    Clase base para representar un Pokémon.
    """
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return f'{self.nombre} es un Pokémon de tipo: {self.tipo}'


class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return f'{self.nombre} usa ataque: {tipo_ataque}'


class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return f'{self.nombre} usa ataque: {tipo_ataque}'


nuevo_pokemon = Pikachu('Boby', 'eléctrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Impactrueno'))


# ==================================
# Polimorfismo
# ==================================

class Animal:
    """
    Clase base abstracta para representar un animal.
    """
    def sonido(self):
        raise NotImplementedError("La subclase debe implementar este método")


class Perro(Animal):
    def sonido(self):
        return "Guau"


class Gato(Animal):
    def sonido(self):
        return "Miau"


def hacer_sonido(animal):
    """
    Función que ejecuta el sonido de cualquier animal.
    """
    print(animal.sonido())


perro = Perro()
gato = Gato()

hacer_sonido(perro)
hacer_sonido(gato)


# ==================================
# Abstracción
# ==================================

from abc import ABC, abstractmethod

class Figura(ABC):
    """
    Clase abstracta para figuras geométricas.
    """
    @abstractmethod
    def area(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio ** 2


cuadrado = Cuadrado(4)
circulo = Circulo(3)

print(f"Área del cuadrado: {cuadrado.area()}")
print(f"Área del círculo: {circulo.area()}")
