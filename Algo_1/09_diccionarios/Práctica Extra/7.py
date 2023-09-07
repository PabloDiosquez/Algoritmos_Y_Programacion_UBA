# 7.
# a.
maratonistas = [
    {
        'Nombre': 'Lio Messi',
        'DNI': 12345678,
        'Maratones': [
            {
                'Nombre_maratón': 'Maratón de Buenos Aires',
                'Año': 2021,
                'Puesto': 3,
                'Tiempo': '1:00:43'
            },
            {
                'Nombre_maratón': 'Maratón de Córdoba',
                'Año': 2019,
                'Puesto': 4,
                'Tiempo': '1:12:21'
            },
            {
                'Nombre_maratón': 'Maratón de Mar del Plata',
                'Año': 2020,
                'Puesto': 2,
                'Tiempo': '1:03:21'
            }
        ]
    },
    {
        'Nombre': 'Dibu Martínez',
        'DNI': 87654321,
        'Maratones': [
            {
                'Nombre_maratón': 'Maratón de Buenos Aires',
                'Año': 2021,
                'Puesto': 6,
                'Tiempo': '0:12:22'
            },
            {
                'Nombre_maratón': 'Maratón de Mar del Plata',
                'Año': 2020,
                'Puesto': 1,
                'Tiempo': '0:30:21'
            }
        ]
    }
]

# b.

def nombre_maratonista(maratonista):
    """
    Obtiene el nombre del maratonista a partir de su información.
    Parámetros:
        - maratonista (dict): Un diccionario que representa al maratonista. 
    Precondición:
        - El diccionario debe contener la clave 'Nombre'.
    Retorna:
        - El nombre completo del maratonista (str).
    """
    return maratonista['Nombre']

def ordenar_maratonistas(maratonistas):
    """
    Describe una nueva lista de maratonistas ordenada alfabéticamente por sus nombres.
    Parámetros:
        - maratonistas (list[dict]): La lista de maratonistas a partir de la cual se creará la nueva lista ordenada.
    Retorna:
        - Una lista de maratonistas ordenada según los nombres de los mismos.
    Observación:
        - Si la lista de maratonistas dada está vacía, lanza ValueError.  
    """
    if not maratonistas: raise ValueError('La lista de maratonistas está vacía')
    maratonistas_ordenados = []
    for maratonista in sorted(maratonistas, key=lambda maratonista: nombre_maratonista(maratonista)):
        maratonistas_ordenados.append(maratonista)
    return maratonistas_ordenados

# c. 
def ordenar_maratones_según_tiempo(maratonista):
    """
    Describe una nueva lista de maratones ordenada por el tiempo que el maratonista dado tardó en completarlas, de menor a mayor.
    Parámetros: 
        - maratonista (dict): El maratonista según el cual se describe la nueva lista ordenada de maratones.
    Precondición:
        - El diccionario debe contener la clave 'Maratones'.
    Retorna:
        - Una lista de maratones ordenada según los tiempos de finalización de cada una del maratonista dado.
    """
    maratones_ordenadas = []
    for maratón in sorted(maratonista['Maratones'], key=lambda maratón: maratón['Tiempo']):
        maratones_ordenadas.append(maratón)
    return maratones_ordenadas