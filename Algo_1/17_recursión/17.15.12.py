# Ya sabemos que la implementación recursiva del cálculo del número de Fi-
# bonacci (Fn = Fn−1 + Fn−2, F0 = 0, F1 = 1) es ineficiente porque muchas de las ramas calculan reiteradamente los mismos valores.
# Escribir una función _fibonacci(n) que calcule el enésimo número de Fibonacci de forma recursiva pero que utilice un diccionario para almacenar los valores ya computados y no computarlos más de una vez.

# Nota: Será necesario implementar una función wrapper para cumplir con la firma de la fun-
# ción pedida.

def fib(n: int):
    """
    Describe el nésimo término de la secuencia de Fibonacci.
    """
    return _fib(n, {})

# Wrapper 🌮
def _fib(n: int, resultados: dict):
    if n in resultados:
        return resultados[n]
    else:
        if n <= 1: return 1 
        resultados[n] = _fib(n-1, resultados) + _fib(n-2, resultados)
    return resultados[n]

print(fib(900))