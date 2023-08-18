# a) Escribir una función que reciba dos vectores y devuelva su producto escalar.

def producto_escalar_2D(vector1: tuple, vector2: tuple) -> float:
    """ Describe el producto escalar entre los dos vectores de R2 dados.
        Precondición:
            Los dos vectores dados deben ser de dos componentes.
    """
    vx, vy = vector1
    ux, uy = vector2
    return vx*ux + vy*uy 

def producto_escalar(vector1: tuple, vector2: tuple) -> float:
    """ Describe el producto escalar entre los dos vectores de Rn dados.
        Precondición:
            Los dos vectores dados deben tener la misma dimensión.
    """
    producto_escalar = 0
    for índice in range(len(vector1)):
        producto_escalar += vector1[índice]*vector2[índice]
    return producto_escalar

# b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
# d) Escribir una función que reciba un vector y devuelva su norma.