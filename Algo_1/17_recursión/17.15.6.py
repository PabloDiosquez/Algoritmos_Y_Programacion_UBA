# Escribir una función recursiva que calcule recursivamente el n-ésimo número
# triangular (el número 1 + 2 + 3 + ⋯ + n).

def numero_triangular(n):
  """
  Calcula recursivamente el n-ésimo número triangular.

  Parámetros:
  - n (int): El índice del número triangular que se calculará.

  Retorna:
  int: El n-ésimo número triangular.
  """
  # Caso base: el número triangular de 0 es 0.
  if n == 0:
      return 0
  # Llama recursivamente a la función para el índice n-1 y suma n.
  return numero_triangular(n - 1) + n

# Ejemplos de uso con assert para verificar resultados.
assert numero_triangular(0) == 0
assert numero_triangular(1) == 1
assert numero_triangular(2) == 3   # 1 + 2 = 3
assert numero_triangular(3) == 6   # 1 + 2 + 3 = 6
assert numero_triangular(4) == 10  # 1 + 2 + 3 + 4 = 10