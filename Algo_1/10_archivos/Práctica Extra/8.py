# Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada
# respuesta en un .csv de la siguiente manera: nombre;color;le gusta, pero se dió cuenta que no es una
# forma muy práctica de guardarlo, así que lo quiere cambiar. Hacer un programa que lea el archivo y lo
# transforme en un archivo .txt. Es decir que si se tiene un archivo csv de la siguiente forma:
# Agus;verde;si
# Tomi; violeta;no
# Manu;marrón;no
# El archivo .txt tiene que quedar así:
# A Agus sí le gusta el verde
# A Tomi no le gusta el violeta
# A Manu no le gusta el marrón

def para_gustos_colores(archivo_colores, archivo_colores_nuevo):
    """
    Esta función toma un archivo CSV que contiene información sobre los gustos de amigos por colores y crea un nuevo archivo de texto con el formato 'A {amigo} {gusto} le gusta el {color}'.
    Parámetros:
        - archivo_colores: Ruta al archivo CSV de entrada con los datos de gustos por colores.
        - archivo_colores_nuevo: Ruta al archivo de texto de salida donde se guardarán los resultados.
    """
    # Abre el archivo de colores en modo lectura
    with open(archivo_colores, "r") as file_colores:
        # Lee todas las líneas del archivo y las almacena en una lista
        amigos_y_colores = file_colores.readlines()
    
    # Abre el archivo de colores nuevo en modo escritura
    with open(archivo_colores_nuevo, "w") as file_colores_nuevo:
        # Itera a través de cada línea de gustos en la lista
        for gusto in amigos_y_colores:
            # Divide la línea en amigo, color y gusto utilizando el carácter ';'
            amigo, color, gusto = gusto.strip("\n").split(";")
            # Escribe la información en el archivo de colores nuevo
            file_colores_nuevo.write(f"A {amigo} {gusto} le gusta el {color}\n")

# Rutas a los archivos de entrada y salida
ruta_colores = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\colores.csv"
ruta_colores_nuevo = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\colores.txt"

# Llama a la función para realizar la conversión
para_gustos_colores(ruta_colores, ruta_colores_nuevo)