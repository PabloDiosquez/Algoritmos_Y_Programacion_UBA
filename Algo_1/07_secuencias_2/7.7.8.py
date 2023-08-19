# Inversión de listas
# a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
# igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
# deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

from helpers import es_vacía

def lista_invertida(lista: list) -> list:
    invertida = list()
    for index in range(len(lista)-1, -1, -1):
        invertida.append(lista[index])
    return invertida

# b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista dada para invertirla, sin usar listas auxiliares.

def lista_invertida(lista: list) -> list:
    if es_vacía(lista): return lista
    primer_elemento = lista[0]
    lista.remove(primer_elemento)
    return lista_invertida(lista) + [primer_elemento]

def pruebas():
    assert lista_invertida([1,2,3]) == [3,2,1]
    assert lista_invertida(['Di', 'buen', 'día', 'a', 'papa']) == ['papa', 'a', 'día', 'buen', 'Di']

pruebas()