# Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n
# es potencia de b.
# Ejemplos:
# es_potencia(8, 2) -> True
# es_potencia(64, 4) -> True
# es_potencia(70, 10) -> False

def es_potencia(n: int, b: int):
    """
    Indica si 'n' es potencia de 'b'.
    """
    if n == 1: return True
    return n % b == 0 and es_potencia(n // b, b)

# Casos de prueba 
assert es_potencia(8, 2)
assert es_potencia(64, 4)
assert not es_potencia(70, 10)