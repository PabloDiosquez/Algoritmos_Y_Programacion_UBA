# La recurusión ocurre cuando algo está definido en términos de sí mismo o su tipo.

def factorial_iterativo(n: int):
    """
    Precondición: n entero >= 0
    Devuelve: n!
    """
    fact = 1
    for index in range(1, n+1):
        fact *= index
    return fact

def factorial_recursivo(n: int):
    """
    Precondición: n entero >= 0
    Devuelve: n!
    """
    if n == 0: return 1
    return factorial_recursivo(n-1)*n