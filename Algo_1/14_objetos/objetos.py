# Objetos 🐱‍🏍

# Los objetos tienen estado y comportamiento, ya que los valores que tengan los atributos
# de una instancia determinan el estado actual de esa instancia, y los métodos definidos en una clase
# determinan cómo se va a comportar ese objeto.
from helpers import validar_número, validar_cadena_no_vacía

# -----------------------------
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
    
    # Métodos especiales 🪓
    # Así como el constructor, __init__, existen diversos métodos especiales que, si están definidos en nuestra clase, Python los llamará por nosotros cuando se utilice una instancia en situaciones particulares.

    def __str__(self) -> str:
        """
        Describe la representanción del punto como cadena de texto.
        """
        return f"{(self.x, self.y)}"
    
    def __repr__(self) -> str:
        """
        Devuelve la representación formal del Punto como
        cadena de texto.
        """
        return f"Punto: {(self.x, self.y)}"
    
    def __add__(self, otro_punto):
        """
        Describe el punto que resulta de sumar los dos puntos.
        """
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)
    
    def __sub__(self, otro_punto):
        """
        Describe el punto que resulta de restar los dos puntos.
        """
        return Punto(self.x - otro_punto.x, self.y - otro_punto.y)
    
    def __eq__(self, otro_punto: object) -> bool:
        """
        Indica si dos puntos son iguales.
        """
        return self.x == otro_punto.x and self.y == otro_punto.y
    
    def desplazar(self, dx, dy):
        """
        Desplaza el punto según 'dx' y 'dy'.
        """
        self.x += dx
        self.y += dy

# -----------------------------
class Rectángulo:
    """
    Representación de un rectángulo en el plano cartesiano de lados paralelos a los ejes cartesianos.
    """

    def __init__(self, noroeste: Punto, sudeste: Punto):
        """
        Crea un Rectangulo a partir de los puntos correspondientes a las
        esquinas superior izquierda e inferior derecha.
        """
        self.noroeste = noroeste
        self.sudeste  = sudeste

# -----------------------------
class Hotel:
    """
    Representa un hotel: sus atributos son:
    nombre, ubicacion, puntaje y precio.
    """

    def __init__(self, nombre, ubicación, puntaje, precio):
        """
        Crea un Hotel.
        nombre y ubicación deben ser cadenas no vacías;
        puntaje y precio son números.
        """
        self.nombre    = validar_cadena_no_vacía(nombre)
        self.ubicación = validar_cadena_no_vacía(ubicación)
        self.puntaje   = validar_número(puntaje)
        self.precio    = validar_número(precio)
    
    def __str__(self) -> str:
        """
        Conversión a cadena de texto.
        """
        return f"{self.nombre} de {self.ubicación} -- Puntaje: {self.puntaje} -- Precio: ${self.precio}"
    
    def ratio(self):
        """
        Describe la relación calidad-precio de un hotel.
        """
        return 10*(pow(self.puntaje, 2))/(self.precio)
    
    def __lt__(self, otro_hotel):
        """
        Indica si el hotel que recibe el mensaje tiene menor ratio que el hotel dado.
        """
        return self.ratio() < otro_hotel.ratio()
    
    def precio(self):
        """
        Describe el precio de un hotel.
        """
        return self.precio
    
# Una pequeña prueba...

hotel1 = Hotel("Hotel 1* normal", "MDQ", 1, 10)
hotel2 = Hotel("Hotel 2* normal", "MDQ", 2, 40)
hotel3 = Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
hotel4 = Hotel("Hotel vale la pena" ,"MDQ", 4, 130)
hoteles = [hotel1, hotel2, hotel3, hotel4]

hoteles.sort()
for hotel in hoteles:
    print(hotel)

print()
hoteles.sort(key=Hotel.precio)
for hotel in hoteles:
    print(hotel)