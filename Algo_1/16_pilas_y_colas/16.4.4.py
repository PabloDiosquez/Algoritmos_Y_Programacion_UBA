# Juego de Cartas
# a) Crear una clase Carta que contenga un palo y un valor.
# b) Crear una clase Solitario que permita apilar las cartas una arriba de otra, pero sólo
# permita apilar una carta si es de un número inmediatamente inferior y de distinto palo
# a la carta que está en el tope. Si se intenta apilar una carta incorrecta, debe lanzar una
# excepción.

from enum import Enum
from pila_bis import Pila

class Palo(Enum):
    "Modela el palo de una carta"
    BASTO  = 0
    COPAS  = 1
    ESPADA = 2
    ORO    = 3

class Carta:
    "Modela una carta que contenga un palo y un valor."
    def __init__(self, palo: Palo, valor: int):
        """
        Inicializa una carta con un palo y un valor.
        Parámetros:
            palo (Palo): El palo de la carta.
            valor (int): El valor de la carta.
        Pre:
            - 'valor' debe estar comprendido entre 1 y 12 inclusive.
        """
        if not 1 <= valor <= 12:
            raise ValueError("Los valores deben estar comprendidos entre 1 y 12 inclusive")
        self.palo  = palo 
        self.valor = valor 

    def obtener_palo(self):
        """
        Obtiene el palo de la carta.
        Retorna:
            - El palo de la carta (Palo).
        """
        return self.palo
    
    def obtener_valor(self):
        """
        Obtiene el valor de la carta.
        Retorna:
            - El valor de la carta (int).
        """
        return self.valor
    
class Solitario:
    "Modela el juego del Solitario"
    def __init__(self):
        "Inicializa una instancia de la clase Solitario"
        self.pila = Pila()

    def apilar_carta(self, carta: Carta):
        """
        Apila la carta dada si es de un número inmediatamente inferior y de distinto palo a la carta que está en el tope de la pila. Si intenta apilar una carta incorrecta lanza ValueError.
        Parámetros:
            - carta (Carta): La carta a apilar.
        """
        carta_al_tope = self.pila.ver_tope()
        # Comprobar si la carta es de distinto palo y un número inmediatamente inferior
        if (
            carta.palo.value == carta_al_tope.palo.value or 
            carta.valor != carta_al_tope.valor - 1
            ):
            raise ValueError("La carta no puede apilarse.")
        self.pila.apilar(carta)