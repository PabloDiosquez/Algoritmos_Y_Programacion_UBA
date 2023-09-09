# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
# rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

# b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
# tos.

# c) Modificar el programa anterior para que después de cada intento agregue una pausa
# cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
# ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

def adivinar_contraseña():
    "Pide al usuario que ingrese una contraseña y no lo deja continuar hasta ingresarla correctamente."
    # Define la contraseña correcta como una constante.
    CONTRASEÑA = "Francia2"
    # Solicita al usuario ingresar una contraseña.
    contraseña = input("Pass: ")
    # Comienza un bucle mientras la contraseña ingresada no sea igual a la contraseña correcta.
    while contraseña != CONTRASEÑA:
        # Imprime un mensaje de error.
        print("Contraseña incorrecta. Intente de nuevo")
        # Solicita al usuario ingresar la contraseña nuevamente.
        contraseña = input("Pass: ")
    # Cuando la contraseña ingresada es correcta, imprime un mensaje de acceso otorgado.
    print("Acceso otorgado 🖖🏼")

# Llamada a la función para ejecutar el programa.
adivinar_contraseña()