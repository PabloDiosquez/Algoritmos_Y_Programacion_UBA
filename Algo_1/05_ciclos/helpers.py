def es_primo(n):
    """
    Indica si el número 'n' es primo.
    Pre:
        - 'n' debe ser >= 0
    """
    d = 2
    while n % d and d <= n // 2:
        d += 1
    return n > 1 and d > n // 2 

def divisores(n: int):
    """
    Describe una lista con los divisores del número dado.
    Pre:
        - El número dado debe ser > 0.
    """
    divisores = []
    for d in range(1,n+1):
        if not n % d: divisores.append(d)
    return divisores