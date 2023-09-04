# Búsqueda binaria 🌳 

def búsqueda_iter(L, x):
    """
    Describe el índice del elemento dado en la secuencia dada. En caso de no encontrarlo, describe -1.
    Pre:
        - La secuencia dada debe estar ordenada.
    """
    izq = 0
    der = len(L) - 1
    while izq <= der:
        medio = (izq + der)// 2
        if L[medio] == x:  return medio 
        elif L[medio] < x: izq = medio + 1
        else:              der = medio - 1
    return -1 


def búsqueda_recursiva(L, x):
    """
    Describe el índice del elemento dado en la secuencia dada. En caso de no encontrarlo, describe -1.
    Pre:
        - La secuencia dada debe estar ordenada.
    """
    if len(L) == 0: return -1 
    izq = 0
    der = len(L) - 1 
    medio = (izq + der) // 2
    if   L[medio] == x:return medio 
    elif L[medio] < x: return búsqueda_recursiva(L[medio+1:], x)
    else:              return búsqueda_recursiva(L[:medio], x)

# Búsqueda buinaria con wrapper 🌮

def búsqueda_binaria(L, x):
    """
    Describe el índice del elemento dado en la secuencia dada. En caso de no encontrarlo, describe -1.
    Pre:
        - La secuencia dada debe estar ordenada.
    """
    return _búsqueda_binaria(L, x, 0, len(L)-1)

def _búsqueda_binaria(L, x, desde, hasta):
    """
    Describe el índice del elemento dado en la secuencia dada desde 'desde' hasta 'hasta'. En caso de no encontrarlo, describe -1.
    Pre:
        - La secuencia dada debe estar ordenada.
        - Debe ser 'desde' < 'hasta' < len(L) 
    """
    if desde > hasta:  return -1 
    medio = (desde + hasta) // 2
    if L[medio] == x:  return medio 
    elif L[medio] < x: return _búsqueda_binaria(L, x, desde+1, hasta)
    return _búsqueda_binaria(L, x, desde, hasta-1)