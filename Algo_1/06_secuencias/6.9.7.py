# Escribir funciones que dadas dos cadenas de caracteres:
# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
# es una subcadena de 'subcadena'.

def es_subcadena_de(primera_cadena: str, segunda_cadena: str):
    """ Indica si la segunda cadena es una subcadena de la primera.
        Observación: La cadena vacía es subcadena de todas las cadenas.
    """
    return segunda_cadena in primera_cadena

# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
# debe devolver 'gnome'.

def menor_entre(primera_cadena: str, segunda_cadena: str):
    for i in range(len(cadena_de_menor_longitud(primera_cadena, segunda_cadena))):
        if   primera_cadena[i] < segunda_cadena[i]: return primera_cadena
        elif primera_cadena[i] > segunda_cadena[i]: return segunda_cadena
    return primera_cadena

def cadena_de_menor_longitud(primera_cadena: str, segunda_cadena: str):
    """ Describe la cadena de caracteres de menor longitud entre las dos cadenas dadas.
    """
    return primera_cadena if len(primera_cadena) <= len(segunda_cadena) else segunda_cadena

# print(menor_entre('kde', 'gnome'))