# Escribir funciones que permitan encontrar:
# a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
# c), indicando si es un máximo o un mínimo.
# b) Las raíces (reales o complejas) de un polinomio de segundo grado.
# Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
# cero, ni calcular la raíz de un número negativo).
# c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
# Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la opera-
# ción.

from math import sqrt

# a) 
def _coordX_vertice(a: float, b: float, c: float) -> float:
    """ Describe la coordenada X del vértice de un polinomio de segundo grado dados los coeficientes
       'a', 'b' y 'c'.
    """
    return -b / 2*a 

def _coordY_vertice(a: float, b: float, c: float) -> float:
    """ Describe la coordenada Y del vértice de un polinomio de segundo grado dados los coeficientes 
        'a', 'b' y 'c'.
    """
    return a*pow(_coordX_vertice(a, b, c),2) + b*_coordX_vertice(a, b, c) + c

def vertice(a: float, b: float, c: float) -> float:
    """ Describe el máximo o el mínimo de un polinomio de segundo grado dados los coeficientes
       'a', 'b' y 'c', indicando si es un máximo o un mínimo.
    """ 
    return f"Mínimo: {_coordY_vertice(a, b, c)}" if a > 0 else f"Máximo: {_coordY_vertice(a, b, c)}"

# b) 
def _discriminante(a: float, b: float, c: float) -> float:
    """ Describe el discriminante de un polinomio de segundo grado dados los coefientes 'a', 'b'
        y 'c'.
    """
    return pow(b, 2) - 4*a*c 

def _tiene_raices_reales(a: float, b: float, c: float) -> float:
    """Indica si un polinomio de segundo grado tiene raíces reales dados los coeficientes 'a', 'b'
       y 'c'.
    """
    return _discriminante(a, b, c) >= 0

def raices_polinomio_segundo_grado(a: float, b: float, c: float):
    """
        Describe las raíces (reales o complejas ) de un polinomio de segundo grado dados los
        coeficientes 'a', 'b' y 'c'.
        Precondición: 
            -- El coeficiente cuadrático 'a' debe ser distinto de 0.
    """
    sqrt_disc = sqrt(abs(_discriminante(a, b, c)))
    if _tiene_raices_reales(a, b, c):
        return (-b + sqrt_disc)/2*a,  (-b - sqrt_disc)/ 2*a
    
    # Se define la unidad imaginaria ➡ i = 0 + 1j
    i = 1j
    return (-b + sqrt_disc*i)/2*a, (-b - sqrt_disc*i)/2*a 

#c) 
def interseccion_rectas(a1, b1, a2, b2):
    """Describe la intersección de las dos rectas cuyas pendientes y ordenadas al origen son dadas, en 
       caso de que sean rectas válidas. En caso contrario, describe un pequeño texto con el error ocurrido.
    """
    if _son_validas_las_rectas(a1, a2):
        return _coordX_interseccion(a1, b1, a2, b2), _coordY_interseccion(a1, b1, a2, b2)
    return "Algo salió mal 🥶.\nLas rectas dadas son paralelas o coincidentes."

def _coordX_interseccion(a1, b1, a2, b2):
    """Describe la coordenada X del punto de intersección de las dos rectas dadas.
       Precondición: Las rectas dadas no deben ser ni paralelas ni coincidentes.
    """
    return (b2-b1)/(a1-a2)

def _coordY_interseccion(a1, b1, a2, b2):
    """Describe la coordenada Y del punto de intersección de las dos rectas dadas.
       Precondición: Las rectas dadas no deben ser ni paralelas ni coincidentes.
    """
    return a1*_coordX_interseccion(a1, b1, a2, b2) + b1

def _son_validas_las_rectas(a1, a2):
    """ Indica si las rectas de pendientes dadas no son paralelas ni coincidentes.
    """
    return not a1-a2 == 0