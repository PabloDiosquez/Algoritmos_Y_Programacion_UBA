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

from helpers import get_lines, set_file  # Importa las funciones get_lines y set_file desde el módulo helpers

def customizar_datos_amigos(amigos: list) -> str:
    """
    Genera una cadena personalizada para cada amigo a partir de una lista de sus datos.
    
    Argumentos:
    - amigos (list): Lista con el nombre, gusto y color del amigo
    
    Retorna:
    - str: Cadena personalizada que describe los gustos del amigo
    """
    nombre, gusto, color = amigos
    return f'A {nombre} {gusto} le gusta el {color}\n'

def main():
    """
    Función principal del programa. Lee datos de amigos, los personaliza y los guarda en un archivo.
    """
    amigos = [customizar_datos_amigos(amigo.split(';')) for amigo in get_lines('archivos/amigos.csv')]
    # Lee datos de amigos desde el archivo 'amigos.csv', personaliza cada uno y los guarda en una lista

    set_file('archivos/amigos.txt', amigos)
    # Guarda los datos personalizados de amigos en un archivo llamado 'amigos.txt'

main()  # Llama a la función principal para ejecutar el programa