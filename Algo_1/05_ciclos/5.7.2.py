# Escribir una función que reciba un número entero k e imprima su descomposi-
# ción en factores primos.

from helpers import divisores, es_primo

def factorización(número: int):
    """
    Devuelve una cadena de caracteres que representa la factorización en primos del número dado.
    Parámetros:
        número (int): El número entero positivo que se va a factorizar.
    Retorna:
        str: Una cadena de caracteres que muestra la factorización en primos del número. 
    Observación:
        ValueError: Se lanza si el número no es un entero positivo.
    """
    if número <= 0:
        raise ValueError("El número debe ser un entero positivo.")
    factorización = []
    for primo, exponente in _factorización(número):
        factorización.append(f"{primo}^{exponente}")
    return '*'.join(factorización)

def _factorización(número: int):
    """
    Describe una lista de tuplas formadas por los divisores primos con sus respectivos exponenetes en la factorización de 'número'.
    Pre:
        - Debe ser 'número' > 0.
    """
    divisores_y_exponentes = []
    for primo in divisores_primos(número):
        divisores_y_exponentes.append((primo, exponente_en_fact(número, primo)))
    return divisores_y_exponentes

def divisores_primos(número: int):
    """
    Describe una lista de los divisores primos del número dado.
    Pre:
        - El número dado debe ser > 0.
    """
    # return primos(divisores(número))
    return list(filter(es_primo, divisores(número)))

def exponente_en_fact(número: int, divisor: int):
    """
    Describe el exponente de 'divisor' en la factorización de 'número'.
    En caso de que la división no sea entera, describe 0.
    Pre:
        - Deben ser 'número' y 'divisor' > 0.
    """
    exponente = 0
    while número > 0 and not número % divisor:
        exponente += 1
        número     = número // divisor
    return exponente

# Ejemplos de uso
número = 120
print(f"Factorización en primos de {número}: {factorización(número)}")

# Función auxiliar -- No utilizada 🤔

# def primos(números: list):
#     """
#     Describe una lista con los números primos de la lista de números dada.
#     """
#     primos = []
#     for número in números:
#         if es_primo(número):
#             primos.append(número)
#     return primos