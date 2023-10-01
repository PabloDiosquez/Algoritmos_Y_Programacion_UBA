# En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
# sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
# leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
# Por ejemplo si se tienen los siguientes archivos:
# (salas.txt) (peliculas.txt)
# D2              Megamente
# F1              Rápidos y furiosos
# E4              El padrino
# El              nuevo archivo deberá quedar:
# (funciones.csv)
# D2;Megamente
# F1;Rápidos y furiosos
# E4;El padrino

def funciones(archivo_salas, archivo_peliculas, archivo_funciones):
    """
    Combina la información de salas y películas y crea un archivo de funciones en formato CSV.
    Parámetros:
        - archivo_salas (str): La ruta al archivo que contiene la información de las salas.
        - archivo_peliculas (str): La ruta al archivo que contiene la información de las películas.
        - archivo_funciones (str): La ruta al archivo de salida donde se almacenarán las funciones combinadas.
    """
    # Abrir el archivo de salas en modo lectura
    with open(archivo_salas, "r") as file_salas:
        salas = file_salas.readlines()

    # Abrir el archivo de películas en modo lectura
    with open(archivo_peliculas, "r") as file_peliculas:
        peliculas = file_peliculas.readlines()

    # Combinar las salas y películas en una lista de tuplas
    funciones = [(sala.strip("\n"), pelicula.strip("\n")) for sala, pelicula in zip(salas, peliculas)]

    # Abrir el archivo de funciones en modo escritura
    with open(archivo_funciones, "w") as file_funciones:
        # Escribir las funciones en formato "sala;pelicula\n" en el archivo
        for sala, pelicula in funciones:
            file_funciones.write(f"{sala};{pelicula}\n")

# Rutas de los archivos de entrada y salida
ruta_salas = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\salas.txt"
ruta_peliculas = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\peliculas.txt"
ruta_funciones = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\funciones.csv"

# Llamar a la función para crear el archivo de funciones
funciones(ruta_salas, ruta_peliculas, ruta_funciones)