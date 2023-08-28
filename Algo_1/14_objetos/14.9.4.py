# a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
# asignan en el constructor, y se imprimen como X/Y en el método __str__.
# b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
# con la suma de ambas.
# c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
# con el producto de ambas.
# d) Crear un método simplificar que modifica la fracción actual de forma que los valores
# del dividendo y divisor sean los menores posibles.

from helpers import validar_número_distinto_de_cero
from math import gcd

class Fraccion:
    """
    Representa una fracción.
    """

    def __init__(self, dividendo, divisor):
        """
        Crea una instancia de la clase Fraccion.

        Parámetros:
        - dividendo: El numerador de la fracción.
        - divisor: El denominador de la fracción.

        Precondiciones:
            - 'divisor' debe ser distinto de 0.
        """
        self.dividendo = dividendo
        self.divisor   = validar_número_distinto_de_cero(divisor)

    def __str__(self) -> str:
        """
        Describe una representación en cadena de la fracción en el formato X/Y.
        """ 
        return f"{self.dividendo}/{self.divisor}"
    
    def __add__(self, otra_fracción):
        """
        Describe una nueva fracción que resulta de la suma de dos fracciones.
        """
        dividendo = self.dividendo * otra_fracción.divisor + self.dividendo * otra_fracción.dividendo
        divisor   = self.divisor * otra_fracción.divisor
        return Fraccion(dividendo, divisor)
    
    def __mul__(self, otra_fracción):
        """
        Describe una nueva fracción que resulta de la multiplicación de dos fracciones.
        """
        return Fraccion(self.dividendo*otra_fracción.dividendo, self.divisor*otra_fracción.divisor)
    
    def simplificar(self):
        """
        Describe una fracción que resulta de simplificar la fracción actual de forma que los valores del dividendo y divisor sean los menores posibles.
        """
        mcd = gcd(self.dividendo, self.dividendo)
        dividendo = self.dividendo // mcd
        divisor   = self.divisor   // mcd
        return Fraccion(dividendo, divisor)