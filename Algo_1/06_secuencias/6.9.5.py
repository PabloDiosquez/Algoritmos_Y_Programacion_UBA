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

def primera_letra_en_mayúscula_vers1(cadena: str) -> str:
    """ 
    """
    palabras = cadena.split()
    cadena_nueva = str()
    for palabra in palabras:
        cadena_nueva += f"{palabra.capitalize()} "
    return cadena_nueva

def primera_letra_en_mayúscula_vers2(cadena: str):
    palabras = cadena.split()
    return ' '.join([palabra.capitalize() for palabra in palabras]) 

# print(primera_letra_en_mayúscula_vers1('república argentina'))
# print(primera_letra_en_mayúscula_vers2('república argentina'))

# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
# debe devolver 'Antes ayer'.

def palabras_que_comiencen_con__(cadena: str, letra: str) -> str:
    """
    """
    palabras = cadena.split()
    cadena_nueva = str()
    for palabra in palabras:
        if palabra[0] == letra or palabra[0] == letra.upper():
            cadena_nueva += f"{palabra} "
    return cadena_nueva

# print(palabras_que_comiencen_con__('Antes de ayer', 'a'))