"""
# PRACTICA DICCIONARIOS
# 1. Crear un diccionario con los nombres de los alumnos y sus notas.   
# 2. Imprimir el nombre del alumno con la mejor nota.
#     tarea("tarea2"),
#         tarea("tarea3"),
#     )
#     )
# 3. Imprimir el nombre del alumno con la peor nota.
# 4. Imprimir el nombre del alumno con la nota más alta.
# 5. Imprimir el nombre del alumno con la nota más baja.
# 6. Imprimir el nombre del alumno con la nota más alta y la más baja.
Dic={'x':'equis', 'y':'ye', 'D':'De'}
Dic2=dict(x='equis', y="ye", D="De")
print(Dic['x'])
#print(Dic['z'])   #truena
print(Dic.get('x'))
print(Dic.get('z'))
Dic['x']="equisD"
Dic['z']="Zeta" 
print(Dic['x'])
print(Dic['z'])
#del Dic['y'] #>????????

x=Dic.pop('y')
print(x)

llaves=Dic.keys()
print(llaves)
valores=Dic.values()
print(valores)
p=Dic.items()
print("--------------------------------")
print(p)

Dic.clear()
Dic.update() #agregar elementos que quiera
Dic.get('x',"xd")
"""