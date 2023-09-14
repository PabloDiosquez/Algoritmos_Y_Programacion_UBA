# 6.
def elementos_distintos(elementos: list) -> int:
    """
    Describe la cantidad de elementos distintos en la lista dada.
    Parámetros:
        - elementos (list): Una lista de elementos que se desea analizar.
    Retorna:
        - La cantidad de elementos distintos en la lista.
    Raises:
    TypeError: Si la entrada no es una lista.
    Ejemplo:
    >>> elementos = [1, 2, 2, 3, 4, 4, 5]
    >>> elementos_distintos(elementos)
    5
    Observaciones:
        - Esta función utiliza un enfoque eficiente para calcular la cantidad de elementos distintos en una lista.
          Convierte la lista en un conjunto (set) para eliminar duplicados y luego retorna la longitud del conjunto resultante.
          Esto significa que no se conserva el orden original de los elementos en la lista.
    """
    if not isinstance(elementos, list):
        raise TypeError("El argumento 'elementos' debe ser una lista.")
    return len(set(elementos))

def elementos_distintos(elementos: list) -> int:
    """
    Describe la cantidad de elementos distintos en la lista dada.
    Parámetros:
        - elementos (list): Una lista de elementos.
    Retorna:
        - La cantidad de elementos distintos en la lista.
    Ejemplo:
    >>> elementos = [1, 2, 2, 3, 4, 4, 5]
    >>> elementos_distintos(elementos)
    5
    """
    distintos = []
    for elemento in elementos:
        if elemento not in distintos:
            distintos.append(elemento)
    return len(distintos)