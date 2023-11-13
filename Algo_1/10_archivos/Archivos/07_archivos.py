# En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
# sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
# leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
# Por ejemplo si se tienen los siguientes archivos:
# (salas.txt) (peliculas.txt)
# D2        Megamente
# F1        Rápidos y furiosos
# E4        El padrino
# El nuevo archivo deberá quedar:
# (funciones.csv)
# D2;Megamente
# F1;Rápidos y furiosos
# E4;El padrino

from helpers import get_lines, set_file, zipB  # Importar las funciones necesarias desde el módulo helpers

PATHDIR = 'archivos/cine'  # Variable que contiene la ruta del directorio 'archivos/cine'

def obtener_funciones(salas: list, películas: list) -> list:
    """
    Genera una lista de cadenas formateadas que representan funciones al emparejar horarios de películas con salas de cine.
    
    Argumentos:
    - salas (list): Lista de salas de cine
    - películas (list): Lista de películas
    
    Retorna:
    - List: Cadenas formateadas que representan horarios de películas emparejados con salas de cine
    """
    return [f'{";".join(función)}\n' for función in zipB(salas, películas)]
    # Genera cadenas formateadas al unir horarios y salas de cine de listas emparejadas

# Lee los datos de las salas desde el archivo 'salas.txt'
salas = get_lines(f'{PATHDIR}/salas.txt')

# Lee los datos de las películas desde el archivo 'peliculas.txt'
películas = get_lines(f'{PATHDIR}/peliculas.txt')

# Crea un archivo que contiene funciones formateadas al combinar salas de cine y películas
set_file(f'{PATHDIR}/funciones.csv', obtener_funciones(salas, películas))
# Escribe las funciones formateadas en un archivo llamado 'funciones.csv'