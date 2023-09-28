# 2.
# En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
# cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
# es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
# cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta
# forma:
# Agus
# Manu
# Santi
# Lorena
# Maria
# La función tiene que devolver 5000
# c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
# de los nombres, se agregue también a Tomi.

dir_archivo = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\regalo.txt"

# a.
def mostrar_personas_que_quieren_participar(archivo_regalo):
    """
    Lee y muestra en la consola una lista de personas que desean participar en un regalo.
    Parámetros:
        - archivo_regalo: El nombre o ruta del archivo que contiene la lista de personas.
    """
    with open(archivo_regalo, "r") as file_regalo:
        for persona in file_regalo.readlines():
            # Elimina el carácter de salto de línea y muestra cada persona en la lista.
            print(persona.strip("\n"))


def dinero_total(archivo_regalo):
    """
    Calcula y devuelve el monto total de dinero necesario para un regalo, basado en el número de personas en la lista.
    Parámetros_
        - archivo_regalo: El nombre o ruta del archivo que contiene la lista de personas.
    Retorna:
        - El monto total de dinero necesario.
    """
    with open(archivo_regalo, "r") as file_regalo:
        DINERO_POR_PERSONA = 1000  # Monto de dinero por cada participante
        # Calcula el número de personas en la lista y multiplica por el monto por persona.
        return len(file_regalo.readlines()) * DINERO_POR_PERSONA
    

def participa_si(primer_nombre, segundo_nombre, archivo_regalo):
    """
    Comprueba si el segundo nombre está en la lista de participantes en un regalo,
    y si está, agrega el primer nombre a la lista.
    Parámetros:
        - primer_nombre: El primer nombre a agregar a la lista si el segundo nombre no está presente.
        - segundo_nombre: El nombre que se busca en la lista de participantes.
        - archivo_regalo: El nombre o ruta del archivo que contiene la lista de participantes.
    """
    with open(archivo_regalo, "r+") as file_regalo:
        # Comprueba si el segundo nombre está en la lista.
        if f"{segundo_nombre}\n" in file_regalo.readlines():
            file_regalo.write(f"\n{primer_nombre}")  # Agrega el primer nombre a la lista.
        else:
            print(f"{primer_nombre} no participa del cumpleaños de Sol")

# Prueba de las funciones definidas 🕵🏼‍♂️
participa_si("Tomi", "Santi", dir_archivo)
mostrar_personas_que_quieren_participar(dir_archivo) 
print(f"El dinero total con el que cuenta Ale para el regalo de Sol es ${dinero_total(dir_archivo)}")

# ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
# Solución alternativa usando try-except

def mostrar_personas_que_quieren_participar(archivo_regalo):
    """
    Muestra por pantalla los nombres de las personas que quieren participar en el regalo de cumpleaños de Sol.
    :param archivo_regalo: El nombre o ruta del archivo que contiene la lista de personas.
    :type archivo_regalo: str
    """
    try:
        with open(archivo_regalo, "r") as file_regalo:
            print("Personas que quieren participar en el regalo:")
            for persona in file_regalo.readlines():
                print(persona.strip("\n"))
    except FileNotFoundError:
        print("El archivo no se encontró. Verifica el nombre o la ubicación del archivo.")

def calcular_dinero_total(archivo_regalo):
    """
    Calcula y devuelve la cantidad total de dinero disponible para el regalo de cumpleaños de Sol.
    :param archivo_regalo: El nombre o ruta del archivo que contiene la lista de personas.
    :type archivo_regalo: str
    :return: La cantidad total de dinero disponible.
    :rtype: int
    """
    try:
        with open(archivo_regalo, "r") as file_regalo:
            DINERO_POR_PERSONA = 1000
            # Calcula el número de personas en la lista y multiplica por el monto por persona.
            return len(file_regalo.readlines()) * DINERO_POR_PERSONA
    except FileNotFoundError:
        print("El archivo no se encontró. Verifica el nombre o la ubicación del archivo.")
        return 0  # Si hay un error, devuelve 0 como cantidad total de dinero.

def agregar_tomi_si_santi_participa(archivo_regalo):
    """
    Si Santi está en la lista de nombres, agrega a Tomi a la lista.
    :param archivo_regalo: El nombre o ruta del archivo que contiene la lista de personas.
    :type archivo_regalo: str
    """
    try:
        with open(archivo_regalo, "r+") as file_regalo:
            lista_personas = file_regalo.readlines()
            if "Santi\n" in lista_personas:
                file_regalo.write("Tomi\n")
                print("Tomi ha sido agregado a la lista.")
    except FileNotFoundError:
        print("El archivo no se encontró. Verifica el nombre o la ubicación del archivo.")