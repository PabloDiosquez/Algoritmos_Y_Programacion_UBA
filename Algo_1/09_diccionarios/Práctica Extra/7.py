# 7.
maratonistas = {
    'Maratonista1': {
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
    'Maratonista2': {
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
}

def nombre_maratonista(maratonista):
    """
    Obtiene el nombre del maratonista a partir de su información.
    Parámetros:
        maratonista (dict): Un diccionario que representa al maratonista, debe contener la clave 'Nombre'.
    Retorna:
        str: El nombre completo del maratonista.
    Observación:
        KeyError: Si el diccionario 'maratonista' no contiene la clave 'Nombre'.
    """
    return maratonista['Nombre']

# print(sorted(maratonistas.items(), key=lambda x: nombre_maratonista(x[1])))

for maratonista in maratonistas:
    print(maratonistas[maratonista]['Nombre'])

print(sorted(maratonistas, key=lambda x: nombre_maratonista(maratonistas[x]))) # Lista de claves ordenadas alfabéticamente por nombre

ordenados = []
for clave in sorted(maratonistas, key=lambda x: nombre_maratonista(maratonistas[x])):
    ordenados.append((clave, maratonistas[clave]))

print(dict(ordenados))