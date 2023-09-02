# Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n
# es potencia de b.
# Ejemplos:
# es_potencia(8, 2) -> True
# es_potencia(64, 4) -> True
# es_potencia(70, 10) -> False

def es_potencia(n: int, b: int):
    """
    Indica si 'n' es potencia de 'b'.
    Precondición:
        - Los números dados deben ser >= 0.
    """
    if n == 1: return True
    return es_divisible(n, b) and es_potencia(n // b, b)

# Casos de prueba 
assert     es_potencia(8, 2)
assert     es_potencia(64, 4)
assert not es_potencia(4, 10)

# Fuciones auxiliares 🐱‍🏍 

def es_divisible(n: int, b: int):
    """
    Indica si el primer número dado es divisible por el segundo número dado.
    """
    return not n % b 