import numpy as np

# ==================================
# Clase para operaciones con arreglos de NumPy
# ==================================

class Arreglos:
    """
    Clase que encapsula operaciones básicas sobre un arreglo NumPy:
    insertar, eliminar y modificar elementos.
    """

    def __init__(self, arreglo):
        self.arreglo = np.array(arreglo)
        print("Arreglo inicial:", self.arreglo)

    def insertar(self, indice, elemento):
        """
        Inserta un elemento en el índice especificado.
        """
        self.arreglo = np.insert(self.arreglo, indice, elemento)
        print(f"Después de insertar {elemento} en el índice {indice}:", self.arreglo)

    def eliminar(self, indice):
        """
        Elimina el elemento del índice especificado.
        """
        self.arreglo = np.delete(self.arreglo, indice)
        print(f"Después de eliminar el elemento en el índice {indice}:", self.arreglo)

    def modificar(self, indice, nuevo_elemento):
        """
        Modifica el valor del elemento en el índice dado.
        """
        self.arreglo[indice] = nuevo_elemento
        print(f"Después de modificar el índice {indice} a {nuevo_elemento}:", self.arreglo)


# ==================================
# Clase para operaciones con listas de Python
# ==================================

class Listas:
    """
    Clase que encapsula operaciones básicas sobre listas de Python:
    insertar, eliminar y modificar elementos.
    """

    def __init__(self, lista):
        self.lista = lista
        print("Lista inicial:", self.lista)

    def insertar(self, elemento):
        """
        Inserta un elemento al final de la lista.
        """
        self.lista.append(elemento)
        print(f"Después de insertar {elemento}:", self.lista)

    def eliminar(self, indice):
        """
        Elimina el elemento del índice especificado.
        """
        self.lista.pop(indice)
        print(f"Después de eliminar el elemento en el índice {indice}:", self.lista)

    def modificar(self, indice, nuevo_elemento):
        """
        Modifica el valor del elemento en el índice dado.
        """
        self.lista[indice] = nuevo_elemento
        print(f"Después de modificar el índice {indice} a {nuevo_elemento}:", self.lista)


# ==================================
# Pruebas de uso
# ==================================

if __name__ == "__main__":
    print("=== Probando la clase Arreglos ===")
    arr = Arreglos([1, 2, 3, 4])
    arr.insertar(2, 99)
    arr.eliminar(3)
    arr.modificar(1, 88)

    print("\n=== Probando la clase Listas ===")
    lst = Listas([1, 2, 3, 4])
    lst.insertar(99)
    lst.eliminar(2)
    lst.modificar(1, 88)
