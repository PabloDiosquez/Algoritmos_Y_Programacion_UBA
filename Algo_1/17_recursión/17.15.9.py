# Escribir una función recursiva para replicar los elementos de una lista una
# cantidad n de veces. Por ejemplo:
# replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])

from helpers import es_vacía, lista_vacía

def replicar(lista: list, cantidad: int):
    """
    Describe una lista con los elementos de la lista dada replicados 'cantidad' de veces.
    Parámetros:
        - lista (list):   Lista de elementos a replicar.  
        - cantidad (int): Cantidad de veces que se van a replicar los elementos de la lista dada.
    Retorna:
        - Una lista con los elementos de la lista dada replicados 'cantidad' de veces.{
    Ejemplo de uso:
        >>> replicar([1, 3, 3, 7], 2)
        [1, 1, 3, 3, 3, 3, 7, 7] 
    """
    if es_vacía(lista) or cantidad == 0: return lista_vacía()
    primer_elemento = lista[0]
    resto           = lista[1:]
    return [primer_elemento]*cantidad + replicar(resto, cantidad)

# Otras soluciones 🙃...

def replicarV1(numeros, cantidad):
    """
    Replica recursivamente los elementos de una lista una cantidad n de veces.
    
    Esta versión utiliza la técnica de replicación mediante la creación de una nueva lista 
    que contiene la primera posición replicada n veces, concatenada con el resultado de 
    la replicación recursiva del resto de la lista.

    Parámetros:
    - numeros (list): La lista cuyos elementos se replicarán.
    - cantidad (int): La cantidad de veces que se replicarán los elementos.

    Retorna:
    list: La lista resultante después de replicar los elementos.

    Ejemplo:
    >>> replicarV1([1, 3, 3, 7], 2)
    [1, 1, 3, 3, 3, 3, 7, 7]
    """
    # Caso base: si la lista está vacía, la lista resultante es vacía.
    if not numeros:
        return []
    # Replica el primer elemento de la lista n veces y concatena el resultado 
    # con la replicación recursiva del resto de la lista.
    return [numeros[0]] * cantidad + replicarV1(numeros[1:], cantidad)


def replicarV2(numeros, cantidad):
    """
    Replica recursivamente los elementos de una lista una cantidad n de veces.

    Esta versión utiliza la técnica de replicación mediante la concatenación de la lista
    original con el resultado de la replicación recursiva decrementando la cantidad.

    Parámetros:
    - numeros (list): La lista cuyos elementos se replicarán.
    - cantidad (int): La cantidad de veces que se replicarán los elementos.

    Retorna:
    list: La lista resultante después de replicar los elementos.

    Ejemplo:
    >>> replicarV2([1, 3, 3, 7], 2)
    [1, 3, 3, 7, 1, 3, 3, 7]
    """
    # Caso base: si la cantidad es 0, la lista resultante es vacía.
    if not cantidad:
        return []
    # Concatena la lista original con el resultado de la replicación recursiva
    # decrementando la cantidad.
    return numeros + replicarV2(numeros, cantidad - 1)

# Ejemplo de uso
resultado = replicarV2([1, 3, 3, 7], 2)
print(resultado)