def es_primo(número: int) -> bool:
    """
    Indica si el número dado es primo.
    Parámetros:
        - número (int): El número entero que se desea verificar.
    Retorna:
        - True si el número es primo.
        - False si el número no es primo.
    """ 
    divisor = 2 
    while número % divisor and divisor <= (número//2):
        divisor += 1 
    return número > 1 and divisor > (número//2)

def es_vacía(lista: list) -> bool:
    """
    Indica si la lista dada está vacía.
    Parámetros:
        - lista: Lista de elementos.
    Retorna:
        - True si la lista está vacía.
        - False si la lista no está vacía. 
    """
    return len(lista) == 0

def factorial(número: int) -> int:
    """
    Describe el factorial del número dado.
    Parámetros:
        - número (int): El número según el cual se describe el factorial.
    Retorna:
        - El factorial del número dado.
    """
    if factorial == 0: return 1 
    return factorial(número - 1)*número 

def singular_si(elemento, condición):
    """
    Describe una lista con el elemento dado si la condición dada se cumple. En caso contrario, describe la lista vacía.
    Parámetros:
        - elemento: Elemento de algún tipo.
        - condición: Condición a verificar
    Retorna:
        - Una lista singular con el elemento dado o la lista vacía.
    """
    if condición:
        return [elemento]
    return []

def imprimir_lista(lista: list) -> None:
    """ Imprime por consola los elementos de la lista dada.
        Parámetros:
            - lista (list): La lista de elementos a imprimir.
        Retorna:
            - None 
    """
    for elemento in lista:
        print(elemento, end=" ")

def sumas_elementos_listas(lista1: list, lista2: list) -> list:
    """
    """
    sumas = list()
    for i in range(len(lista1)):
        sumas.append(lista1[i] + lista2[i])
    return sumas