# Objetos 🐱‍🏍

# Los objetos tienen estado y comportamiento, ya que los valores que tengan los atributos
# de una instancia determinan el estado actual de esa instancia, y los métodos definidos en una clase
# determinan cómo se va a comportar ese objeto.
from helpers import validar_número

class Punto:
    """
    Representación de un punto en el plano en
    coordenadas cartesianas (x, y)
    """
    def __init__(self, x, y):
        """
        Constructor de Punto. x e y deben ser numéricos.
        """
        self.x = validar_número(x)
        self.y = validar_número(y)

    # Todos los métodos de cualquier clase reciben como primer parámetro a la instancia sobre
    # la que está trabajando. Por convención, a ese primer parámetro se lo suele llamar self (que
    # podríamos traducir como yo mismo), pero puede llamarse de cualquier forma.

    def distancia(self, otro_punto):
        """
        Describe la distancia entre éste punto y el punto dado por parámetro.
        """
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return self.restar(otro_punto).norma()
    
    def restar(self, otro_punto):
        """
        Describe el punto que resulta de la resta entre los dos puntos.
        """
        return Punto(self.x - otro_punto.x, self.y - otro_punto.y)

    def norma(self):
        """
        Describe la norma del vector que va desde el origen hasta el punto.
        """
        return pow(pow(self.x, 2) + pow(self.y, 2), 0.5)

# Ejemplos

o = Punto(0, 0)
print(f"x: {o.x}")
print(f"y: {o.y}")

p = Punto(1,2)
print(p.distancia(o))