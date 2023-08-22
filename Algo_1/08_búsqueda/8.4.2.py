# Escribir una función que reciba una lista de números no ordenada, que:
# a) Devuelva el valor máximo.
# b) Devuelva una tupla que incluya el valor máximo y su posición.
# c) ¿Qué sucede si los elementos son cadenas de caracteres?
# Nota: no utilizar lista.sort()

from helpers import máximo_entre

# a)
def máximo(lista: list):
    """
    Describe el máximo de la lista dada.
    Parámetros:
        - lista (list[int]): Lista en la que se realizará la búsqueda.
    Precondición:
        - La lista dada no debe ser vacía.
    """
    if len(lista) == 1: return lista[0]
    nueva_lista = lista[:]
    primer_elemento = nueva_lista[0]
    nueva_lista.remove(primer_elemento)
    return máximo_entre(primer_elemento, máximo(nueva_lista))
    
# b)
def máximo_y_posición(lista: list):
    """
    Describe el máximo y la posición del mismo en la lista dada.
    Parámetros:
        - lista (list[int]): Lista en la que se realizará la búsqueda.
    Precondición:
        - La lista dada no debe ser vacía.
    """
    return máximo_desde(lista, 0) 

def máximo_desde(lista: list, desde: int):
    """
    Describe el máximo y la posición del mismo en la lista dada desde 'desde'.
    Parámetros:
        - lista (list[int]): Lista en la que se realizará la búsqueda.
    Precondición:
        - La lista dada no debe ser vacía.
        - Debe tener al menos 'desde' elementos.
        - Debe ser 0 <= 'desde' <= len(lista). 
    """
    máximo_hasta_ahora = lista[desde]
    posición_máximo    = desde
    for índice, valor in enumerate(lista, desde):
        if valor >= máximo_hasta_ahora:
            máximo_hasta_ahora = valor 
            posición_máximo    = índice + 1
    return máximo_hasta_ahora, posición_máximo 

# c) 
def pruebas():
    assert máximo_y_posición(['a', 'h', 't', 'd']) == ('t', 3) 
    assert máximo_y_posición(['a', 'h', 'f', 'd']) == ('h', 2) 
    assert máximo_y_posición(['z', 'h', 't', 'd']) == ('z', 1) 

pruebas()