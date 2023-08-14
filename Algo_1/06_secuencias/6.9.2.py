# Escribir funciones que dada una cadena y un caracter:
# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
# 's,e,p,a,r,a,r'

def insertar_caracter(cadena: str, separador: str):
    """ Describe una cadena de caracteres con el separador insertado entre cada letra de la 
        cadena.  
    """
    res = str()
    for index in range(len(cadena)-1):
        res += cadena[index] + separador
    return res + cadena[index-1]

print(insertar_caracter("separar", ","))