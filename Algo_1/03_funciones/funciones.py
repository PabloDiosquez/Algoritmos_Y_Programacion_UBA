
def cuad(x: float):
    """Describe el cuadrado del número dado.
    """
    return x**2 

def raiz(x: float):
    """Describe la raíz cuadrada del número dado.
    Pre: El número dado debe ser >= 0.
    """
    return x**0.5 

def norma_vectorial(x: float, y: float):
    """Describe la norma del vector cuyas coordenadas están dadas por los dos números dados.
    """
    return raiz(cuad(x) + cuad(y))

print(norma_vectorial(3,6))

# -- Input ☂ -- 
# nombre = input("Nombre?: ")
# print(nombre)

def imprimir_norma():
    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    print("La norma vectorial es: ", norma_vectorial(x, y))

def a_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60 
    s = (segundos % 3600) % 60 
    return h, m, s 

hms = a_hms(3601)
h, m, s = a_hms(3601) # Desempaquetar 📦  

# Alcance de variables 🐣 

x = 'x'
y = 'y'
w = 'w'

def f(x):
    y = 'Y'
    print(w, x, y)
    z = 'Z'
    print(z)

f('X')
print(w, x, y)
# print(z) ➡ name 'z' is not defined

# constante global (no cambia su valor a lo largo de la ejecución del programa)

NOMBRE_APP = "AlgoApp"

def bienvenida(nombre: str):
    return f"Hola {nombre}! Te damos la bienvenida a {NOMBRE_APP}"

def adios(nombre: str):
    return f"Adiós {nombre}! Gracias por usar {NOMBRE_APP}"