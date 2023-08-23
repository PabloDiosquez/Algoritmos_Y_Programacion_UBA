# Escribir una función que reciba un texto y para cada caracter presente en el texto
# devuelva la cadena más larga en la que se encuentra ese caracter.

def diccionario_de_caracteres(texto: str) -> dict:
    """
    """
    diccionario = {}
    for caracter in texto.replace(" ", ""):
        if caracter not in diccionario:
            diccionario[caracter] = cadena_más_larga(texto, caracter)
    return diccionario

def cadena_más_larga(texto: str, caracter: str) -> str:
    """
    Precondición:
        - El caracter dado debe pertenecer al texto dado.
    """
    cadenas = texto.split(' ')
    cadenas_contenedoras_al_momento = []
    for cadena in cadenas:
        agregar_elemento_si(cadenas_contenedoras_al_momento, cadena, caracter in cadena)
    return max(cadenas_contenedoras_al_momento, key=len)

def agregar_elemento_si(lista: list, elemento, condición: bool):
    """
    """
    if condición: 
        lista.append(elemento)

# print(diccionario_de_caracteres("Nosotros no somos como los Orozco"))