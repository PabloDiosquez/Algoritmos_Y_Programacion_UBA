# Escribir una función recursiva para replicar los elementos de una lista una
# cantidad n de veces. Por ejemplo:
# replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])

from helpers import es_vacía, lista_vacía

def replicar(lista: list, cantidad: int):
    """
    Describe una lista con los elementos de la lista dada replicados 'cantidad' de veces.
    Parámetros:
        - lista (list):   Lista de elementos a replicar.  
        - cantidad (int): Cantidad de veces que se van a replicar los elementos de la lista dada.
    Retorna:
        - Una lista con los elementos de la lista dada replicados 'cantidad' de veces.{
    Ejemplo de uso:
        >>> replicar([1, 3, 3, 7], 2)
        [1, 1, 3, 3, 3, 3, 7, 7] 
    """
    if es_vacía(lista) or cantidad == 0: return lista_vacía()
    primer_elemento = lista[0]
    resto           = lista[1:]
    return [primer_elemento]*cantidad + replicar(resto, cantidad)