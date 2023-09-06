# a.
def crear_persona(nombre, dni, edad, curso):
    """
    Crea un diccionario que representa a una persona.
    Parámetros:
        nombre (str): El nombre de la persona.
        dni (str): El número de identificación de la persona.
        edad (int): La edad de la persona.
        curso (dict): Un diccionario que representa el curso al que está inscrito.
    Retorna:
        dict: Un diccionario con los datos de la persona.
    """
    return {
        'Nombre': nombre,
        'DNI'   : dni,
        'Edad'  : edad,
        'Curso' : curso 
    }

# b.
def crear_curso(año, división, orientación):
    """
    Crea un diccionario que representa un curso.
    Parámetros:
        año (int): El año del curso.
        división (str): La división del curso.
        orientación (str): La orientación del curso.
    Retorna:
        dict: Un diccionario con los datos del curso.
    """
    return {
        'Año'        : año,
        'División'   : división,
        'Orientación': orientación
    }

# c.
def estudiante_más_viejo(estudiantes):
    """
    Encuentra al estudiante más viejo en una lista de estudiantes.
    Parámetros:
        estudiantes (list): Una lista de diccionarios que representan a los estudiantes.
    Retorna:
        dict: Un diccionario que representa al estudiante más viejo.
    """
    if not estudiantes: raise ValueError("Lista de estudiantes vacía")

    estudiante_más_viejo_al_momento = estudiantes[0]
    mayor_edad_al_momento           = estudiante_más_viejo_al_momento['Edad']
    # estudiantes_restantes = estudiantes[1:]

    for estudiante in estudiantes[1:]:
        estudiante_más_viejo_al_momento = estudiante_más_viejo_entre(estudiante_más_viejo_al_momento, estudiante)
    return estudiante_más_viejo_al_momento

def estudiante_más_viejo_entre(estudiante1, estudiante2):
    """
    Describe al estudiante más viejo entre los dos estudiantes dados.
    """
    if estudiante1['Edad'] > estudiante2['Edad']:
        return estudiante1
    return estudiante2