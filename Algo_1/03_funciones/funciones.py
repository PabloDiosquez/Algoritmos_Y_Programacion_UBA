
def cuad(x):
    """Describe el cuadrado del número dado.
    """
    return x**2 

def raiz(x):
    """Describe la raíz cuadrada del número dado.
    Pre: El número dado debe ser >= 0.
    """
    return x**0.5 

def norma_vectorial(x,y):
    """Describe la norma del vector cuyas coordenadas están dadas por los dos números dados.
    """
    return raiz(cuad(x) + cuad(y))