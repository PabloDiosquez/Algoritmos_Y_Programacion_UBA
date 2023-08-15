# Escribir funciones que dada una cadena y un caracter:
# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
# 's,e,p,a,r,a,r'

def insertar_caracter(cadena: str, separador: str):
    """ Describe una cadena de caracteres con el separador insertado entre cada letra de la cadena.  
    """
    res = str()
    for index in range(len(cadena)-1):
        res += cadena[index] + separador
    return res + cadena[index-1]

print(insertar_caracter("separar", ","))

# b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
# debería devolver 'mi_archivo_de_texto.txt'

def reemplazar_en____por__(cadena: str, caracter_viejo: str, caracter_nuevo: str) -> str:
    """ Reemplaza todas las apariciones de 'caracter_viejo' en la cadena dada por 'caracter_nuevo'.
    """
    cadena_nueva = str()
    for caracter in cadena:
        cadena_nueva += caracter____si__sino__(caracter_nuevo, caracter == caracter_viejo, caracter)
    return cadena_nueva

def caracter____si__sino__(caracter_nuevo, condición, caracter):
    """ Describe 'caracter_nuevo' si se cumple la condición. En caso contrario, describe
        'caracter'.
    """
    if condición:
        return caracter_nuevo
    return caracter

# print(reemplazar_en____por__('mi archivo de texto.txt', ' ', '_'))

# Usando el método replace() 🐣
# print('mi archivo de texto.txt'.replace(' ', '_'))

# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
# 'X' debería devolver 'su clave es: XXXX'

def reemplazar_dígitos_por_caracter(cadena: str, caracter_nuevo: str) -> str:
    cadena_nueva = str()
    for caracter in cadena:
        cadena_nueva += reemplazar__por__si_es_dígito(caracter, caracter_nuevo)
    return cadena_nueva

def reemplazar__por__si_es_dígito(caracter_viejo, caracter_nuevo):
    if es__dígito(caracter_viejo):
        return caracter_nuevo
    return caracter_viejo

def es__dígito(caracter):
    return caracter in "0123456789"

# print(reemplazar_dígitos_por_caracter('su clave es: 1540', 'X'))