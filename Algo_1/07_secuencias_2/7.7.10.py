from helpers import imprimir_lista
from random import randint

# Matrices.
# a) Escribir una función que reciba dos matrices y devuelva la suma.
# b) Escribir una función que reciba dos matrices y devuelva el producto.

# a) 
def suma_matrices(matriz1: list[list], matriz2: list[list]):
    """
    """
    pass 

# b)
def producto_matrices(matriz1: list[list], matriz2: list[list]):
    """
    """
    pass 

# -------------------------------------------------------------------------- # 
# La forma más usual de representar matrices es mediante una lista de filas 🐣
m = [[1, 2, 3], [4, 5, 6]]

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

imprimir_matriz(crear_matriz_xy(3,3))