# Escribir una función que reciba las coordenadas de un vector en R3
# (x,y,z) y devuelva la norma del vector.

from math import sqrt

def norma_vectorial3(x1, x2, x3):
    """Describe la norma del vector de R3 cuyas coordenas se corresponden con los números dados.
    """
    return sqrt(pow(x1,2) + pow(x2,2) + pow(x3,2))