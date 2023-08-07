# Escribir una implementación propia de la función abs, que devuelva el valor
# absoluto de cualquier valor que reciba.

from helpers import get_int

def valor_absoluto(n: int) -> int:
    """Describe el valor absoluto del número dado.
    """
    if n >= 0: return n 
    return -n 