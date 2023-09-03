# Escribir una funcion recursiva que encuentre el mayor elemento de una lista.

def máximo(lista: list):
    """
    Describe el mayor elemento de la lista dada.
    Pre:
        - La lista dada no debe ser vacía.
    """
    primer_elemento = lista[0]
    resto           = lista[1:]
    return máximo_entre(primer_elemento, resto)


def máximo(lista: list):
    """
    Describe el mayor elemento de la lista dada.
    Pre:
        - La lista dada no debe ser vacía.
    """
    return máximo_hasta(lista, len(lista))

def máximo_hasta(lista: list, hasta: int):
    """
    Describe el mayor elemento de la lista dada hasta el índice 'hasta' - 1.
    Pre:
        - La lista dada no debe ser vacía.
        - Debe ser 0 <= 'hasta' <= len(lista) 
    """
    if hasta == 1: return lista[0]
    return máximo_entre(lista[hasta-1], máximo_hasta(lista, hasta-1))


# Funciones auxiliares 🐱‍🏍 

def máximo_entre(num1: int, num2: int):
    """
    Describe el máximo entre los dos números dados.
    """
    if num1 >= num2: return num1 
    return num2