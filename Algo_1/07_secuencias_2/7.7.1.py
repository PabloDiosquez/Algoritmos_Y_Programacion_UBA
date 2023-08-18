# Escribir una función que reciba una tupla de elementos e indique si se encuen-
# tran ordenados de menor a mayor o no.

def está_ordenada_de_menor_a_mayor(tupla: tuple) -> bool:
    """ Indica si la tupla dada está ordenada de menor a mayor.
        Observación: 
            La tupla vacía está ordenada de menor a mayor.
    """
    for índice in range(len(tupla)-1):
        if tupla[índice] > tupla[índice + 1]: 
            return False 
    return True 

def está_ordenado_división_y_conquista(tupla):
    """ Indica si la tupla dada está ordenada de menor a mayor.
        Observación: 
            La tupla vacía está ordenada de menor a mayor.
    """
    if len(tupla) <= 1:
        return True
    
    mitad     = len(tupla) // 2
    izquierda = tupla[:mitad]
    derecha   = tupla[mitad:]

    if not está_ordenado_división_y_conquista(izquierda) or not está_ordenado_división_y_conquista(derecha):
        return False

    if izquierda[-1] > derecha[0]:
        return False

    return True

def pruebas():
    assert     está_ordenada_de_menor_a_mayor(tuple())
    assert     está_ordenada_de_menor_a_mayor((1,1,2))
    assert     está_ordenada_de_menor_a_mayor((1,1,2))
    assert not está_ordenada_de_menor_a_mayor((3,2,1))
    assert not está_ordenada_de_menor_a_mayor((1,3,2))

    assert está_ordenado_división_y_conquista(str())
    assert está_ordenado_división_y_conquista((1,1,2))
    assert está_ordenado_división_y_conquista((1,2,3))
    assert not está_ordenado_división_y_conquista((3,2,1))
    assert not está_ordenado_división_y_conquista((1,3,2))

pruebas()