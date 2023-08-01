# Escribir una función que, dados cuatro números, devuelva el mayor producto
# de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos (8 = −2 × −4).

def mayor_producto(num1: int, num2: int, num3: int, num4: int) -> int:
    return _maximo(todas_las_multiplicaciones(num1, num2, num3, num4))

def todas_las_multiplicaciones(a, b, c, d):
    return [a*b, a*c, a*d, b*c, b*d, c*d]

def _maximo(numeros: list) -> int:
    if len(numeros) == 1: return numeros[0]
    maximoAlMomento = numeros[0]
    numeros.remove(maximoAlMomento)
    return _maximo2(maximoAlMomento, _maximo(numeros))

def _maximo2(num1: int, num2: int) ->  int:
    if num1 >= num2: return num1
    return num2