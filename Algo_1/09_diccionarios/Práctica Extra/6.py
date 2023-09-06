# 6.

def eliminar_productos_defectuosos(productos):
    """
    Esta función recibe una lista de productos representados como diccionarios y elimina los productos defectuosos
    que no pasaron el cheque de calidad. Retorna una tupla que contiene la lista de productos modificada y la
    cantidad de productos que quedaron.
    Parámetros:
        - productos: Una lista de diccionarios, donde cada diccionario representa un producto con la clave 'Chequeo de calidad'.
    Retorna:
        -Una tupla que contiene la lista de productos sin los productos defectuosos y la cantidad de productos restantes.
    Observación:
        - raises ValueError: Si la lista de productos está vacía.
    """
    if not productos: raise ValueError("Lista de productos vacía")
    
    productos_sin_defectos = [producto for producto in productos if producto['Chequeo de calidad']]
    cantidad_de_productos_sin_defectos = len(productos_sin_defectos)
    return productos_sin_defectos, cantidad_de_productos_sin_defectos