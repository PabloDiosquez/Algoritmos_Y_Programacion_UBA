# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
# rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
# tos.
# c) Modificar el programa anterior para que después de cada intento agregue una pausa
# cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
# ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

# a.
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
# adivinar_contraseña()

# b.
def adivinar_contraseña():
    "Solicita al usuario ingresar una contraseña y permite un número limitado de intentos."
    # Define la contraseña correcta como una constante.
    CONTRASEÑA = "Francia2"
    # Establece el número máximo de intentos permitidos.
    intentos_permitidos = 3
    # Solicita al usuario ingresar la contraseña y muestra el número de intentos restantes.
    contraseña = input(f"Pass (Restan {intentos_permitidos} intentos): ")
    # Inicia un bucle while que se ejecutará mientras la contraseña ingresada sea incorrecta.
    while contraseña != CONTRASEÑA:
        # Reduce el contador de intentos permitidos en 1.
        intentos_permitidos -= 1
        # Verifica si se agotaron los intentos permitidos.
        if intentos_permitidos == 0:
            print("Intentos agotados. Pruebe de nuevo luego de un tiempo ⌛")
            return  # Sale de la función si se agotan los intentos.
        # Muestra un mensaje de error y solicita al usuario ingresar la contraseña nuevamente.
        print("Contraseña incorrecta. Intente de nuevo")
        contraseña = input(f"Pass (Restan {intentos_permitidos} intentos): ")
    # Cuando la contraseña ingresada es correcta, imprime un mensaje de acceso otorgado.
    print("Acceso otorgado 🖖🏼")

# Llamada a la función para ejecutar el programa.
# adivinar_contraseña()

# c.
def adivinar_contraseña():
    """
    Solicita al usuario ingresar una contraseña y permite un número limitado de intentos.
    Esta función tiene como objetivo solicitar al usuario una contraseña específica y permite un número limitado
    de intentos para adivinarla. Si el usuario ingresa la contraseña correcta, se le otorga acceso. Si agota
    todos los intentos permitidos, se le informa que debe esperar un tiempo antes de intentarlo nuevamente.
    Observaciones sobre las variables:
        CONTRASEÑA (str): La contraseña que el usuario debe adivinar para obtener acceso.
        intentos_permitidos (int): El número máximo de intentos permitidos antes de bloquear el acceso.
        pausa (int): El valor inicial de pausa para introducir un retraso entre intentos.

    Ejemplo:
        >>> adivinar_contraseña()
        Pass (Restan 4 intentos)  # Suponiendo que el usuario ingresa una contraseña incorrecta
        Pass (Restan 3 intentos)  # Suponiendo que el usuario ingresa una contraseña incorrecta nuevamente
        Pass (Restan 2 intentos)  # Suponiendo que el usuario ingresa una contraseña incorrecta nuevamente
        Pass (Restan 1 intentos)  # Suponiendo que el usuario ingresa una contraseña incorrecta nuevamente
        Intentos agotados. Pruebe de nuevo luego de un tiempo ⌛  # Se agotaron los intentos permitidos
    """
    from time import sleep
    # La contraseña que el usuario debe adivinar para obtener acceso
    CONTRASEÑA = "Francia2"
    # El número máximo de intentos permitidos antes de bloquear el acceso
    intentos_permitidos = 4
    # El valor inicial de pausa para introducir un retraso entre intentos
    pausa = 1
    # Bucle que solicita la contraseña y verifica los intentos
    while True:
        contraseña = input(f"Pass (Restan {intentos_permitidos} intentos): ")
        if contraseña == CONTRASEÑA:
            break
        intentos_permitidos -= 1
        if intentos_permitidos == 0:
            print("Intentos agotados. Pruebe de nuevo luego de un tiempo ⌛")
            return 
        # Introduce un retraso entre intentos
        sleep(pausa)       
        pausa += 1
    print("Acceso otorgado 🖖🏼")

# adivinar_contraseña()

# d.
def adivinar_contraseña():
    """
    Solicita al usuario ingresar una contraseña y permite un número limitado de intentos.
    Esta función tiene como objetivo solicitar al usuario una contraseña específica y permite un número limitado
    de intentos para adivinarla. Si el usuario ingresa la contraseña correcta, se le otorga acceso y se decribe True. Si agotan todos los intentos permitidos, se le informa que debe esperar un tiempo antes de intentarlo nuevamente describiendo False.
    Retorna:
        bool: True si el usuario adivina la contraseña correctamente, False si se agotan los intentos.
    """
    from time import sleep
    # La contraseña que el usuario debe adivinar para obtener acceso
    CONTRASEÑA = "Francia2"
    # El número máximo de intentos permitidos antes de bloquear el acceso
    intentos_permitidos = 4
    # El valor inicial de pausa para introducir un retraso entre intentos
    pausa = 1
    # Bucle que solicita la contraseña y verifica los intentos
    while True:
        contraseña = input(f"Pass (Restan {intentos_permitidos} intentos): ")
        if contraseña == CONTRASEÑA:
            break
        intentos_permitidos -= 1
        if intentos_permitidos == 0:
            print("Intentos agotados. Pruebe de nuevo luego de un tiempo ⌛")
            return False 
        # Introduce un retraso entre intentos
        sleep(pausa)       
        pausa += 1
    print("Acceso otorgado 🖖🏼")
    return True 