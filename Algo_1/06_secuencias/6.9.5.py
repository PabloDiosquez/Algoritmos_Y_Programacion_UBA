# Escribir una función que dada una cadena de caracteres, devuelva:
# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
# devolver 'USB'.

def primera_letra_de_cada_palabra(cadena: str) -> str:
    """ Describe una cadena de caracteres formada por las primeras letras de cada palabra
        de la cadena dada.
        Precondición: La cadena dada no debe ser vacía.
    """
    primeras_letras = str()
    palabras = cadena.split(' ')
    for palabra in palabras:
        primeras_letras += palabra[0]
    return primeras_letras

# print(primera_letra_de_cada_palabra(''))

# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
# 'república argentina' debe devolver 'República Argentina'.
# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
# debe devolver 'Antes ayer'
