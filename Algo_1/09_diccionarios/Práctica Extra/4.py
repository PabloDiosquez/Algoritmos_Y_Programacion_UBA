# 4.

def mejores_películas(películas):
    """
    Filtra las películas del diccionario que tienen una puntuación mayor a 7.
    Parámetros:
        - diccionario_peliculas (list[dict]): Una lista de diccionarios donde cada diccionario
            representa una película con las claves 'nombre', 'año' y 'puntuacion'.
    Retorna:
        - list[dict]: Una nueva lista de diccionarios que solo contiene las películas
            con una puntuación mayor a 7.
    """
    PUNTUACIÓN_ELEGIDA = 7
    if not películas: raise ValueError("Lista de películas vacía")
    mejores_películas = []
    for película in películas:
        if película['puntaje'] > PUNTUACIÓN_ELEGIDA:
            mejores_películas.append(película)
    return mejores_películas

def agregar_película(películas, nombre, año, puntuación):
    """
    Agrega una película al diccionario de películas.
    Parámetros:
        películas (list of dict): Una lista de diccionarios que representa las películas.
        nombre (str): El nombre de la película a agregar.
        año (int): El año en que se lanzó la película.
        puntuación (int): La puntuación de la película en una escala del 1 al 10.
    Retorna:
        None: Esta función no devuelve nada; simplemente modifica la lista de películas.

    Ejemplo de uso:
        películas = [
            {'nombre': 'Pelicula1', 'año': 2010, 'puntuación': 8},
            {'nombre': 'Pelicula2', 'año': 2015, 'puntuación': 7}
        ]
        
        # Agregar una nueva película
        agregar_película(películas, 'Pelicula3', 2018, 9)
    """
    películas.apppend({
        'nombre': nombre, 
        'año': año,
        'puntuación': puntuación
    })

peliculas_de_sol = [
    {'nombre': 'Pelicula1', 'año': 2010, 'puntuacion': 8},
    {'nombre': 'Pelicula2', 'año': 2015, 'puntuacion': 6},
    {'nombre': 'Pelicula3', 'año': 2018, 'puntuacion': 9},
    {'nombre': 'Pelicula4', 'año': 2020, 'puntuacion': 7},
]

peliculas_mejores_sol = mejores_películas(peliculas_de_sol)
print(peliculas_mejores_sol)