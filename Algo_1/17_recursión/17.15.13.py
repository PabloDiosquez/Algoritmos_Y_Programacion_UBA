# Escribir una función recursiva que reciba un conjunto de caracteres únicos,
# y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres
# dados (permitiendo caracteres repetidos).
# Ejemplo: combinaciones(['a', 'b', 'c'], 2) debe imprimir aa ab ac ba bb bc ca cb cc

def combinaciones(lista: list, longitud: int):
    """
    """
    if longitud == 1: return lista
    return _agregar_adelante_todos(combinaciones(lista, longitud-1),lista)
    

def _agregar_adelante_todos(lista, lista_aux):
    """
    """
    if not len(lista_aux): return []
    primer_elemento = lista_aux[0]
    resto = lista_aux[1:]
    return _agregar_adelante(lista, primer_elemento) + _agregar_adelante_todos(lista, resto)


def _agregar_adelante(lista: list[str], c: str):
    """
    """
    if not len(lista): return []
    primer_elemento = lista[0]
    resto           = lista[1:]
    nuevo = c + primer_elemento
    return [nuevo] + _agregar_adelante(resto, c)

L = ['a','b','c']
print(combinaciones(L,3))