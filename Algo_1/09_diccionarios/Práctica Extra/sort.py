# En este ejemplo se define una función que define como acceder al campo por el que se va a ordenar

estudiantes = [
{"Nombre": "Juan","Edad": 19, "DNI": 45041659},
{"Nombre": "Pablo","Edad": 17,"DNI": 46058692},
{"Nombre": "Ana","Edad": 20,"DNI": 44058692},
{"Nombre": "Maria","Edad": 22,"DNI": 41058692},
{"Nombre": "Eva","Edad": 15,"DNI": 48058692},
 ]

def obtener_campo_para_ordenar(d):
    return d["Edad"]
estudiantes.sort(key=obtener_campo_para_ordenar)
print(estudiantes)
# En este ejemplo se utilizan funciones anónimas (lambda) es lo mismo que el de arriba pero la función no tiene nombre.

estudiantes = [
{"Nombre": "Juan","Edad": 19, "DNI": 45041659},
{"Nombre": "Pablo","Edad": 17,"DNI": 46058692},
{"Nombre": "Ana","Edad": 20,"DNI": 44058692},
{"Nombre": "Maria","Edad": 22,"DNI": 41058692},
{"Nombre": "Eva","Edad": 15,"DNI": 48058692},
 ]
estudiantes.sort(key=lambda e: e["Edad"])
print(estudiantes)