# Escribir una función empaquetar para una lista, donde epaquetar significa indi-
# car la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones).
# Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5,
# 1), (1, 2), (3, 2)].

def empaquetar(lista: list) -> list[tuple]:
    """ Describe una lista de tuplas (elemento, cantidad_de_apariciones) para cada elemento de la lista dada.
        Parámetros:
            - lista (list[a]): Lista de elementos.
        Retorna:
            - lista (list[tuple(a, int)]): Lista de tuplas formadas por cada elemento de la lista dada junto con su cantidad correspondiente de apariciones.
    """
    empaquetado = list()
    apariciones = 1
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            apariciones += 1
        else:
            empaquetado.append((lista[i], apariciones))
            apariciones = 1
    empaquetado.append((lista[-1], apariciones))
    return empaquetado 

# print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]))