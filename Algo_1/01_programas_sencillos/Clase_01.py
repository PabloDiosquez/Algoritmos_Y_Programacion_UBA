# Funciones ☂
def hola_grace():
    return "Hola Grace!"

def hola_alan():
    return "Hola Alan!"

def hola_(nombre: str) -> str:
    return f"Hola {nombre}!"

def cuad(numero: int) -> int:
    """Describe el cuadrado del número dado.
    """
    return numero*numero

def suma_5_cuadrados() -> int:
    """Describe la suma de los primeros 5 números naturales, 
    elevados al cuadrado.
    """
    total = 0
    # total = total + cuad(1)
    # total = total + cuad(2)
    # total = total + cuad(3)
    # total = total + cuad(4)
    # total = total + cuad(5)
    for i in range(6):
        total += cuad(i)
    return total

# print(suma_5_cuadrados())

def suma_n_cuadrados(n: int) -> int:
    """Describe la suma de los primeros n números naturales
    elevados al cuadrado.
    """
    total = 0
    for i in range(n+1):
        total += cuad(i)
    return total

print("Suma:", suma_n_cuadrados(100))

def modulo_de_un_vector(x, y) -> float:
    """Describe el módulo de un vector 2D.
       Argumentos:
            x: <float|int> coordenada de las abscisas.
            y: <float|int> coordenada de las ordenadas.
       Devuelve: (float) módulo de un vector.
    """
    return pow((pow(x,2) + pow(y,2)), 0.5)

# Algunas cuestiones para pensar... 🙊
def f():
    return "Hola" # 

x = f() # x ➡ "Hola"

def g():
    print("Hola") 

x = g() # x ➡ None

def f():
    8 
    abs(-10.432 + 33)
    "Holis"

f()