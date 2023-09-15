# 8.
def eliminar_elemento(tupla: tuple, eliminado: any):
    """
    Elimina un elemento específico de una tupla y devuelve una nueva tupla sin el elemento eliminado.
    Parámetros:
    - tupla (tuple): La tupla original de la que se eliminará el elemento.
    - eliminado (any): El elemento que se desea eliminar de la tupla.
    Retorna:
        - tuple: Una nueva tupla que contiene todos los elementos de la tupla original  excepto el elemento eliminado.
    Si el elemento no se encuentra en la tupla, se devuelve la tupla original sin cambios.
    """
    nueva = []
    for elemento in tupla:
        if elemento != eliminado:
            nueva.append(elemento)
    return tuple(nueva)

def eliminar_elemento(tupla: tuple, elemento_a_eliminar: any):
    """
    Elimina un elemento específico de una tupla y devuelve una nueva tupla sin el elemento eliminado.
    Parámetros:
    - tupla (tuple): La tupla original de la que se eliminará el elemento.
    - eliminado (any): El elemento que se desea eliminar de la tupla.
    Retorna:
        - tuple: Una nueva tupla que contiene todos los elementos de la tupla original  excepto el elemento eliminado.
    Si el elemento no se encuentra en la tupla, se devuelve la tupla original sin cambios.
    """
    if elemento_a_eliminar in tupla:
        índice = tupla.index(elemento_a_eliminar)
        return tupla[:índice] + tupla[índice+1:]
    return tupla 