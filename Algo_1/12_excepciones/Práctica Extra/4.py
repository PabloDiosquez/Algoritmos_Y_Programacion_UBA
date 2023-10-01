# Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
# archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.

# FileNotFoundError: Este error ocurre cuando intentas abrir un archivo que no existe en la ubicación especificada. Para manejarlo, puedes verificar si el archivo existe antes de intentar abrirlo utilizando una declaración try...except.

def leer_archivo(archivo):
    """
    Lee el contenido de un archivo especificado y maneja excepciones si el archivo no existe.
    Parámetros:
        archivo (str): El nombre del archivo a leer.
    Retorna:
        str: El contenido del archivo.
    """
    try:
        file = open(archivo, "r")
        contenido = file.read()
        file.close()  # Es importante cerrar el archivo después de leerlo.
        return contenido
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{archivo}'")
        return None  