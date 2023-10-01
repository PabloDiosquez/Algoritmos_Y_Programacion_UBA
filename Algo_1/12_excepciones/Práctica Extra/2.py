# Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para
# calcular el producto entre dos números enteros ingresados.

# Función Auxiliar 🐱‍🏍
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


def producto_de_enteros():
    """
    Esta función calcula el producto de dos números enteros ingresados por el usuario.
    Retorna:
        int: El producto de los dos números enteros ingresados.
    """
    return get_int_version2() * get_int_version2()

# Ejemplo de uso:
if __name__ == "__main__":
    print("El producto de los enteros dados es:", producto_de_enteros())