# Escribir una función recursiva que calcule recursivamente el n-ésimo número
# triangular (el número 1 + 2 + 3 + ⋯ + n).

def n_esimo_número_triangular(n: int):
    """
    Describe el 'n'-ésimo número triangular.
    Pre:
        - El número dado debe ser >= 0.
    """
    if n == 1: return 1 
    return n_esimo_número_triangular(n-1) + n 

# Ejemplo de uso
n = 5
resultado = n_esimo_número_triangular(n)
print(f"El {n}-ésimo número triangular es {resultado}")