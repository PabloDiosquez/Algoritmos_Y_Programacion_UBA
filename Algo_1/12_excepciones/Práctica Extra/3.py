# Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el
# cociente entre ellos.
# AYUDA: Considerar que el usuario podría brindar un valor no numérico o un divisor nulo.

def obtener_numero(mensaje):
    """
    Esta función solicita al usuario un número y maneja excepciones para validar la entrada.
    Parámetros:
        - mensaje (str): El mensaje para solicitar la entrada al usuario.
    Retorna:
        - float: El número ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Ocurrió un error 🤔. Asegúrese de ingresar un número válido.")

def calcular_cociente(dividendo, divisor):
    """
    Esta función calcula el cociente entre un dividendo y un divisor.
    Parámetros:
        - dividendo (float): El dividendo.
        - divisor (float): El divisor.
    Retorna:
        - float: El cociente calculado.
    """
    try:
        return dividendo // divisor
    except ZeroDivisionError:
        print("No se puede dividir por 0 🙉")

if __name__ == "__main__":
    print("Calculadora de cociente")
    dividendo = obtener_numero("Ingrese el dividendo: ")
    divisor   = obtener_numero("Ingrese el divisor: ")
    resultado = calcular_cociente(dividendo, divisor)
    if isinstance(resultado, int):
        print("El cociente es:", resultado)