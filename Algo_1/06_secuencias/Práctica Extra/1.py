# 1.
def vocales(texto: str):
    "Recibe un str y devuelve los caracteres que sólo sean vocales"
    vocales = ""
    for caracter in texto:
        if es_vocal(caracter):
            vocales += caracter
    return vocales 

def es_vocal(caracter: str):
    "Indica si el caracter dado es una vocal"
    VOCALES = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return caracter in VOCALES