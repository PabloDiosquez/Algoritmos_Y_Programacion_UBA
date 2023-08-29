# Crear las clases Materia y Carrera, que se comporten según el siguiente ejem-
# plo:

# >>> analisis2 = Materia("61.03", "Análisis 2", 8)
# >>> fisica2 = Materia("62.01", "Física 2", 8)
# >>> algo1 = Materia("75.40", "Algoritmos 1", 6)
# >>> c = Carrera([analisis2, fisica2, algo1])
# >>> str(c)
# Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
# >>> c.aprobar("95.14", 7)
# ValueError: La materia 75.14 no es parte del plan de estudios
# >>> c.aprobar("75.40", 10)
# >>> c.aprobar("62.01", 7)
# >>> str(c)
# Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
# 75.40 Algoritmos 1 (10)
# 62.01 Física 2 (7)

from helpers import es_vacía

class Materia:
    "Representa una materia de la universidad. Ésta consta de un código, un nombre y una cantidad de créditos."

    def __init__(self, código: str, nombre: str, créditos: int):
        """
        """
        self.código   = código
        self.nombre   = nombre 
        self.créditos = créditos
        self.estado   = 0
        self.promedio = 0.0

    def __str__(self) -> str:
        """
        Describe una cadena de caracteres con la información de una materia.
        """
        return f"{self.código} {self.nombre} ({self.promedio})"

class Carrera:
    "Representa el plan de estudios de un alumno de la universidad."

    def __init__(self, materias: list[Materia]) -> None:
        """
        """
        self.materias = materias

    def aprobar(self, código: str, promedio: float):
        """
        """
        for materia in self.materias:
            if materia.código == código:
                materia.estado   = 1
                materia.promedio = promedio
        
    def __créditos(self):
        """
        Describe el total de créditos adquiridos de las materias aprobadas en una carrera.
        """
        total = 0
        for materia in self.materias:
            if not materia.estado == 0: total += materia.créditos
        return total
    
    def __promedio(self):
        """
        Describe el promedio de las materias aprobadas en una carrera. En caso de no haber materias aprobadas lanza ValueError.
        """
        if es_vacía(self.__materias_aprobadas()): raise ValueError("Aún no hay materias aprobadas") 

        total = 0
        for materia in self.__materias_aprobadas():
            total += materia.promedio
        return total / len(self.__materias_aprobadas())

    def __materias_aprobadas(self):
        """
        Describe una lista con las materias aprobadas de una carrera. En caso de no haber materias aprobadas lanza ValueError.
        """
        if es_vacía(self.materias): raise ValueError("Lista de materias vacía")
        aprobadas = []
        for materia in self.materias:
            if materia.estado != 0: aprobadas.append(materia)
        if es_vacía(aprobadas): raise ValueError("Aún no hay materias aprobadas")
        return aprobadas

    def __str__(self) -> str:
        """
        Describe una cadena de caracteres con la información de una carrera.
        """
        return f"Créditos: {self.__créditos()} -- Promedio: {self.__promedio()} -- Materias aprobadas: {[str(materia) for materia in self.__materias_aprobadas()]}"



def main():
    analisis2 = Materia("61.03", "Análisis 2", 8)
    fisica2   = Materia("62.01", "Física 2", 8)
    algo1     = Materia("75.40", "Algoritmos 1", 6)

    c = Carrera([analisis2, fisica2, algo1])
    # print(c)
# Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
    # c.aprobar("95.14", 7)
# ValueError: La materia 75.14 no es parte del plan de estudios
    c.aprobar("75.40", 10)
    c.aprobar("62.01", 7)
    print(c)
    

main()