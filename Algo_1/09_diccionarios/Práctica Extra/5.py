# 5.

def promedio_de_notas_en_intento(estudiantes: list[dict], intento):
    """
    Describe el promedio de notas de los estudiantes en el intento 'intento' de rendir un parcial.
    Parámetros:
        - estudiantes (list[dict]): Lista de los estudiantes guardada por el profesor. Cada alumno será un diccionario que debe tener las claves 'Nombre', 'Apellido', 'Intento' y 'Nota'.
        - intento (int): El intento del parcial para el cual se calculará el promedio. 
    Retorna:
        - El promedio de las notas de los estudiantes en el intento 'intento'. 
    """
    if not estudiantes: raise ValueError("Lista de estudiantes vacía")
    total_notas          = 0
    cantidad_estudiantes = 0
    for estudiante in estudiantes:
        if estudiante['Intento'] == intento:
            total_notas += estudiante['Nota']
            cantidad_estudiantes += 1
    if not cantidad_estudiantes:
        raise ZeroDivisionError(f"No hay estudiantes que hayan rendido en el intento {intento}")
    return total_notas / cantidad_estudiantes

# Ejemplo de uso:
lista_notas = [
            {'Nombre': 'Juan', 'Apellido': 'Pérez', 'Intento': 1, 'Nota': 85},
            {'Nombre': 'María', 'Apellido': 'Gómez', 'Intento': 1, 'Nota': 92},
            {'Nombre': 'Pedro', 'Apellido': 'López', 'Intento': 2, 'Nota': 78},
            {'Nombre': 'Ana', 'Apellido': 'Rodríguez', 'Intento': 2, 'Nota': 88},]

# Calcular el promedio de las notas en el intento 1
promedio_intent_1 = promedio_de_notas_en_intento(lista_notas, 1)
print(f"Promedio en el intento 1: {promedio_intent_1}")