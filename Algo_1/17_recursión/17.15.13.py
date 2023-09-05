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

# Otra solución posible...🐕‍🦺
def combinaciones(chars, k, prefijo=""):
    if k == 0:
        print(prefijo)
        return
    for char in chars:
        combinaciones(chars, k - 1, prefijo + char)

# Ejemplo de uso
caracteres = ['a', 'b', 'c']
k = 2
combinaciones(caracteres, k)

# Esta función combinaciones toma tres argumentos: chars es la lista de caracteres únicos, k es la longitud de las cadenas que deseas generar, y prefijo es un argumento auxiliar que acumula los caracteres a medida que se generan las combinaciones. La función se llama recursivamente reduciendo k en 1 en cada paso hasta que k sea igual a 0, momento en el que se imprime el prefijo actual. Esto genera todas las combinaciones posibles de longitud k con los caracteres dados.