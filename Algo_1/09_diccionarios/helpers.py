def apariciones(palabra: str, cadena: str) -> int:
    """
    """
    apariciones_al_momento = 0
    palabras = cadena.split(' ')
    for p in palabras:
        apariciones_al_momento += uno_si_cero_sino(p == palabra)
    return apariciones_al_momento

def uno_si_cero_sino(condición: bool) -> int:
    """
    """
    if condición: return 1 
    return 0