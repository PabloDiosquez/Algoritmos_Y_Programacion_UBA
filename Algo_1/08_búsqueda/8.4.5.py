# Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
# se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
# no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
# (No utilizar lista.sort().)

def búsqueda_o_inserción(lista: list, elemento):
    """
    Describe la posición del elemento dado en la lista dada. En caso de que el elemento no pertenezca a la lista, describe la posición en la que el elemento debería estar.
    Parámetros:
        - lista: La lista en la que se realizará la búsqueda.
        - elemento: Elemento a buscar en la lista.
    Precondiciones:
        - La lista dada debe estar ordenada bajo algún criterio.
    """
    izq = 0 
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if   lista[medio] == elemento: return medio
        elif lista[medio] < elemento : izq = medio + 1
        else:                          der = medio - 1    

    return posición_correcta_en(lista, elemento)
    
def posición_correcta_en(lista, elemento):
    """
    Describe la posición correcta en la que debería estar el elemento dado en la lista dada. En caso de que el elemento pertenezca a la lista, describe la posición de la primera aparición del mismo.
    Parámetros:
        - lista: La lista en la que se realizará la búsqueda.
        - elemento: Elemento a buscar en la lista.
    Precondiciones:
        - La lista dada debe estar ordenada bajo algún criterio. 
    """
    posición_correcta_al_momento = 0
    for índice, valor in enumerate(lista):
        if valor > elemento: break
        posición_correcta_al_momento += 1  
    return posición_correcta_al_momento