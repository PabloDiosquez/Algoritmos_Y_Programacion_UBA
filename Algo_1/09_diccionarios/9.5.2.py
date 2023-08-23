# Diccionarios usados para contar.
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
# hace hoy” debe devolver: {'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
# dena de texto, y los devuelva en un diccionario.
# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.

from helpers import apariciones, agregar_clave_valor_si_no_está, repeticiones
from random import choice

# a) 
def diccionario_de_apariciones(cadena: str) -> dict:
    """
    Describe un diccionario con la cantidad de apariciones de cada palabra en la cadena dada.
    """
    diccionario = {}
    palabras = cadena.split(' ')
    for palabra in palabras:
        agregar_clave_valor_si_no_está(palabra, apariciones(palabra, cadena), diccionario)
    return diccionario
        
# print(diccionario_de_apariciones("que lindo día que hace hoy"))

# b)
def apariciones_de_caracteres(cadena: str) -> dict:
    """
    """
    diccionario = {}
    for caracter in cadena:
        agregar_clave_valor_si_no_está(caracter, repeticiones(caracter, cadena), diccionario)
    return diccionario

# print(apariciones_de_caracteres("que lindo dia"))

# c)

def tirar_dados(iteraciones):
    """
    """
    dados = [1,2,3,4,5,6]
    cantidades = dict()
    for _ in range(iteraciones):
        suma = choice(dados) + choice(dados)
        if suma in cantidades:
            cantidades[suma] += 1
        else:
            cantidades[suma] = 1
    return cantidades

# print(tirar_dados(5))