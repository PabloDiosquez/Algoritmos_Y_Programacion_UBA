# 4.
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

def cambia_palabra(ruta):
    """
    Reemplaza una palabra en un archivo de texto.
    Esta función abre un archivo de texto especificado por 'ruta', busca una palabra específica ingresada por el usuario ('palabra_a_reemplazar') y la reemplaza con otra palabra ingresada por el usuario ('palabra_nueva'). Luego, guarda los cambios en el mismo archivo.
    Parámetros:
    - ruta (str): La ruta del archivo de texto en el que se realizará el reemplazo.
    """
    # Abre el archivo en modo lectura ('r') y lee su contenido
    file = open(ruta, "r")
    texto = file.readlines()
    file.close()
    # Solicita al usuario que ingrese la palabra que desea reemplazar ('palabra_a_reemplazar') y la nueva palabra ('palabra_nueva').
    palabra_a_reemplazar = input("¿Qué palabra querés reemplazar?\n")
    palabra_nueva        = input("¿Cuál es la palabra nueva?\n")
    # Abre el archivo en modo escritura ('w') para sobrescribir su contenido.
    file = open(ruta, "w")
    # Reemplaza 'palabra_a_reemplazar' con 'palabra_nueva' en cada línea.
    for linea in texto:
        # Escribe la línea modificada en el archivo.
        file.write(linea.replace(palabra_a_reemplazar, palabra_nueva))

# Uso de la función definida anteriormente
ruta = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\poema.txt"
cambia_palabra(ruta)