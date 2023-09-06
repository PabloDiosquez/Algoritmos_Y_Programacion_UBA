# 2.
def agregar_planta(plantas, especie, necesita_luz, precio):
    """
    Agrega una nueva planta a la lista de plantas dada.
    Parámetros:
        - plantas: Lista de plantas del vivero.
        - especie: Especie de la nueva planta agregada.
        - necesita_luz_solar: ¿Necesita luz del Sol la planta agregada?
        - precio: Precio de la nueva planta agregada.
    """
    plantas.append({
        'Especie': especie,
        '¿Necesita luz solar?': necesita_luz,
        'Precio': precio
    })