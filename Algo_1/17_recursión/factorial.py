# La recurusión ocurre cuando algo está definido en términos de sí mismo o su tipo.

def factorial_iterativo(n: int):      # T(n)      E(n)
    """
    Precondición: n entero >= 0       # O(n)      O(1)
    Devuelve: n!
    """
    fact = 1
    for index in range(1, n+1):
        fact *= index
    return fact

def factorial_recursivo(n: int):      # O(n)      O(n)
    """
    Precondición: n entero >= 0
    Devuelve: n!
    """
    if n == 0: return 1               # Caso base 
    return factorial_recursivo(n-1)*n # Caso recursivo