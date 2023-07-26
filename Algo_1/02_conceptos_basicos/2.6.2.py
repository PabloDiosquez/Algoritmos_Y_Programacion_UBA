from helpers import get_int, get_float

def _capital_total(capital_inicial, tasa_interes, cantidad_anios):
    """Describe el monto final a obtener dado un capital inicial, una tasa de interés
    y según la cantidad de años.
    """
    return capital_inicial * pow((1 + tasa_interes/100),cantidad_anios)

def capital_total():
    """Describe el monto final a obtener dado un capital inicial, una tasa de interés
    y según la cantidad de años.
    """
    capital_inicial = get_float("Capital inicial: ")
    tasa_interes    = get_float("Tasa de interés:(%) ")
    cantidad_anios  = get_int("Cantidad de años: ")
    return round(_capital_total(capital_inicial, tasa_interes, cantidad_anios),2)

print("- Ejercicio 2.6.2 -")
print(capital_total())