# Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar
# la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la
# respuesta dada por el usuario en el archivo.
# Por ejemplo,s e tiene el archivo pregunta.txt que originalmente tiene:
# ¿Cómo estás hoy?
# Y el usuario de la respuesta: “¡Bien, porque me comí una hamburguesa!”
# Entonces el archivo debería quedar de la forma:
# ¿Cómo estás hoy?
# ¡Bien, porque me comí una hamburguesa!

# Función para leer la pregunta desde un archivo de texto.
def leer_pregunta():
    with open('archivos/pregunta.txt', 'r', encoding='UTF-8') as archivo:
        return archivo.readline()  # Lee y retorna la primera línea del archivo.

# Función para obtener la respuesta del usuario a partir de un mensaje.
def obtener_respuesta(mensaje: str):
    return input(f'{mensaje}\n')  # Muestra el mensaje y espera la entrada del usuario.

# Función para escribir en un archivo la respuesta obtenida.
def escribir_archivo(respuesta: str):
    with open('archivos/pregunta.txt', 'a', encoding='UTF-8') as archivo:
        archivo.write(f'\n{respuesta}')  # Escribe la respuesta en una nueva línea en el archivo.
    print(f'El archivo "{archivo.name}" fue sobrescrito con éxito.')  # Imprime un mensaje de éxito.

# Función principal que coordina todas las operaciones.
def main():
    pregunta = leer_pregunta()  # Lee la pregunta del archivo.
    escribir_archivo(obtener_respuesta(pregunta))  # Obtiene la respuesta del usuario y la escribe en el archivo.

main()  # Ejecuta la función principal para llevar a cabo las operaciones.