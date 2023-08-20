# Funciones que reciben funciones.
# a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.

from helpers import es_vacía, singular_si

def map(f: function, lista: list) -> list:
    """
    """
    res = list()
    for elemento in lista:
        res.append(f(elemento))
    return res 

def map(f: function, lista: list) -> list:
    """
    """
    if es_vacía(lista): return lista
    primer_elemento = lista[0]
    lista.remove(primer_elemento)
    return [f(primer_elemento)] + map(f, lista) 

# b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una
# lista con los elementos de la lista recibida para los cuales la función recibida devuelve un valor verdadero.

def filter(f: function, lista: list) -> list:
    """
    """
    res = list()
    for elemento in lista:
        if f(lista):
            res.append(elemento)
    return res 

def filter(f: function, lista: list) -> list:
    """
    """
    if es_vacía(lista): return lista 
    primer_elemento = lista[0]
    lista.remove(primer_elemento)
    return singular_si(primer_elemento, f(primer_elemento)) + filter(f, lista)