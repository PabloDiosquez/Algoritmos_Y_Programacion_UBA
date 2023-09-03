def imprimir_estrellas(n):
    """
    Imprime 'n' estrellas en la pantalla.
    Parámetros:
        n (int): Número de estrellas a imprimir.
    Pre: 
        - 'n' debe ser un número entero no negativo.
    """
    if n == 0: return  
    else:
        print('⭐', end=' ')
        imprimir_estrellas(n - 1)

# Una pequeña prueba... 🚀
imprimir_estrellas(5)