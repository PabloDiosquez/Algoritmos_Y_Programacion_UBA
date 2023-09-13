# 2.
def invertir_v1(cadena: str):
    "Recibe una cadena de texto y la invierte"
    invertida = ""
    for índice in range(len(cadena)-1, -1, -1):
        invertida += cadena[índice]
    return invertida

def invertir_v2(cadena: str):
    "Recibe una cadena de texto y la invierte"
    return cadena[::-1]