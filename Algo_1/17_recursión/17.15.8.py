# Escribir una funcion recursiva que encuentre el mayor elemento de una lista.

# 1.
def máximo(lista: list):
    """
    Describe el mayor elemento de la lista dada.
    Pre:
        - La lista dada no debe ser vacía.
    """
    primer_elemento = lista[0]
    resto           = lista[1:]
    return máximo_entre(primer_elemento, resto)


# 2.
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

# 3.
def mayor_en_lista_div_conq(numeros: list[int]) -> int:
    """
    Encuentra recursivamente el mayor elemento de una lista utilizando división y conquista.

    Parámetros:
    - números (list[int]): La lista de números enteros.

    Precondición:
    - La lista dada no debe ser vacía.

    Postcondición:
    - Devuelve el mayor elemento de la lista.

    Ejemplo:
    >>> mayor_en_lista_div_conq([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    9
    """
    if len(numeros) == 1:
        # Caso base: Si la lista tiene un solo elemento, ese es el mayor.
        return numeros[0]
    middle = len(numeros) // 2
    # Divide la lista en dos mitades y encuentra el mayor en cada mitad.
    mayor_izq = mayor_en_lista_div_conq(numeros[:middle])
    mayor_der = mayor_en_lista_div_conq(numeros[middle:])
    # Compara los mayores de las dos mitades.
    return max(mayor_izq, mayor_der)

# Funciones auxiliares 🐱‍🏍 

def máximo_entre(num1: int, num2: int):
    """
    Describe el máximo entre los dos números dados.
    """
    if num1 >= num2: return num1 
    return num2