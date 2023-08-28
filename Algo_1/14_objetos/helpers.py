def validar_número(valor):
    """
    Si el valor es numérico lo devuelve. En caso contrario lanza TypeError.
    """
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor!r} no es un valor numérico")
    return valor 

def validar_número_positivo(valor):
    """
    Si el valor es numérico y positivo lo devuelve. En caso contrario lanza una excepción.
    """
    if not isinstance(valor, (int, float)):
        raise TypeError(f"{valor!r} no es un valor numérico")
    if not valor > 0:
        raise ValueError("El número debe ser mayor a 0")
    return valor

def validar_número_entero_positivo(valor):
    """
    Si el valor es un número entero y positivo lo devuelve. En caso contrario lanza una excepción.
    """
    if not isinstance(valor, int):
        raise TypeError(f"{valor!r} no es un número entero")
    if not valor > 0:
        raise ValueError("El número debe ser mayor a 0")
    return valor 

def validar_cadena_no_vacía(cadena):
    """
    Si la cadena no es vacía la devuelve. En caso contrario lanza ValueError.
    """
    if es_vacía(cadena):
        raise ValueError("La cadena no debe ser vacía")
    return cadena

def es_vacía(cadena: str):
    """
    Indica si la cadena de caracteres dada es vacía.
    """
    return not len(cadena)