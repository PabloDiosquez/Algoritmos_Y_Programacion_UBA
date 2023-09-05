# MergeSort 🐕‍🦺

def mergesort(L):
    """
    Describe la lista que resulta de ordenar los elementos de la lista dada.
    (No modifica 'L')
    """
    if len(L) <= 1: return L
    med = len(L) // 2
    izq = mergesort(L[:med])
    der = mergesort(L[med+1:])
    return merge(izq, der) 

def merge(L1, L2):
    """
    Intercala los elementos de las dos listas de forma ordenada.
    Pre:
    - Las listas dadas (L1 y L2) deben estar ordenadas de manera ascendente.
    Post:
    - Devuelve una nueva lista (R) que contiene todos los elementos de L1 y L2,
      manteniendo el orden ascendente.
    """
    i, j = 0, 0
    R = []

    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i += 1
        else:
            R.append(L2[j])
            j += 1
    # Agregar lo que falta
    R += L1[i:] 
    R += L2[i:]
    return R 

# Anexo ⭐

# Merge Sort divide la lista no ordenada en dos mitades iguales, ordena cada mitad de forma recursiva y luego combina (fusiona) las dos mitades ordenadas en una sola lista ordenada. El proceso de división y combinación continúa hasta que la lista esté completamente ordenada.

# Pseudocódigo del Merge Sort:

# merge_sort(lista):
#     Si la longitud de la lista es 0 o 1, devolver la lista (caso base).
    
#     Dividir la lista en dos mitades, izquierda y derecha.
    
#     Aplicar merge_sort a la mitad izquierda.
#     Aplicar merge_sort a la mitad derecha.
    
#     Fusionar (merge) las dos mitades ordenadas en una sola lista ordenada.
    
#     Devolver la lista ordenada.

# Complejidad Temporal:

# La complejidad temporal de Merge Sort es O(n log n) en todos los casos, donde "n" es el número de elementos en la lista. Esto significa que Merge Sort es eficiente y conserva su rendimiento incluso en listas grandes.

# El análisis matemático detrás de esta complejidad se basa en el hecho de que el algoritmo divide repetidamente la lista en dos mitades iguales hasta que las sublistas tengan solo un elemento (caso base). Luego, fusiona (merge) las sublistas de manera eficiente en un proceso que también es O(n). Por lo tanto, el número total de operaciones realizadas es proporcional a n * log n.

# Complejidad Espacial:

# La complejidad espacial de Merge Sort es O(n) debido a la necesidad de almacenar temporalmente las sublistas durante la fase de fusión. Esto significa que Merge Sort requiere memoria adicional en función del tamaño de la lista que se está ordenando. Sin embargo, en comparación con otros algoritmos de ordenamiento, Merge Sort es bastante eficiente en términos de uso de memoria.

# Análisis Matemático:

# El análisis matemático de Merge Sort se basa en el teorema maestro, que proporciona una forma de analizar la complejidad de los algoritmos de "dividir y conquistar". En el caso de Merge Sort, el teorema maestro muestra que la complejidad es O(n log n) debido a las divisiones recursivas de la lista y la fusión eficiente de las sublistas.

# En resumen, Merge Sort es un algoritmo de ordenamiento eficiente con una complejidad temporal de O(n log n) en todos los casos, lo que lo hace adecuado para ordenar grandes conjuntos de datos. También tiene una complejidad espacial de O(n), lo que lo hace eficiente en términos de memoria. Su análisis matemático respalda su eficiencia y rendimiento constante.