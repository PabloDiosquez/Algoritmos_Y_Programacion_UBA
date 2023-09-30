# Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
# último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
# y la nota que sacó.
# a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
# notas.csv
# b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
# aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
# cantidad de alumnos aprobados (su nota es mayor a 4).

# a.
def guardar_notas(alumnos: dict, archivo):
    """
    Guarda las notas de los alumnos en un archivo CSV.
    Parámetros:
        - alumnos (list[dict]): Lista de diccionarios con los datos de los alumnos.
        Cada diccionario debe contener las claves 'nombre', 'apellido', 'dni' y 'nota'.
        - archivo (str): Ruta del archivo en el que se guardarán las notas.
    """
    with open(archivo, "w", encoding="UTF-8") as file_notas:
        for alumno in alumnos:
            nombre   = alumno["nombre"]
            apellido = alumno["apellido"]
            dni      = alumno["dni"]
            nota     = alumno["nota"]
            file_notas.write(f"{nombre};{apellido};{dni};{nota}\n") 

# Lista de alumnos 📚
alumnos = [
    {'nombre': 'Juan', 'apellido': 'Pérez', 'dni': '12345678', 'nota': 7},
    {'nombre': 'María', 'apellido': 'Gómez', 'dni': '87654321', 'nota': 5},
    {'nombre': 'Carlos', 'apellido': 'Rodríguez', 'dni': '56789012', 'nota': 6},
    {'nombre': 'Ana', 'apellido': 'López', 'dni': '98765432', 'nota': 4},
    {'nombre': 'Pedro', 'apellido': 'Martínez', 'dni': '23456789', 'nota': 8}
]

# Uso de la función definida anteriormente.
archivo = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\notas.csv"
guardar_notas(alumnos, archivo)

# b.
def cantidad_aprobados(archivo_alumnos):
    # Abrir el archivo CSV en modo lectura
    with open(archivo_alumnos, "r") as file_alumnos:
        alumnos = file_alumnos.readlines()
        # Inicializar contador de alumnos aprobados
        cantidad_aprobados = 0
        # Iterar sobre las filas de la lista de alumnos
        for alumno in alumnos:
            nombre, apellido, dni, nota = alumno.split(";")
            if int(nota) >= 7: cantidad_aprobados += 1
        return cantidad_aprobados

# Uso de la función definida anteriormente.
print(f"La cantidad de alumnos aprobados es {cantidad_aprobados(archivo)}")