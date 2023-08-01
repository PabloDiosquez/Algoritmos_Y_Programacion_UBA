# Escribir una función que reciba las coordenadas de dos vectores en R3 y devuelva las
# coordenadas del producto vectorial.

def producto_vectorial(x1,y1,z1,x2,y2,z2):
    """Describe las coordenas del producto vectorial de los dos vectores dados.
    """
    return y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2