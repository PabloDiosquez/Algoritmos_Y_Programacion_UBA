# Escribir una función que reciba una lista de tuplas, y que devuelva un dicciona-
# rio en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
# segundos.
# Por ejemplo:
# >>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
# >>> print(tuplas_a_diccionario(l))
# { 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

def tuplas_a_diccionario(lista: list[tuple]) -> dict:
    """
    Describe un diccionario en el cual las claves son los primeros elementos de las tuplas de la lista dada, y los valores son una lista con los segundos elementos de dichas tuplas.
    Parámetros:
        - lista (list[tupla]): Una lista de tuplas.
    Retorna:
        - diccionario (dict): Un diccionario en donde las claves son los primeros elementos de las tuplas y los valores son una lista con los segundos elementos de dichas tuplas.
    """
    diccionario = {}
    for clave, valor in lista:
        agregar_par_al_diccionario(clave, valor, diccionario)
    return diccionario


def agregar_par_al_diccionario(clave, valor, diccionario):
    """
    """
    if clave in diccionario:
        diccionario[clave] += [valor]
    else:
        diccionario[clave] = [valor]

def pruebas():
    l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
    print(tuplas_a_diccionario(l))

pruebas()