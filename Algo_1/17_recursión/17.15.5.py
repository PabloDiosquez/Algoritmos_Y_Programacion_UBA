# Escribir dos funciones mutualmente recursivas par(n) e impar(n) que de-
# terminen la paridad del numero natural dado, conociendo solo que:

# • 1 es impar.
# • Si un número es impar, su antecesor es par; y viceversa.

def par(n: int):
    """
    """
    if n == 1: return False
    return impar(n-1)

def impar(n: int):
    """
    """
    if n == 1: return True 
    return par(n-1)

# Casos de prueba:
assert     par(2)
assert     impar(11)
assert     par(22)
assert     impar(21)
assert not impar(2)
assert not par(15)
assert not impar(14)