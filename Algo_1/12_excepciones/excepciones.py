
# try:
# # aquí ponemos el código que puede lanzar excepciones
# except IOError:
# # entrará aquí en caso que se haya producido
# # una excepción IOError
# except ZeroDivisionError:
# # entrará aquí en caso que se haya producido
# # una excepción ZeroDivisionError
# except:
# # entrará aquí en caso que se haya producido
# # una excepción que no corresponda a ninguno
# # de los tipos especificados en los casos previos

def factorial(n):
    """Calcula el factorial de n.
    Pre: n debe ser un entero, mayor igual a 0
    Post: se devuelve el valor del factorial pedido
    """
    assert n >= 0, "n debe ser mayor igual a 0"
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def pedir_entero():
    """Solicita un valor entero y lo devuelve.
    Si el valor ingresado no es entero, da 5 intentos para ingresarlo
    correctamente, y de no ser así, lanza una excepción."""
    intentos = 0
    while intentos < 5:
        valor = input("Ingrese un número entero: ")
        try:
        return int(valor)
        except ValueError:
        print(f"{valor!r} no es un número entero.")
        intentos += 1
        raise ValueError("Valor incorrecto ingresado en 5 intentos")