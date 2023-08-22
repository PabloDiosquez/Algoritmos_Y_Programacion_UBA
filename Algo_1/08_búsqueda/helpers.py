def es_vacía(lista: list) -> bool:
    """
    Indica si la lista dada es vacía.
    Parámetros:
        - lista (list): La lista según la cual se describe True o False.
    """
    return len(lista) == 0

def uno_si_cero_sino(condición: bool) -> int:
    """
    Describe 1 si se cumple la condición dada. En caso contrario, describe 0.
    Parámetros:
        - condición (bool): Condición según la cual se describe 1 o 0.
    """
    if condición: return 1
    return 0

def máximo_entre(elemento1, elemento2):
    """
    Describe el máximo entre los dos elementos dados.
    Parámetros:
        - elemento1: Uno de los elementos a comparar.
        - elemento2: Uno de los elementos a comparar.
    Precondiciones:
        - Los elementos dados deben ser comparables entre sí a través del operador '>'.
    """
    if elemento1 > elemento2: return elemento1
    return elemento2