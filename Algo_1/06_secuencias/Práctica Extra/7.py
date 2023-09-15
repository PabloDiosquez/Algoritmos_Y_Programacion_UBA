# 7.
def pares(números: list):
    """
    Esta función toma una lista de números y describe una lista con solo los números pares.
    Parámetros:
        - números (list): Una lista de números que se deben examinar.
    Retorna:
        - Una lista de números pares.
    """
    pares = []  # Inicializamos una lista vacía para almacenar los números pares.
    for número in números:
        if es_par(número):
            pares.append(número) # Si es par, lo agregamos a la lista de números pares.
    return pares # Devolvemos la lista de números pares.

def es_par(número: int):
    "Indica si el número dado es par"
    return not número % 2