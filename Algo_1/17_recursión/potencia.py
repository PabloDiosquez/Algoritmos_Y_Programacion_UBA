from helpers import es_par

# Exponenciación binaria 🚀         T(n) ➡ O(log n) || E(n) ➡ O(log n)
def potencia(b: float, n: int):
    """
    Describe 'b' elevado a la 'n'.
    Observaciones: 
        - El algoritmo utiliza la bien conocida propiedad: b^n = [b^(n/2)]^2
    """
    if n == 0: return 1
    restante = 1 
    pot = potencia(b, n // 2) 
    if not es_par(n):
        restante = b 
     
    return pot*pot*restante

print(potencia(3,11))