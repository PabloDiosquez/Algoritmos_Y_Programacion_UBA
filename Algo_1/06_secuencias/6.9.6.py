# Ejercicio 6.9.6. Escribir funciones que dada una cadena de caracteres:
# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
# 'logaritmos' debe devolver 'lgrtms'.
# b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
# devolver 'i ooae'.

# a)
def consonantes_de_(cadena: str) -> str:
    """ Describe una cadena de caracteres formada solamente por las consonantes de la 
        cadena dada.
        Precondición: La cadena dada no debe ser vacía.
    """
    consonantes = str()
    for caracter in cadena:
        if es_consonante(caracter):
            consonantes += caracter
    return consonantes

def es_consonante(caracter: str) -> bool:
    """ Indica si el caracter dado es una consonante.
    """
    return caracter.lower() in "bcdfghjklmnpqrstvwxyz"

# b) 
def vocales_de_(cadena: str) -> str:
    """ Describe una cadena de caracteres formada solamente por las vocales de la 
        cadena dada.
        Precondición: La cadena dada no debe ser vacía.
    """
    vocales = str()
    for caracter in cadena:
        if es_vocal(caracter):
            vocales += caracter
    return vocales

def es_vocal(caracter: str) -> bool:
    """ Indica si el caracter dado es una vocal.
    """
    return caracter.lower() in "aeiouáéíóú"

# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
# devolver 'vistaerou'.

def switchear_vocales_por_su_siguiente(cadena: str) -> str:
    """ Dada una cadena de caracteres reemplaza cada vocal por su siguiente.
    """
    cadena_switcheada = str()
    for caracter in cadena: 
        cadena_switcheada += próxima_vocal_si(caracter, es_vocal(caracter))
    return cadena_switcheada

def próxima_vocal_si(caracter: str, condición: bool):
    """ Describe la vocal siguiente a la dada si se cumple la condición dada.
    """
    if condición:
        return vocal_siguiente(caracter)
    return caracter

def vocal_siguiente(vocal: str) -> str:
    vocal = vocal.lower()
    """ Describe la vocal siguiente a la dada.
        Precondición: El str dado debe ser una vocal.
    """
    if vocal   == 'a': proxima_vocal = 'e'
    elif vocal == 'e': proxima_vocal = 'i'
    elif vocal == 'i': proxima_vocal = 'o'
    elif vocal == 'o': proxima_vocal = 'u'
    elif vocal == 'u': proxima_vocal = 'a'
    return proxima_vocal

# print(switchear_vocales_por_su_siguiente('vestuario'))

# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un pa-
# líndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palíndromo(cadena: str) -> bool:
    """ Indica si la cadena dada es un palíndromo.
    """
    return not es_vacía(cadena) and eliminar_espacios(cadena) == eliminar_espacios(cadena_invertida(cadena))

def cadena_invertida(cadena: str) -> str:
    """ Describe la cadena dada al revés.
    """
    return cadena[::-1]

def eliminar_espacios(cadena: str) -> str:
    """ Describe la cadena dada comprimida (sin espacios).
    """
    return cadena.replace(' ','')

def es_vacía(cadena: str) -> bool:
    """ Indica si la cadena dada es vacía.
    """
    return cadena == str()

print(es_palíndromo("anita lava la tina"))