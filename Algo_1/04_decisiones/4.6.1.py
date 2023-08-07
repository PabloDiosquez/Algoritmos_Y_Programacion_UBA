# Escribir dos funciones que resuelvan los siguientes problemas:
# a) Dado un número entero n, indicar si es par o no.
# b) Dado un número entero n, indicar si es primo o no.

from helpers import get_int
# a)
def es_par(n: int) -> bool:
    """Indica si el número dado es par.
    """
    return not n % 2

def es_impar(n: int) -> bool:
    """Indica si el número dado es impar.
    """
    return n % 2 

def paridad():
    if es_par(get_int("Ingrese un número: ")):
        print("Es par.")
    else:
        print("Es impar.")
    
# b) 
def es_primo(n: int) -> bool: 
    """Indica si el número dado es primo.
    """
    return n > 1 and not _tiene_divisores_propios(n)

def _tiene_divisores_propios(n: int) -> bool:
    """Indica si el número dado tiene divisores propios.
    """
    for i in range(2, n//2 + 1):
        if not n % i: return True
    return False