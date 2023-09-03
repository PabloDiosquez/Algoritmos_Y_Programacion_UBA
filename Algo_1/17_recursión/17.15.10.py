# Escribir una funcion recursiva que dada una cadena determine si en la misma
# hay más letras A o letras E.

# Una primer idea... 🤔
    
def mayor_cantidad_de__o_de__(cadena: str, letra1: str, letra2: str):
    """
    Dada una cadena determina si hay más letras 'letra1' o letras 'letra2'
    Pre:
        - La cadena dada no puede ser vacía.
    """
    return mayor_cantidad_de__o_de__hasta(cadena, letra1, 0, letra2, 0, len(cadena))

def mayor_cantidad_de__o_de__hasta(cadena: str, letra1: str, contador1: int, letra2: str, contador2: int, hasta: int):
    """
    Dada una cadena determina si hay más letras 'letra1' o letras 'letra2' hasta el índice 'hasta'.
    Pre:
        - La cadena dada no puede ser vacía.
        - Debe ser 0 <= 'hasta' <= len(cadena)
    """
    if hasta == 0:
        if max(contador1, contador2) == contador1:
            return f"Mayor cantidad de letras {letra1}"
        elif max(contador1, contador2) == contador2:
            return f"Mayor cantidad de letras {letra2}"
        return f"Igual cantidad de letras {letra1} que de letras {letra2}"
    
    letra_actual = cadena[hasta-1]

    if letra_actual == letra1: return mayor_cantidad_de__o_de__hasta(cadena, letra1, contador1 + 1, letra2, contador2, hasta-1)
    elif letra_actual == letra2: return mayor_cantidad_de__o_de__hasta(cadena, letra1, contador1, letra2, contador2 + 1, hasta-1)
    return mayor_cantidad_de__o_de__hasta(cadena, letra1, contador1, letra2, contador2, hasta-1) 

# Otra posible idea... 🐱‍🏍
# 
# from helpers import es_vacía

# def mayor_cantidad_de__o_de__(cadena: str, letra1: str, letra2: str):
#     """
    # Dada una cadena determina si hay más letras 'letra1' o letras 'letra2'
    # Pre:
    #     - La cadena dada no puede ser vacía.
#     if _mayor_cantidad_de__o_de__(cadena, letra1, letra2, 0) > 0:
#         return letra1
#     return letra2 

# def _mayor_cantidad_de__o_de__(cadena, letra1, letra2, contador):
#     """
#     Describe la letra que tiene mayor número de apariciones en la cadena dada.
#     """
#     if es_vacía(cadena): return contador 
#     primera_letra = cadena[0]
#     resto         = cadena[1:]
#     if primera_letra == letra1: return _mayor_cantidad_de__o_de__(resto, letra1, letra2, contador + 1)
#     elif primera_letra == letra2: return _mayor_cantidad_de__o_de__(resto, letra1, letra2, contador - 1)
#     return _mayor_cantidad_de__o_de__(resto, letra1, letra2, contador)

# def contar_letras(cadena: str, letra: str):
#     """
#     Describe la cantidad de 'letra' que hay en la cadena dada.
#     """
#     if es_vacía(cadena): return 0 
#     primer_letra = cadena[0]
#     resto        = cadena[1:]
#     if primer_letra == letra: return 1 + contar_letras(resto, letra)
#     return     contar_letras(resto, letra)