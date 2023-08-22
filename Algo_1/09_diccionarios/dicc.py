def traducir(texto, diccionario):
    """
    Reemplaza todas las palabras en el texto por su traducción correspondiente según el diccionario.
    Recibe:
        - <str> texto
    """
    palabras = texto.split(' ')
    palabras_traducidas = []
    for palabra in palabras:
        palabra_traducida = palabra
        for par in diccionario:
            if palabra == par[0]:
                palabra_traducida = par[1]
                palabras_traducidas.append(palabra_traducida)
                break
        palabras_traducidas.append(palabra_traducida)
    return ' '.join(palabras_traducidas)

diccionario = [
    ("algoritmos", "algorithms"),
    ("perro", "dog"),
    ("y", "and"),
    ("programación", "programming")
]

def main():
    assert traducir("algoritmos y programación", diccionario) == "algorithms and programming"