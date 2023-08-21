from helpers import imprimir_lista, es_vacía, sumas_elementos_listas
from random import randint

# Matrices.
# a) Escribir una función que reciba dos matrices y devuelva la sumas.
# b) Escribir una función que reciba dos matrices y devuelva el producto.

# a) 
def sumas_matrices(matriz1: list[list], matriz2: list[list]):
    """ Describe la sumas de las dos matrices dadas.
        Precondiciones:
            - Las matrices dadas deben ser del mismo orden.
            - Los elementos de las matrices dadas deben soportar el operador +.
        - Parámetros:
            - matriz1 (list[list[a]]): La primera de las matrices a sumasr.
            - matriz2 (list[list[a]]): La segunda de las matrices a sumasr.
        Retorna:
            - matriz (list[list[a]]): sumas de las dos matrices dadas.
    """
    
    if es_vacía(matriz1):   return matriz2
    elif es_vacía(matriz2): return matriz1

    primer_fila_matriz1 = matriz1[0]
    primer_fila_matriz2 = matriz2[0]
    matriz1.remove(primer_fila_matriz1)
    matriz2.remove(primer_fila_matriz2)
    return [sumas_elementos_listas(primer_fila_matriz1, primer_fila_matriz2)] + sumas_matrices(matriz1, matriz2)

# b)
def producto_matrices(matriz1: list[list], matriz2: list[list]):
    """
    """
    pass 

# -------------------------------------------------------------------------- # 
# La forma más usual de representar matrices es mediante una lista de filas 🐣
# m = [[1, 2, 3], [4, 5, 6]]

def imprimir_matriz(matriz: list[list]):
    """
    """
    cantidad_filas    = len(matriz)
    cantidad_columnas = len(matriz[0])
    for f in range(cantidad_filas):
        for c in range(cantidad_columnas):
            print(matriz[f][c], end=' ')
        print() # Salto a la otra fila 🐸

# Una alternativa ☂

def imprimir_matriz(matriz: list[list]):
    """
    """
    for fila in matriz:
        imprimir_lista(fila)
        print()

# imprimir_matriz(m)

# Escribir una función que reciba las dimensiones (cantidad de filas y columnas)
# y devuelva una matriz donde cada elemento sea una cadena de la forma "xy", donde x es una
# letra representando la columna e y un número representando la fila.

LETRAS = 'abcdefghijklmnopqrstuvwxyz'

def crear_matriz_xy(cantidad_filas: int, cantidad_columnas: int):
    """
    """
    matriz = list()
    for f in range(cantidad_filas):
        fila = list()
        for c in range(cantidad_columnas):
            index = randint(0, len(LETRAS)-1)
            fila.append(LETRAS[index])
        matriz.append(fila)
    return matriz

# imprimir_matriz(crear_matriz_xy(3,4))

m = [[1, 2, 3], [4, 5, 6]]
n = [[2, 3], [1,6], [1,8]]

imprimir_matriz(sumas_matrices(m, n))
imprimir_matriz(producto_matrices(m, n))