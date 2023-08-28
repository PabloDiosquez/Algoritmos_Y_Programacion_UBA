def validar_número(valor):
    """
    Si el valor es numérico lo devuelve. En caso contrario lanza TypeError.
    """
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor!r} no es un valor numérico")
    return valor 