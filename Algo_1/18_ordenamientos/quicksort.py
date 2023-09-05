# QuickSort 🏃🏼‍♂️

def quicksort(L: list):
    """
    Describe la lista que resulta de ordenar los elementos de la lista dada.
    Pre:
        - Los elementos de 'L' deben ser comparables.
    """
    if len(L) <= 1: return L
    menores, medio, mayores = particiones(L)
    return quicksort(menores) + medio + quicksort(mayores)

def particiones(L):
    """
    Describe una partición de la lista dada en tres listas: menores, medio, mayores.
    Pre:
        - La lista dada no debe ser vacía.
    """
    p = pivot(L)
    menores = []
    mayores = []
    for x in range(len(L)):
        if   L[x] == p: continue
        elif L[x] < p:
            menores.append(L[x])
        else:
            mayores.append(L[x])
    return menores, [p], mayores

def pivot(L):
    """
    Describe un elemento aleatorio (pivot) de la lista dada.
    Pre:
        - La lista dada no debe ser vacía.
    """
    from random import randint
    return L[randint(0, len(L)-1)]

# Una pequeña prueba 🤘🏼

L = ['f', 'k', 'a', 'c', 'x', 'o', 'd']
print(quicksort(L))