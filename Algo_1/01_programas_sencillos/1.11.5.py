from helpers import get_int, ejercicio
from math import pi, sqrt

def perimetro(base, altura):
    """Describe el perímetro de un rectángulo dada su base 
    y su altura.
    """
    return 2*base + 2*altura

ejercicio("1.11.5 - Perímetro de un rectángulo:", perimetro(3,5))

def area_rectangulo(lado1, lado2):
    """Describe el área de un rectángulo dadas su base y su altura."""
    return lado1*lado2

def area_rectangulo_coordenadas(x1, x2, y1, y2):
    """Describe el área de un rectángulo alineado con los ejes x e y, dadas
    sus coordenadas x1, x2, y1, y2.
    """
    lado_x = abs(x1-x2)
    lado_y = abs(y1-y2)
    return area_rectangulo(lado_x, lado_y)

ejercicio("1.11.5 - Área rectángulo alineado con los ejes:", area_rectangulo_coordenadas(1,2,4,7))

def perimetro_circulo(radio):
    """Describe el perímetro de un círculo dado su radio.
    """
    return round(2*pi*radio,2)

ejercicio("1.11.5 - Perímetro círculo de radio dado:", perimetro_circulo(3))

def area_circulo(radio):
    """Describe el área de un círculo de radio dado.
    """
    return round(pi*radio*radio, 2)

ejercicio("1.11.5 - Área círculo de radio dado:", area_circulo(3))

def volumen_esfera(radio):
    """Describe el volumen de una esfera de radio dado.
    """
    return round((4*pi*radio**3)/3, 2)

ejercicio("1.11.5 - Volumen esfera de radio dado:", volumen_esfera(3))

def hipotenusa(cateto1, cateto2):
    """Describe la hipotenusa de un triángulo rectángulo de catetos dados.
    """
    return round(sqrt(pow(cateto1,2) + pow(cateto2,2)), 2)

ejercicio("1.11.5 - Hipotenusa:", hipotenusa(2,3))