# Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
# excepto que también sea divisible por 400.

def es_bisiesto(año: int) -> bool:
    """ Indica si el año dado es bisiesto.
    """
    return (_es_divisible_por_(año, 4) and not _es_divisible_por_(año, 100)) or _es_divisible_por_(año, 400)

def _es_divisible_por_(num: int, otro_num: int) -> bool:
    """ Indica si el primer número dado es divisible por el segundo número dado.
    """
    return not num % otro_num