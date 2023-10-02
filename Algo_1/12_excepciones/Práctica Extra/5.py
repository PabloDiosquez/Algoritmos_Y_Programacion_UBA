# Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la
# lista en esa ubicación.
# a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango?
# b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso
# contrario, mostrar un mensaje apropiado para dicho error.

def mostrar_valor_lista(lista, indice):
    """
    Describe el valor de una lista en una posición dada por el índice.
    Parámetros:
        - lista (list): La lista en la que buscar el valor.
        - indice (int): El índice de posición en la lista.
    Retorna:
        str: El valor de la lista en la ubicación especificada o un mensaje de error.
    """
    try:
        return lista[indice]
    except IndexError:
        return f"El índice está fuera del rango válido.\nIngrese un valor entre 0 y {len(lista)-1}"

# Ejemplo de uso:
if __name__ == "__main__":
    mi_lista = [1, 2, 3, 4, 5]
    indice = 3
    resultado = mostrar_valor_lista(mi_lista, indice)
    print(resultado)
 