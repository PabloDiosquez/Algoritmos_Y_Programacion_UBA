# Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
# último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
# y la nota que sacó.
# a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
# notas.csv
# b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
# aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
# cantidad de alumnos aprobados (su nota es mayor a 4).

def guardar_nota(alumno: dict):
    """Guarda los datos del alumno en un archivo CSV llamado 'notas.csv'."""
    # Convierte los valores del diccionario de alumno a una lista de strings
    datos_alumno = [str(dato) for dato in list(alumno.values())]
    # Abre el archivo 'notas.csv' en modo de agregar ('a') y codificación UTF-8
    with open('archivos/notas.csv', 'a', encoding='UTF-8') as archivo_notas:
        # Escribe los datos del alumno separados por ';' y agrega un salto de línea
        archivo_notas.write(f'{";".join(datos_alumno)}\n')
        print('Alumno agregado con éxito en "notas.csv"')

def obtener_total_aprobados() -> int:
    """Lee 'notas.csv' y devuelve la cantidad de alumnos aprobados."""
    # Abre el archivo 'notas.csv' en modo de lectura ('r') y codificación UTF-8
    with open('archivos/notas.csv', 'r', encoding='UTF-8') as archivo_notas:
        # Lee cada línea, separa los datos por ';' y crea una lista de listas de datos de alumnos
        alumnos = [alumno.strip().split(';') for alumno in archivo_notas.readlines()]
        # Usa la función 'está_aprobado' para filtrar los alumnos aprobados y cuenta su cantidad
        return len(list(filter(está_aprobado, alumnos)))

def está_aprobado(datos_alumno: list) -> bool:
    """Verifica si el alumno tiene una nota igual o mayor a 4."""
    # Comprueba si la nota del alumno (último elemento en la lista de datos) es mayor o igual a 4
    return float(datos_alumno[-1]) >= 4

def main():
    """Función principal que simula el ingreso de datos de alumnos y muestra el total de aprobados."""
    # Lista de alumnos con sus datos
    alumnos = [
        {
            'nombre': 'Lio',
            'apellido': 'Messi',
            'dni': 123456,
            'nota': 9,
        },
        {
            'nombre': 'Cristiano',
            'apellido': 'Ronaldo',
            'dni': 234567,
            'nota': 8.5,
        },
        {
        'nombre': 'Neymar',
        'apellido': 'Jr.',
        'dni': 345678,
        'nota': 8.7
    },
    {
        'nombre': 'Kylian',
        'apellido': 'Mbappé',
        'dni': 456789,
        'nota': 8.9
    },
    {
        'nombre': 'Robert',
        'apellido': 'Lewandowski',
        'dni': 567890,
        'nota': 8.4
    },
    {
        'nombre': 'Kevin',
        'apellido': 'De Bruyne',
        'dni': 678901,
        'nota': 8.6
    },
    {
        'nombre': 'Luka',
        'apellido': 'Modric',
        'dni': 789012,
        'nota': 8.8
    }
    ]

    # Itera sobre la lista de alumnos y guarda sus datos usando la función 'guardar_nota'
    for alumno in alumnos:
        guardar_nota(alumno)
    # Imprime el total de alumnos aprobados utilizando la función 'obtener_total_aprobados'
    print(f'Total alumnos aprobados: {obtener_total_aprobados()}')

# Llamada a la función principal para ejecutar el código
main()