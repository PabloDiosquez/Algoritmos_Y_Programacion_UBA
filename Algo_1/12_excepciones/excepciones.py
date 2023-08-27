# Errores de programación

# def cuad(n)
#     """
#     """
#     return n ** n 

# n = input("Ingrese un número: ")
# print(n + " al cuadrado es" + cuad(5))

# Error de ejecución ➡ Excepción 💥

# def f(x, y):
#     return x / y 

# def g(x, y):
#     return f(x, y)

# z = g(5, 0) ➡ ZeroDivisionError

# Propagación de excepciones 💣

def normalizar(x, y):
    norma = (x**2 + y**2)**0.5
    print("Antes")
    xn = x / norma
    yn = y / norma
    print("Después")
    return xn, yn 

def main():
    try:
        x = float(input("x: "))
        y = float(input("y: "))
        print(normalizar(x,y))
    except ZeroDivisionError:
        print("No se puede normalizar al vector (0, 0)")
    except ValueError as ex:
        print(f"Asegúrese de ingresar números - {ex}")
    except:
        print("Ocurrió algo inesperado")
    finally:
        print("Adiós ☂")

# main()

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

# pedir_entero()

def archivo():
    f = None
    try:
        f = open('archivo.txt')
        s = f.readline()
        print(s)
    except:
        print('Algo salió mal')
    finally:
        if f is not None:
            f.close()

# archivo()

# Validaciones: precondiciones 🐸

def promedio(L):
    # assert len(L) > 0, "La lista no debe ser vacía"
    if len(L) == 0:
        raise ValueError("La lista dada no debe ser vacía")
    return sum(L) / len(L)

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

def pedir_número():
    while True:
        número = input("Número: ")
        try:
            return float(número)
        except ValueError:
            continue 

# pedir_número()