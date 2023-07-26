from helpers import get_int, ejercicio

def _factorial(num):
    """Describe el factorial del número dado.
    """
    factorial = 1
    for i in range(2,num+1):
        factorial *= i
    return factorial

def factorial():
    """Describe el factorial del número leído por consola.
    """
    return _factorial(get_int("Número: "))

ejercicio("1.11.7 - Factorial:", factorial())