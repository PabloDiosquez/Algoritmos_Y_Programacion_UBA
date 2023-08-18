# a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)

def encajan(primer_ficha: tuple, segunda_ficha: tuple) -> bool:
    """ Indica si las dos fichas de dominó dadas encajan.
    """
    return primer_ficha[0] == segunda_ficha[0] or primer_ficha[0] == segunda_ficha[1] or primer_ficha[1] == segunda_ficha[0] or primer_ficha[1] == segunda_ficha[1]

# b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
# cadenas.

def encajan(primer_ficha: str, segunda_ficha: str) -> bool:
    """ Indica si las dos fichas de dominó dadas encajan.
    """
    return primer_ficha[0] == segunda_ficha[0] or primer_ficha[0] == segunda_ficha[2] or primer_ficha[2] == segunda_ficha[0] or primer_ficha[2] == segunda_ficha[2]