# Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres.
# b) Imprima los tres últimos caracteres.
# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
# 'reflejoojelfer'.

# a)
def primeros_dos_caracteres(cadena: str):
    """ Imprime los primeros dos caracteres de la cadena dada.
        Pre: 
        La cadena dada debe tener al menos dos caracteres.
    """
    print(cadena[:2])

# b)
def ultimos_tres_caracteres(cadena: str):
    """ Imprime los tres últimos caracteres de la cadena de caracteres dada.
        Pre:
        La cadena dada debe tener al menos tres caracteres.
    """
    desde = len(cadena)-3
    print(cadena[desde:])

# c) 
def cadena_cada_dos(cadena: str):
    """ Imprime la cadena dada cada dos caracteres.
    """
    print(cadena[::2])

# d)
def cadena_en_reverso(cadena: str):
    """ Describe la cadena dada en orden inverso.
    """
    reverso = ""
    for i in range(len(cadena)-1, -1, -1):
        reverso += cadena[i]
    return reverso
    # return cadena[::-1] 

def imprimir_cadena_invertida(cadena: str):
    """ Imprime la cadena dada en orden inverso.
    """
    print(cadena_en_reverso(cadena))

# e)
def directo_e_inverso(cadena: str):
    """ Imprime la cadena en un sentido y en sentido inverso.
    """
    print(cadena + cadena_en_reverso(cadena))