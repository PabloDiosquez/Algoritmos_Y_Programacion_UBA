# 1.
# Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar
# la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la
# respuesta dada por el usuario en el archivo.
# Por ejemplo,s e tiene el archivo pregunta.txt que originalmente tiene:
# ¿Cómo estás hoy?
# Y el usuario de la respuesta: “¡Bien, porque me comí una hamburguesa!”
# Entonces el archivo debería quedar de la forma:
# ¿Cómo estás hoy?
# ¡Bien, porque me comí una hamburguesa!

def responder_pregunta(archivo):
    """
    Lee una pregunta desde un archivo, muestra la pregunta al usuario, 
    solicita una respuesta, y guarda la respuesta en el mismo archivo.
    Parámetros:
        - archivo: El nombre o ruta del archivo que contiene la pregunta.
    """    
    # Leer la pregunta del archivo
    with open(archivo, 'r+', encoding='utf-8') as archivo:
        pregunta = archivo.readline()
        # Mostrar la pregunta por pantalla
        print(f"Pregunta: {pregunta}")
        # Solicitar al usuario que ingrese una respuesta
        respuesta = input("Ingresa tu respuesta: ")
        # Agregar la respuesta al archivo con un salto de línea
        archivo.write(f"\n{respuesta}")
        # Confirmar que la respuesta se ha guardado exitosamente
        print("Respuesta guardada con éxito en el archivo.")

# Dirección del archivo de la pregunta
dir_archivo = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\pregunta.txt"
responder_pregunta(dir_archivo)