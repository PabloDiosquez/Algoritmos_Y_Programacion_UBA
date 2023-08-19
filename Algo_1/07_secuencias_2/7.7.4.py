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

def son_ortogonales(vector1: tuple, vector2: tuple) -> bool:
    """ Indica si los vectores dados son ortogonales.
        Precondición:
            Los dos vectores dados deben tener la misma dimensión.
    """
    return producto_escalar(vector1, vector2) == 0

# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.

def son_paralelos(vector1: tuple, vector2: tuple) -> bool:
    """ Indica si los dos vectores dados son paralelos.
        Precondición:
            Los vectores dados no deben ser iguales al vector nulo.
    """
    if not len(vector1) or not len(vector2): return False
     
    for índice in range(len(vector1)):
        if   not vector1[índice] and not vector2[índice]:                  continue
        elif not vector1[índice] or not vector2[índice] :                  return False 
        elif vector1[índice] / vector2[índice] != vector1[0] / vector2[0]: return False 

    return True  

# d) Escribir una función que reciba un vector y devuelva su norma.

def norma_vectorial2D(vector: tuple) -> float:
    """ Describe la norma del vector dado.
        Precondición:
            El vector dado debe ser de dos dimensiones.
    """
    vx, vy = vector
    return pow(pow(vx, 2) + pow(vy, 2), 0.5)

def norma_vectorial(vector: tuple) -> float:
    """ Describe la norma del vector dado.
    """
    norma = 0
    for número in vector:
        norma += pow(número, 2)
    return pow(norma, 0.5)  

def pruebas():
    assert son_paralelos((1,2,3), (2,4,6))

pruebas() 