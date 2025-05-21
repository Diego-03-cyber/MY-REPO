# ==================================
# Ejemplo 1: Concurrencia con hilos (threading)
# ==================================

import threading
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Hilo(threading.Thread):
    """
    Clase que representa un hilo personalizado que imprime mensajes con retardo.
    """

    def __init__(self, nombre, intervalo, color):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo
        self.color = color

    def run(self):
        print(f"{self.color}El hilo {self.nombre} ha comenzado")
        for i in range(5):
            print(f"{self.color}El hilo {self.nombre} está en iteración {i + 1}")
            time.sleep(self.intervalo)
        print(f"{self.color}El hilo {self.nombre} ha finalizado")


# Crear e iniciar hilos
hilo1 = Hilo("hilo1", 2, Fore.BLUE)
hilo2 = Hilo("hilo2", 4, Fore.MAGENTA)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()


# ==================================
# Ejemplo 2: Concurrencia con async/await (asyncio)
# ==================================

import asyncio

async def tarea(nombre):
    """
    Función asincrónica que simula una tarea concurrente.
    """
    print(f"{nombre} inicia")
    await asyncio.sleep(2)
    print(f"{nombre} termina")

async def main():
    """
    Ejecuta múltiples tareas asincrónicas en paralelo.
    """
    await asyncio.gather(
        tarea("tarea1"),
        tarea("tarea2")
    )

# Ejecutar corrutinas
asyncio.run(main())
