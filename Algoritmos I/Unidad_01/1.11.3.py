from helpers import get_int, ejercicio

def producto(num1, num2):
    """Recibe dos números y describe su producto.
    """
    return num1*num2

def producto():
    """Lee dos números por consola y luego describe el producto entre ambos.
    """
    num1 = get_int("Número 1: ")
    num2 = get_int("Número 2: ")
    return num1*num2

ejercicio("1.11.3 - Producto de dos números:", producto())