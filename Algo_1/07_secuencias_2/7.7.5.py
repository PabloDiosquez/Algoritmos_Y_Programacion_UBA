# Dada una lista de números enteros, escribir una función que:
# a) Devuelva una lista con todos los que sean primos.

from helpers import es_primo, es_vacía, factorial, singular_si

def lista_de_primos(números: list[int]) -> list[int]:
    """ Devuelve una lista con todos los números primos de una lista dada.
        Parámetros:
        - lista (list): La lista de números enteros a evaluar.
        Retorna:
        - Una lista con los números primos de la lista dada.
    """
    primos = list()
    for número in números:
        if es_primo(número): primos.append(número)
    return primos

def lista_de_primos(números: list[int]) -> list[int]:
    """ Devuelve una lista con todos los números primos de una lista dada.
        Parámetros:
        - lista (list): La lista de números enteros a evaluar.
        Retorna:
        - Una lista con los números primos de la lista dada.
    """
    if es_vacía(números): return list() 
    primer_elemento = números[0]
    números.remove(primer_elemento)
    return singular_si(primer_elemento, es_primo(primer_elemento)) + lista_de_primos(números)
    
# b) Devuelva la sumatoria y el promedio de los valores.

def sumatoria(números: list[int]) -> int:
    """ Describe la sumatoria de los números de la lista de enteros dada.
        Parámetros:
            - lista (list): La lista de números enteros a evaluar.
        Retorna:
            - La sumatoria de los números enteros dados.
    """
    if es_vacía(números): return 0
    primer_elemento = números[0]
    números.remove(primer_elemento)
    return primer_elemento + sumatoria(números)  

def promedio(números: list[int]) -> int:
    """ Describe el promedio de los números de la lista de enteros dada.
        Precondición:
            La lista dada no debe ser vacía.
    """
    return sumatoria(números) // len(números)

# c) Devuelva una lista con el factorial de cada uno de esos números.

def lista_de_factoriales(números: list[int]) -> int:
    """ Recibe una lista de números y describe una lista con el factorial de cada uno de   ellos.
    Parámetros:
        - lista (list): La lista de números enteros a evaluar.
        Retorna:
        - Una lista con los factoriales de los números de la lista dada.
    """
    factoriales = list()
    for número in números:
        factoriales.append(factorial(número))
    return factoriales