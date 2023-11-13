# Se tiene un archivo con el siguiente texto:

# Paco Peco, chico rico,
# insultaba como un loco
# a su tío Federico;
# y éste dijo: Poco a poco,
# Paco Peco, poco pico. Me han dicho que has dicho un dicho
# que han dicho que he dicho yo,
# el que lo ha dicho, mintió,
# y en caso que hubiese dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo,
# dicho y redicho quedó.
# y estaría muy bien dicho,
# siempre que yo hubiera dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo.

# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función
# recibe “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.

from helpers import get_lines, set_file  # Importa las funciones get_lines y set_file desde el módulo helpers

PATH_DIR = 'archivos/poema.txt'  # Ruta del archivo donde se encuentra el poema

def main():
    """
    Función principal del programa. Lee un poema, permite al usuario modificar una palabra en el mismo y guarda el poema modificado.
    """
    estrofas = get_lines(PATH_DIR)
    # Lee las líneas del poema ubicado en el archivo especificado por PATH_DIR y guarda cada estrofa en una lista

    palabra_vieja = input('¿Qué palabra desea modificar?\n')  
    # Solicita al usuario la palabra que desea modificar en el poema

    palabra_nueva = input('¿Cuál es la palabra nueva?\n')
    # Solicita al usuario la palabra nueva que reemplazará a la palabra antigua en el poema

    estrofas_modificadas = [f'{estrofa.replace(palabra_vieja, palabra_nueva)}\n' for estrofa in estrofas]
    # Modifica las estrofas del poema reemplazando la palabra antigua por la nueva y guarda las estrofas modificadas en una lista

    set_file(PATH_DIR, estrofas_modificadas)
    # Guarda las estrofas del poema, ya modificadas, en el archivo de origen especificado por PATH_DIR

main()  # Llama a la función principal para ejecutar el programa