# Búsqueda lineal ☂ 

def búsqueda_lineal(secuencia, elemento):
    """
    """
    for índice, valor in secuencia:
        if valor == elemento: return índice
    return -1 

def búsqueda_binaria(secuencia, elemento):
    """

    Precondición:
        - La secuencia dada debe estar ordenada.
    """
    izquierda = 0 
    derecha   = len(secuencia) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if    secuencia[medio] == elemento: return medio 
        elif  secuencia[medio] < elemento : izquierda = medio + 1
        else: derecha = medio - 1
    return -1  
