# Escribir una clase Caja para representar cuánto dinero hay en una caja de un
# negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
# de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
# 5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
# >>> c = Caja({500: 6, 300: 7, 2: 4})
# ValueError: Denominación "300" no permitida
# >>> c = Caja({500: 6, 100: 7, 2: 4})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
# >>> c.agregar({250: 2})
# ValueError: Denominación "250" no permitida
# >>> c.agregar({50: 2, 2: 1})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
# >>> c.quitar({50: 3, 100: 1})
# ValueError: No hay suficientes billetes de denominación "50"
# >>> c.quitar({50: 2, 100: 1})
# 200
# >>> str(c)
# 'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

from helpers import validar_denominaciones, sumar_denominaciones, agregar_par_clave_valor, validar_denominaciones_específicas

class Caja:
    """
    Representa cuánto dinero hay en una caja de un negocio.
    """

    def __init__(self, denominaciones: dict):
        """
        Crea una instancia de la clase Caja usando las denominaciones dadas.
        Precondiciones:
            - Las denominaciones permitidas son 1, 2, 5, 10, 20, 50, 100, 200, 500 y 1000 pesos.
        """
        self.denominaciones = validar_denominaciones(denominaciones)

    def __str__(self) -> str:
        """
        Describe el dniero total de una caja.
        """
        return f"Caja {self.denominaciones} -- Total: {sumar_denominaciones(self.denominaciones)}"
    
    def agregar(self, denominación: dict):
        """
        Agrega a una caja el número de billetes de la denominación dada. Lanza ValueError si la denominación es incorrecta.
        """
        return Caja(agregar_par_clave_valor(self.denominaciones, validar_denominaciones(denominación)))
    
    def quitar(self, denominaciones: dict):
        """
        Describe el dinero total de una caja luego quitar las cantidades de cada denominación dada. En caso de no existir determinada denominación o de no haber suficiente dinero lanza ValueError.
        """
        denominaciones = validar_denominaciones_específicas(self.denominaciones, denominaciones)
        for denominación in denominaciones.keys():
            if self.denominaciones[denominación] < denominaciones[denominación]:
                raise ValueError(f"No hay suficientes billetes de denominación {denominación}")
            self.denominaciones[denominación] -= denominaciones[denominación]
        return sumar_denominaciones(self.denominaciones)
    
# c = Caja({500: 6, 300: 7, 2: 4})
# c = Caja({100: 7, 2: 4, 50: 3})
# print(c)
# print(c.quitar({50: 2, 100: 1}))
# print(c)