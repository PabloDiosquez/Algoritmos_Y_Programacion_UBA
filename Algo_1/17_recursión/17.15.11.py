# El triángulo de Pascal es un arreglo triangular de números que se define de la
# siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada
# fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los
# bordes del triángulo son 1. Cualquier otro valor se calcula sumando los dos valores contiguos
# de la fila de arriba.
# Escribir la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n
# y la columna k. Ejemplo: pascal(5, 2) -> 10

def pascal(n, k):
    """
    Describe el valor que se encuentra en la fila 'n' y la columna 'k' del triángulo de Pascal.
    """
    if k == 0: return 1 # Para todo los enteros n >= 0.
    if n == 0: return 0 # Para todos los enteros k > 0.
    return pascal(n-1, k-1) + pascal(n-1, k)

n = 5 
k = 2 
resultado = pascal(n, k)
print(f"El valor en la fila {n} y columna {k} del Triángulo de Pascal es: {resultado}")