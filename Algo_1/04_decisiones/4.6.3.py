# Escribir una función que reciba por parámetro una dimensión n, e imprima la
# matriz identidad correspondiente a esa dimensión.

def matriz_identidad(n: int):
    """Imprime por pantalla la matriz identidad correspondiente a la dimensión 
    dada por parámetro.
    """
    for i in range(n):
        for j in range(n):
            if j == i: print(1, end=" ")
            else: print(0, end=" ")
        print()

matriz_identidad(5)