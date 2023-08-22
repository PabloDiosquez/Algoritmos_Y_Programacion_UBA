# Escribir una función que reciba una lista desordenada y un elemento, que:
# a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
# tidad de coincidencias encontradas.
# b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
# c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
# por parámetro y devuelva una lista con las posiciones.

from helpers import es_vacía, uno_si_cero_sino

# a)
def apariciones(lista: list, elemento):
    """
    Describe la cantidad de apariciones del elemento dado en la lista dada.
 
    Parámetros:
        - lista (list): La lista en la que se realizará la búsqueda.
        - elemento: El elemento que se buscará en la lista.
    Retorna:
        - int: La cantidad de coincidencias encontradas.
    Ejemplos:
        >>> contar_coincidencias([1, 2, 3, 4, 2, 2], 2)
        3
        >>> contar_coincidencias(['a', 'b', 'c'], 'd')
        0
    """ 
    if es_vacía(lista): return 0
    primer_elemento = lista[0] 
    lista.remove(primer_elemento)
    return uno_si_cero_sino(primer_elemento == elemento) + apariciones(lista, elemento)

# b)
def posición_en_lista(lista: list, elemento) -> int:
    """
    Describe la primer posición del elemento dado en la lista dada.
    Parámetros:
        - lista (list): La lista en la que se realizará la búsqueda.
        - elemento: El elemento que se buscará en la lista.
    Retorna:
        - int: La posición del elemento en la lista.
    Precondición:
        - El elemento dado debe pertenecer a la lista dada.
    Ejemplos:
        >>> posición_en_lista([1, 2, 3, 4, 2, 2], 2)
        1
        >>> posición_en_lista(['a', 'b', 'c'], 'a')
        0
    """
    for índice, valor in enumerate(lista):
        if valor == elemento: return índice

# c)
def todas_las_posiciones(lista: list, elemento) -> list[int]:
    """
    Describe una lista con todas las posiciones en la lista dada de los elementos que coinciden con el elemento dado por parámetro. Si no hay coincidencias, describe la lista vacía.
    Parámetros:
        - lista (list): La lista en la que se realizará la búsqueda.
        - elemento: El elemento que se buscará en la lista.
    Retorna:
        - list[int]: Lista con las posiciones de los elementos coincidentes.
    Ejemplos:
        >>> todas_las_posiciones([1, 2, 3, 4, 2, 2], 2)
        [1,4,5]
        >>> todas_las_posiciones(['a', 'b', 'c'], 'a')
        [1]
    """
    posiciones = list()
    for índice, valor in enumerate(lista):
        if valor == elemento: 
            posiciones.append(índice)
    return posiciones