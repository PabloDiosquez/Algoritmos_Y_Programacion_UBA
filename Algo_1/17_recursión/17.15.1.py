# Escribir una función recursiva que reciba un número positivo n y devuelva la
# cantidad de dígitos que tiene.

def cantidad_dígitos(n: int):
    """
    Describe la cantidad de dígitos que tiene el número dado.
    Precondición:
        - El número dado debe ser >= 0.
    """
    if n <= 9: return 1 
    return 1 + cantidad_dígitos(n // 10)

# Ejemplo de uso:
numero = 12345
cantidad_de_digitos = cantidad_dígitos(numero)
print(f"El número {numero} tiene {cantidad_de_digitos} dígitos.")