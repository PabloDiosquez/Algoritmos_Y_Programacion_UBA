
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