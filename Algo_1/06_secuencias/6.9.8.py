# Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.

def de_binario_a_decimal(unos_y_ceros: str):
    """ Describe el valor decimal correspondiente a la cadena de unos y ceros dada.
        Precondición: 'unos_y_ceros' debe ser una cadena de caracteres formada únicamente
        por ceros y unos válida (debe ser un número en representación binaria).
    """
    valor_decimal = 0
    exponente = len(unos_y_ceros) - 1
    for digito in unos_y_ceros:
        valor_decimal += pow(int(digito)*2, exponente)
        exponente -= 1
    return valor_decimal

# Una alternativa... 🐣
 
def de_binario_a_decimal_bis(unos_y_ceros: str):
    """ Describe el valor decimal correspondiente a la cadena de unos y ceros dada.
        Precondición: 'unos_y_ceros' debe ser una cadena de caracteres formada únicamente
        por ceros y unos válida (debe ser un número en representación binaria).
    """
    return int(unos_y_ceros, 2)

# La función utiliza la función int() con el segundo argumento establecido en 2, lo que indica que la cadena se interpreta como un número binario. Esto convierte la cadena binaria en su equivalente decimal.