# Dada una lista de números enteros y un entero k, escribir una función que:
# a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
# k.

from helpers import es_vacía, singular_si

def menores_a_(números: list[int], k: int) -> list[int]:
    if es_vacía(números): return []
    primer_número = números[0]
    números.remove(primer_número)
    return singular_si(primer_número, primer_número < k) + menores_a_(números, k)

# b) Devuelva una lista con aquellos que son múltiplos de k.

def múltiplos_de_(números: list[int], k: int) -> list[int]:
    if es_vacía(números): return []
    primer_número = números[0]
    números.remove(primer_número)
    return singular_si(primer_número, not primer_número % k) + múltiplos_de_(números, k)