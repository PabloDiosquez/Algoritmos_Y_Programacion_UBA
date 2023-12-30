# Escribir una función recursiva que reciba un número positivo n y devuelva la
# cantidad de dígitos que tiene.

# v1
def cantidad_dígitos(n: int):
    """
    Describe la cantidad de dígitos que tiene el número dado.
    Precondición:
        - El número dado debe ser >= 0.
    """
    if n <= 9: return 1 
    return 1 + cantidad_dígitos(n // 10)

# v2
def cantidad_digitos(n: int) -> int:
    """
    Calcula la cantidad de dígitos en un número entero dado.

    Parámetros:
    - n (int): El número del cual se calculará la cantidad de dígitos.

    Retorna:
    int: La cantidad de dígitos en el número dado.

    Ejemplo:
    >>> cantidad_digitos(123)
    3
    """
    if not n:
        # Si el número es 0, no tiene dígitos.
        return 0

    # Si el número no es 0, se llama recursivamente a la función
    # dividiendo el número por 10 en cada llamada hasta que el número sea 0.
    # Se suma 1 en cada llamada para contar el dígito actual.
    return 1 + cantidad_digitos(n // 10)

# Ejemplo de uso:
numero = 12345
cantidad_de_digitos = cantidad_dígitos(numero)
print(f"El número {numero} tiene {cantidad_de_digitos} dígitos.")