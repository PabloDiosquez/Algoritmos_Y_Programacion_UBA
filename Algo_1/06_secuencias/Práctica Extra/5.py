# 5.
def insertar_ordenado(números: list, número: int):
    """
    Inserta 'número' en la lista 'números' manteniendo el orden.
    Pre:
        - La lista de números 'números' debe estar ordenada de menor a mayor.
    """
    índice = 0
    while índice < len(números):
        if números[índice] > número: break 
        índice += 1
    números.insert(índice, número)
    return números