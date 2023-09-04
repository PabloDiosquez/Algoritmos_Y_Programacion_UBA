# Secuencia de Fibonacci 🐍

def fibo(n: int):  # T(n) ➡ O(c^n) -- E(n) ➡ O(n)
    """
    Describe el nésimo término de la secuencia de Fibonacci.
    """
    if n == 0 or n == 1:
        return 1 
    return fibo(n-1) + fibo(n-2)