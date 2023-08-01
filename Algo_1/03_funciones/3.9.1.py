# Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

from helpers import get_int

# a) 
def a_segundos(horas, minutos, segundos): 
    """Describe la duración en segundos de un intervalo dado en horas, minutos y segundos.
    """
    return 3600*horas + 60*minutos + segundos

def calculadora_de_segundos():
    """Pequeña calculadora de segundos.
    """
    horas    = get_int("Horas: ")
    minutos  = get_int("Minutos: ")
    segundos = get_int("Segundos: ")
    return a_segundos(horas, minutos, segundos)


def a_horas_minutos_segundos(segundos):
    """Describe la duración en horas, minutos y segundos de un intervalo dado en segundos."""
    horas   = segundos // 3600
    minutos = (segundos % 3600) // 60 
    segs    = (segundos % 3600) % 60 
    return horas, minutos, segs