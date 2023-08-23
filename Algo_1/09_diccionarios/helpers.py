def agregar_par_al_diccionario(clave, valor, diccionario):
    """
    """
    if clave in diccionario:
        diccionario.get(clave).append(valor)
    else:
        diccionario[clave] = [valor]

def agregar_clave_valor_si_no_está(clave, valor, diccionario):
    """
    """
    if clave not in diccionario:
        diccionario[clave] = valor 

def apariciones(palabra: str, cadena: str) -> int:
    """
    Describe la cantidad de apariciones de 'palabra' en 'cadena'.
    """
    apariciones_al_momento = 0
    palabras = cadena.split(' ')
    for p in palabras:
        apariciones_al_momento += uno_si_cero_sino(p.lower() == palabra.lower())
    return apariciones_al_momento

def repeticiones(key, secuencia) -> int:
    """
    """
    repeticiones_al_momento = 0
    for elemento in secuencia:
        repeticiones_al_momento += uno_si_cero_sino(key == elemento)
    return repeticiones_al_momento

def uno_si_cero_sino(condición: bool) -> int:
    """
    Describe 1 si se cumple la condición dada; en caso contrario, describe 0.
    """
    if condición: return 1 
    return 0