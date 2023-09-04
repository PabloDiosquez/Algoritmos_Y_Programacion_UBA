# Ordenamiento por Selección 🐀

def ordenar_selección(L):
    """
    Ordena los elementos de la lista que recibe.
    Invariantes:
        - La sublista L[0], ..., L[i] está ordenada.
        - Todos los elementos L[i+1], L[N-1] son mayores.
    """
    for i in range(len(L)-1):
        p = buscar_índice_del_mínimo(L, i, len(L)-1)
        L[i], L[p] = L[p], L[i] 
    
def buscar_índice_del_mínimo(L, desde, hasta):
    """
    Describe el índice del menor elemento de la lista.
    Pre: 
        - La lista dada no debe ser vacía.
        - Debe ser 'desde' <= 'hasta'.
    """
    mínimo_al_momento = L[desde]
    índice_al_momento = desde
    for i in range(desde+1, hasta+1):
        if L[i] < mínimo_al_momento:
            mínimo_al_momento = L[i]
            índice_al_momento = i 
    return índice_al_momento  

L = ['e', 'r', 'a', 'g', 'h', 'j', 'z', 'v']
print("Antes: ", L)
ordenar_selección(L)
print("Despúes: ", L)

# Anexo 🖖🏼

# El algoritmo de ordenamiento por ordenar_selección es un algoritmo simple pero ineficiente para ordenar una lista o arreglo de elementos. Funciona seleccionando repetidamente el elemento más pequeño (o más grande, dependiendo de si se desea ordenar de forma ascendente o descendente) de la lista y moviéndolo a la posición adecuada. Aquí tienes una descripción detallada del algoritmo junto con ejemplos en Python:

# Pseudocódigo:
# Para i desde 0 hasta n-1:
#     Encontrar el índice del elemento mínimo (o máximo) en el subarreglo no ordenado [i, n-1]
#     Intercambiar el elemento en el índice i con el elemento en el índice mínimo
# Ejemplo en Python:

def ordenamiento_por_seleccion(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # Supongamos que el primer elemento del subarreglo no ordenado es el mínimo
        min_index = i
        
        # Buscamos el índice del elemento mínimo en el subarreglo no ordenado
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiamos el elemento mínimo con el elemento en la posición i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso:
arr = [64, 25, 12, 22, 11]
ordenamiento_por_seleccion(arr)
print("Arreglo ordenado por ordenar_selección:", arr)
# Explicación paso a paso:

# Comenzamos con un arreglo desordenado, por ejemplo, [64, 25, 12, 22, 11].

# En la primera iteración (i = 0), asumimos que el primer elemento (64) es el mínimo. Luego, recorremos el subarreglo no ordenado [25, 12, 22, 11] para encontrar el mínimo real (11 en este caso). Intercambiamos 64 y 11.

# Ahora, el arreglo se ve así: [11, 25, 12, 22, 64]. El elemento más pequeño (11) se encuentra en la posición correcta.

# En la siguiente iteración (i = 1), asumimos que el segundo elemento (25) es el mínimo. Recorremos el subarreglo [25, 12, 22, 64] y encontramos que el mínimo real es 12. Intercambiamos 25 y 12.

# Repetimos este proceso para las siguientes iteraciones hasta que todo el arreglo esté ordenado.

# Al final, obtenemos el arreglo ordenado [11, 12, 22, 25, 64].

# Es importante destacar que el ordenamiento por ordenar_selección tiene un rendimiento de tiempo cuadrático (O(n^2)), lo que lo hace ineficiente para listas grandes, pero es fácil de implementar y entender. Por lo tanto, se utiliza principalmente en situaciones donde la simplicidad de implementación es más importante que la eficiencia.