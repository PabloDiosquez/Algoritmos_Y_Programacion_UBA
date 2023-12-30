# Escribir dos funciones mutualmente recursivas par(n) e impar(n) que de-
# terminen la paridad del numero natural dado, conociendo solo que:

# • 1 es impar.
# • Si un número es impar, su antecesor es par; y viceversa.

def es_par(n: int) -> bool:
    """
    Verifica la paridad de un número natural utilizando recursión.

    Parámetros:
    - n (int): El número natural que se verificará si es par.

    Retorna:
    bool: True si n es par, False si es impar.
    """
    # Caso base: 0 es par.
    if n == 0:
        return True
    # Llama a la función es_impar con el antecesor de n.
    return es_impar(n - 1)

def es_impar(n: int) -> bool:
    """
    Verifica la paridad de un número natural utilizando recursión.

    Parámetros:
    - n (int): El número natural que se verificará si es impar.

    Retorna:
    bool: True si n es impar, False si es par.
    """
    # Caso base: 0 es par, por lo que n es impar.
    if n == 0:
        return False
    # Llama a la función es_par con el antecesor de n.
    return es_par(n - 1)

# Ejemplos de uso con assert para verificar resultados.
assert es_par(2)
assert es_par(10)
assert es_par(14)
assert not es_par(15)
assert es_impar(15)
assert es_impar(21)
assert es_impar(75)
assert not es_impar(14)