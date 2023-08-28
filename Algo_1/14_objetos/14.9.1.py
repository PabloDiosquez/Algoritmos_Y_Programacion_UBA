# Mejorar la clase Rectangulo, agregando métodos para calcular las dimensiones
# alto y ancho, y las coordenadas del punto central.

from objetos import Punto

class Rectángulo:
    """
    Representa un rectángulo de lados paralelos a los ejes en el plano cartesiano. 
    """

    def __init__(self, noroeste: Punto, sudeste: Punto) -> None:
        """
        """
        self.noroeste = noroeste
        self.sudeste  = sudeste

    def alto(self):
        """
        Describe la altura de un rectángulo.
        """
        self.noroeste.y - self.sudeste.y  

    def ancho(self):
        """
        Describe el ancho de un rectángulo.
        """
        self.sudeste.x - self.noroeste.x 

    def área(self):
        """
        Describe el área del rectángulo dado.
        """
        return self.alto() * self.ancho()

    def coords_punto_central(self):
        """
        Describe las coordenas del punto central de un rectángulo.
        """
        xc = (self.sudeste.x + self.noroeste.x) / 2  
        yc = (self.noroeste.y + self.sudeste.y) / 2 
        return Punto(xc, yc)