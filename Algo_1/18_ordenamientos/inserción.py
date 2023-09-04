# Ordenamiento por Inserción 🐍

def ordenar_inserción(L):
    """
    Ordena los elementos de la lista que recibe.
    Invariante:
        - La sublista L[0], ..., L[i-1] está ordenada.
    """
    for i in range(1, len(L)):
        insertar_ordenado(L, i) 

def insertar_ordenado(L, i):
    """
    Inserta de manera ordenada el elemento L[i] en la sublista L[:i].
    Pre:
        - L[:i] está ordenada.
    Post:
        - L[:i+1] está ordenada y contiene los mismos elementos que L[:i] más el elemento que estaba en i.
    """
    v = L[i]
    j = i-1
    while j >= 0 and L[j] > v:
        L[j+1] = L[j]
        j -= 1
    L[j+1] = v 

# Anexo 🥐

# El algoritmo de ordenamiento por inserción es un algoritmo simple y eficiente que trabaja dividiendo la lista en dos partes: una parte ordenada y otra parte desordenada. A medida que avanza a través de la lista, compara cada elemento con los elementos en la parte ordenada e inserta el elemento en la posición correcta.

# Pseudocódigo del Algoritmo de Ordenamiento por Inserción:

# Comienza con un solo elemento en la parte ordenada (el primer elemento de la lista se considera ordenado por defecto).

# Recorre los elementos restantes uno por uno en la parte desordenada.

# Para cada elemento en la parte desordenada, compáralo con los elementos en la parte ordenada y muévelo a la posición adecuada dentro de la parte ordenada.

# Repite los pasos 2 y 3 hasta que todos los elementos estén en la parte ordenada.

def insertion_sort(arr):
    # Recorre todos los elementos desde el segundo hasta el final de la lista
    for i in range(1, len(arr)):
        # Almacenamos temporalmente el elemento actual
        current_element = arr[i]
        # Comparamos el elemento actual con los elementos en la parte ordenada
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            # Si el elemento actual es menor que el elemento en la parte ordenada,
            # desplazamos el elemento en la parte ordenada una posición hacia la derecha
            arr[j + 1] = arr[j]
            j -= 1
        # Colocamos el elemento actual en su posición correcta en la parte ordenada
        arr[j + 1] = current_element

# Ejemplo de uso
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Lista ordenada:", my_list)

# Explicación del Código:

# El algoritmo recorre la lista desde el segundo elemento (i empieza en 1) hasta el último (len(arr) - 1).
# En cada iteración, el elemento actual se almacena en current_element.
# Se inicia un bucle while para comparar current_element con los elementos en la parte ordenada (desde j hasta 0).
# Si current_element es menor que el elemento en la parte ordenada, se desplaza el elemento en la parte ordenada hacia la derecha para hacer espacio.
# Finalmente, current_element se coloca en su posición correcta en la parte ordenada.
# El resultado es una lista ordenada en orden ascendente. El algoritmo de ordenamiento por inserción tiene una complejidad de tiempo de O(n^2) en el peor caso, lo que lo hace adecuado para listas pequeñas o parcialmente ordenadas.