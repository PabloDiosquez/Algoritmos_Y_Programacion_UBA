# Escribir una función recursiva que simule el siguiente experimento: Se tiene
# una rata en una jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 minutos
# vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. La rata no aprende,
# siempre elige entre los 3 caminos con la misma probabilidad, pero quiere su libertad, por lo que
# recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula.

from random import randint

def tiempo_hasta_salir_de_la_jaula():
    """
    Describe el tiempo (en minutos) que tarda una rata en escapar de la jaula en el siguiente experimento:
    - Una rata atrapada en una jaula elige entre 3 caminos al azar (cada uno con la misma probabilidad).
    - La rata quiere su libertad, por lo que recorrerá los 3 caminos hasta salir de la jaula.
    - Si elige el número 1, luego de 3 minutos vuelve a la jaula.
    - Si elige el número 2, luego de 5 minutos vuelve a la jaula.
    - Si elige el número 3, luego de 7 minutos sale de la jaula.
    - La rata no aprende, por lo que siempre elige cualquiera de los 3 caminos con la misma probabilidad.
    """
    camino = randint(1,3)
    print(f"La rata eligió el camino {camino}")
    if camino == 1:
        "La rata eligió el camino 1, luego de 3 minutos vuelve a la jaula"
        return 3 + tiempo_hasta_salir_de_la_jaula()
    elif camino == 2:
        "La rata eligió el camino 2, luego de 5 minutos vuelve a la jaula"
        return 5 + tiempo_hasta_salir_de_la_jaula()
    "La rata eligió el camino 3, luego de 7 minutos escapa de la jaula"
    return 7 

print(tiempo_hasta_salir_de_la_jaula())