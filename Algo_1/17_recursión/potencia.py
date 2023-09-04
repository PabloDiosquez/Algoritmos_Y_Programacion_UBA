from helpers import es_par

def potencia(b: float, n: int):
    """
    Describe 'b' elevado a la 'n'.
    Observaciones: 
        - El algoritmo utiliza la bien conocida propiedad: b^n = [b^(n/2)]^2
    """
    if n == 0: return 1
    restante = 1  
    if not es_par(n):
        restante = b 
     
    return potencia(b, n // 2)*potencia(b, n// 2)*restante