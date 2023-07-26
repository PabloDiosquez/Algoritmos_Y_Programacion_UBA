# Analizar los siguientes bloques de código. ¿Cuál será el resultado de ejecutar-
# los? Verificar la respuesta con el intérprete.
from helpers import ejercicio

def loop(vueltas):
    for i in range(vueltas):
        print(i * i)

ejercicio("1.11.6.a:", loop(5))

def loop_range(inicio, fin):
    for i in range(inicio, fin):   
        print(i, 2 ** i)
    
ejercicio("1.11.6.b:", loop_range(2,6))