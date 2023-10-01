# Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el
# valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
# a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra?
# b. Realizarlo utilizando try/ except.

# a.
def get_int():
    """
    Esta función solicita al usuario que ingrese un número entero y valida la entrada.
    Retorna:
        int: El número entero ingresado por el usuario.
    """
    while True:
        input_usuario = input("Ingrese un número entero:\n")
        if input_usuario.isdigit():  # Cambio de isnumeric() a isdigit() para admitir enteros negativos
            numero_entero = int(input_usuario)
            return numero_entero
        
        print("Algo salió mal. Asegúrese de ingresar un número entero.")

# b.
def get_int_version2():
    """
    Esta función solicita al usuario que ingrese un número entero y maneja excepciones para validar la entrada.
    Retorna:
        int: El número entero ingresado por el usuario.
    """
    while True:
        try:
            input_usuario = input("Ingrese un número entero: ")
            numero_entero = int(input_usuario)
            return numero_entero
        except ValueError:
            print("Ocurrió un error 🤔. Asegúrese de ingresar un número entero válido.")


# Ejemplo de uso:
if __name__ == "__main__":
    # numero = get_int()
    numero = get_int_version2()
    print("Ha ingresado el número entero:", numero)