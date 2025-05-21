# 🐍 Prácticas de Programación en Python

Este repositorio contiene una colección de prácticas orientadas al aprendizaje de conceptos fundamentales y avanzados de Python, incluyendo Programación Orientada a Objetos, concurrencia, estructuras de datos y desarrollo web con Flask.

---

## 📚 Contenido

### 🔐 Programación Orientada a Objetos (POO)

- **Encapsulamiento:** Uso de atributos y métodos privados.
- **Herencia:** Clases hijas (`Pikachu`, `Charmander`) que heredan de `Pokemon`.
- **Polimorfismo:** Clases `Gato` y `Perro` implementan el mismo método `sonido`.
- **Abstracción:** Clases abstractas como `Figura` y sus subclases `Cuadrado` y `Círculo`.

📄 Archivo relacionado: `poo_practicas.py`

---

### 📆 Enumeraciones (`Enum`)

- Uso del módulo `enum` para representar días de la semana.
- Validación robusta del input del usuario usando `try-except`.

📄 Archivo relacionado: `enum_dias.py`

---

### 📊 Arreglos y Listas

- Uso de `NumPy` para manipular arreglos (insertar, eliminar, modificar).
- Uso de listas nativas de Python con operaciones básicas.

📄 Archivo relacionado: `estructuras_datos.py`

---

### ⚙️ Concurrencia

#### Hilos (`threading`)
- Simulación de tareas con distintos intervalos y colores usando `colorama`.

#### Corrutinas (`asyncio`)
- Uso de `async` y `await` para ejecutar tareas concurrentes de forma asíncrona.

📄 Archivo relacionado: `concurrencia.py`

---

### 🌐 Aplicaciones con Flask

#### 1. **App básica**
- Ruta `/` que devuelve `'nopuedomas'`.

#### 2. **App con restricción por IP**
- Solo permite el acceso a una IP específica (ej. `192.168.1.100`).

#### 3. **App interfaz personalizada**
- Ruta `/` que responde `'Holiwis'`.

📁 Archivos relacionados:
- `app_basic.py`
- `app_ip_restrict.py`
- `app_interface.py`


