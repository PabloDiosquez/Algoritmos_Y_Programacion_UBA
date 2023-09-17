# Escribir una clase TorreDeControl que modele el trabajo de una torre de control
# de un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar
# tienen prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme
# al siguiente ejemplo:
# >>> torre = TorreDeControl()
# >>> torre.nuevo_arribo('AR156')
# >>> torre.nueva_partida('KLM1267')
# >>> torre.nuevo_arribo('AR32')
# >>> torre.ver_estado()
# Vuelos esperando para aterrizar: AR156, AR32
# Vuelos esperando para despegar: KLM1267
# >>> torre.asignar_pista()
# El vuelo AR156 aterrizó con éxito.
# >>> torre.asignar_pista()
# El vuelo AR32 aterrizó con éxito.
# >>> torre.asignar_pista()
# El vuelo KLM1267 despegó con éxito.
# >>> torre.asignar_pista()
# No hay vuelos en espera.

from cola_bis import Cola

class TorreDeControl:
    "Modela una Torre de Control de un aeropuerto con una pista de aterrizaje"

    def __init__(self):
        "Inicializa una instancia de la clase TorreDeControl"
        self.arribos   = Cola()
        self.despegues = Cola()

    def ver_estado(self):
        """
        Describe el estado de una torre de control.
        """
        if self.arribos.está_vacía() and self.despegues.está_vacía():
            return "No hay vuelos en espera."
        estado = ""
        if not self.arribos.está_vacía():
            estado += "Vuelos esperando para aterrizar: " + ", ".join(self.arribos.items)
        if not self.despegues.está_vacía():
            estado += "\nVuelos esperando para despegar: " + ", ".join(self.despegues.items)
        return estado 

    def nuevo_arribo(self, vuelo: str):
        """
        Encola el vuelo 'vuelo' en arribos.
        Parámetros:
            - vuelo (str): El vuelo que está esperando para arribar al aeropuerto.
        """
        self.arribos.encolar(vuelo) 

    def nueva_partida(self, vuelo: str):
        """
        Encola el vuelo 'vuelo' en partidas.
        Parámetros:
            - vuelo (str): El vuelo que está esperando para partir del aeropuerto.
        """
        self.despegues.encolar(vuelo)

    def asignar_pista(self):
        """
        Asigna una pista libre del aeropuerto al vuelo correspondiente.
        Invariante:
            - Los aviones que están esperando para aterrizar tienen prioridad sobre los que están esperando para despegar.
        """
        if not self.arribos.está_vacía():
            arribo = self.arribos.desencolar()
            return f"El vuelo {arribo} aterrizó con éxito"
        if not self.despegues.está_vacía():
            despegue = self.despegues.desencolar()
            return f"El vuelo {despegue} despegó con éxito"
        return "No hay vuelos en espera." 
    
def main():
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    print(torre.ver_estado())
    # Vuelos esperando para aterrizar: AR156, AR32
    # Vuelos esperando para despegar: KLM1267
    print(torre.asignar_pista())
    # El vuelo AR156 aterrizó con éxito.
    print(torre.asignar_pista())
    # El vuelo AR32 aterrizó con éxito.
    print(torre.asignar_pista())
    # El vuelo KLM1267 despegó con éxito.
    print(torre.asignar_pista())
    # No hay vuelos en espera.

main()