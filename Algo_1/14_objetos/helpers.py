# ----------- Funciones sobre números -----------
 
def validar_número(valor):
    """
    Si el valor es numérico lo devuelve. En caso contrario lanza TypeError.
    """
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor!r} no es un valor numérico")
    return valor 

def validar_número_positivo(valor):
    """
    Si el valor es numérico y positivo lo devuelve. En caso contrario lanza una excepción.
    """
    if not isinstance(valor, (int, float)):
        raise TypeError(f"{valor!r} no es un valor numérico")
    if not valor > 0:
        raise ValueError("El número debe ser mayor a 0")
    return valor

def validar_número_entero_positivo(valor):
    """
    Si el valor es un número entero y positivo lo devuelve. En caso contrario lanza una excepción.
    """
    if not isinstance(valor, int):
        raise TypeError(f"{valor!r} no es un número entero")
    if not valor > 0:
        raise ValueError("El número debe ser mayor a 0")
    return valor 

def validar_número_distinto_de_cero(valor):
    """
    Si el valor es un número entero distinto de 0 lo devuelve. En caso contrario lanza ZeroDivisionError.
    """
    if not isinstance(valor, int):
        raise TypeError(f"{valor!r} no es un número entero")
    if not valor == 0:
        raise ZeroDivisionError("El número debe ser distinto de 0")
    return valor

# ----------- Funciones sobre cadenas -----------

def validar_cadena_no_vacía(cadena):
    """
    Si la cadena no es vacía la devuelve. En caso contrario lanza ValueError.
    """
    if es_vacía(cadena):
        raise ValueError("La cadena no debe ser vacía")
    return cadena

def es_vacía(cadena: str):
    """
    Indica si la cadena de caracteres dada es vacía.
    """
    return not len(cadena)

# ----------- Funciones sobre listas -----------

def validar_lista_de_números(lista: list):
    """
    Si la lista es de números, la devuelve. En caso contrario, lanza TypeError.
    Además, valida que la lista no sea vacía.
    """
    if es_vacía(lista):
        raise ValueError("La lista no debe ser vacía")
    for elemento in lista:
        if not isinstance(elemento, (int, float, complex)):
            raise TypeError(f"{elemento!r} no es un valor numérico")
    return lista 

def sumar_uno_a_uno(lista1, lista2):
    """
    Describe la lista que resulta de sumar los elementos de las dos listas dadas uno a uno.
    Precondiciones:
        - Las listas deben tener la misma nro_de_billetes de elementos y no deben ser vacías.
        - Los elementos de ambas listas deben ser 'sumables' entre sí. Deben soportar el operador +.
    """
    suma = []
    for index in range(len(lista1)):
        suma.append(lista1[index] + lista2[index])
    return suma 

def multiplicar_por_número(lista: list, número):
    """
    Multiplica cada elemento de una lista por un número dado.

    Parámetros:
    - lista (list): La lista de elementos a multiplicar.
    - numero: El número por el cual se multiplicarán los elementos de la lista.

    Retorna:
    - lista_multiplicada (list): Una nueva lista con los elementos multiplicados.
    """
    lista_multiplicada = []
    for elemento in lista:
        lista_multiplicada.append(elemento*número)
    return lista_multiplicada

# ----------- Funciones sobre diccionarios -----------

def agregar_par_clave_valor(dicc_viejo: dict, dicc_nuevo: dict):
    """
    Agrega los pares clave-valor del diccionario nuevo al diccionario viejo.

    Parámetros:
    - dicc_viejo (dict): El diccionario viejo al que se agregarán los pares clave-valor.
    - dicc_nuevo (dict): El diccionario nuevo que contiene los pares clave-valor a agregar.

    Retorna:
    - dict: El diccionario viejo con los pares clave-valor adicionales.
    """
    for clave in dicc_nuevo.keys():
        if clave in dicc_viejo:
            dicc_viejo[clave] += dicc_nuevo[clave]
        else: 
            dicc_viejo[clave] = dicc_nuevo[clave]
    return dicc_viejo

# Funciones específicas para el ejercicio 14.9.6 ➡ Clase Caja 

def validar_denominaciones(denominaciones: dict):
    """
    """
    DENOMINACIONES_VÁLIDAS = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

    for denominación in denominaciones:
        if denominación not in DENOMINACIONES_VÁLIDAS:
            raise ValueError(f"Denominación {denominación!r} no válida")
    return denominaciones

def validar_denominaciones_específicas(denominaciones_en_caja, denominaciones_a_validar):
    """
    """
    for denominación in denominaciones_a_validar:
        if denominación not in denominaciones_en_caja:
            raise ValueError(f"No hay billetes de denominación {denominación} en la caja")
    return denominaciones_a_validar

def sumar_denominaciones(denominaciones: dict):
    """
    """
    total = 0
    for denominación in denominaciones:
        nro_de_billetes = denominaciones[denominación]
        total += nro_de_billetes*denominación
    return total 