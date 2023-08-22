# Escribir una función que reciba una lista de números no ordenada, que:
# a) Devuelva el valor máximo.
# b) Devuelva una tupla que incluya el valor máximo y su posición.
# c) ¿Qué sucede si los elementos son cadenas de caracteres?
# Nota: no utilizar lista.sort()

from helpers import máximo_entre

# a)
def máximo(lista: list[int]) -> int:
    """
    """
    if len(lista) == 1: return lista[0]
    nueva_lista = lista[:]
    primer_elemento = nueva_lista[0]
    nueva_lista.remove(primer_elemento)
    return máximo_entre(primer_elemento, máximo(nueva_lista))
    
# b)
def máximo_y_posición(lista: list):
    """
    """
    pass 