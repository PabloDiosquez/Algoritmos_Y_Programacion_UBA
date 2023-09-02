# La recurusión ocurre cuando algo está definido en términos de sí mismo o su tipo.

def factorial(n: int):
    """
    Precondición: n entero >= 0
    Devuelve: n!
    """
    if n == 0: return 1
    return factorial(n-1)*n