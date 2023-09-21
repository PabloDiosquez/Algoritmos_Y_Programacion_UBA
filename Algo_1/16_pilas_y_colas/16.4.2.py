# Escribir las clases Impresora y Oficina que permita modelar el funcionamien-
# to de un conjunto de impresoras conectadas en red.

# Una impresora:
# • Tiene un nombre, y una capacidad máxima de tinta.
# • Permite encolar un documento para imprimir (recibiendo el nombre del documento).
# • Permite imprimir el documento que está al frente de la cola.
# – Si no hay documentos encolados, se muestra un mensaje informándolo.
# – Si no hay tinta suficiente, se muestra un mensaje informándolo.
# – En caso contrario, se muestra el nombre del documento, y se gasta 1 unidad de tinta.
# • Permite cargar el cartucho de tinta
# Una oficina:
# • Permite agregar una impresora
# • Permite obtener una impresora por nombre
# • Permite quitar una impresora por nombre
# • Permite obtener la impresora que tenga menos documentos encolados.
# Ejemplo:
# >>> o = Oficina()
# >>> o.agregar_impresora(Impresora('HP1234', 1))
# >>> o.agregar_impresora(Impresora('Epson666', 5))
# >>> o.impresora('HP1234').encolar('tp1.pdf')
# >>> o.impresora('Epson666').encolar('tp2.pdf')
# >>> o.impresora('HP1234').encolar('tp3.pdf')
# >>> o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
# >>> o.impresora('HP1234').imprimir()
# tp1.pdf impreso
# >>> o.impresora('HP1234').imprimir()
# No tengo tinta :(
# >>> o.impresora('HP1234').cargar_tinta()
# >>> o.impresora('HP1234').imprimir()
# tp3.pdf impreso

from cola_bis import Cola

class Impresora:
    """
    Modela una impresora. Una impresora tiene un nombre y una capacidad máxima de tinta.
    Invariante de representación:
        - El nombre de la impresora no debe ser vacío.
        - La capacidad máxima debe ser un número > 0.
    """

    def __init__(self, nombre: str, capacidad: int):
        """
        Crea una instancia de la clase Impresora.
        Parámetros:
            - nombre (str): El nombre de la impresora.
            - capacidad (int): La capacidad máxima de tinta de la impresora.
        """
        self.nombre     = nombre 
        self.capacidad  = capacidad
        self.tinta      = 0
        self.documentos = Cola()

    def cargar_tinta(self):
        """
        Carga el nivel de tinta de una impresora a su capacidad máxima.
        """
        self.tinta = self.capacidad

    def encolar(self, documento: str):
        """
        Encola un documento para imprimir.
        Parámetros:
            - documento (str): El documento a encolar en una impresora.
        """
        self.documentos.encolar(documento) 

    def imprimir(self):
        """
        Imprime el documento que está al frente de la cola de documentos de una impresora.
        Si no hay documentos encolados, describe un mensaje informándolo.
        Si no hay suficiente tinta, describe un mensaje informándolo.
        """
        if self.documentos.está_vacía():
            return "No hay documentos encolados"
        if self.tinta == 0:
            return "No tengo tinta"
        self.tinta -= 1
        return self.documentos.desencolar()
    
    
class Oficina:
    "Modela una oficina"
    def __init__(self):
        """
        """
        self.impresoras = {}

    def agregar_impresora(self, impresora):
        """
        """
        pass 

    def impresora(self, impresora):
        """
        """
        pass 

    def quitar_impresora(self, impresora: str):
        """
        """
        pass 

    def obtener_impresora_libre(self):
        """
        """
        pass 