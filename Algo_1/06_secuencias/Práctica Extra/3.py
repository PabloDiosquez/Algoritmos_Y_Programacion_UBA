# 3.
def eliminar_substring(cadena: str, subcadena: str):
    """
    Recibe dos strings 'cadena' y 'subcadena' y describe el string habiendo eliminado el substring del mismo.
    Pre:
        - 'cadena' debe contener a 'subcadena'
    """
    partes = cadena.split(" ")
    for parte in partes:
        if parte == subcadena:
            partes.remove(parte)
    return " ".join(partes) 