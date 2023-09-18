# 11.
def calcular_total_a_pagar(ticket: list) -> float:
    """
    Describe el total a pagar a partir de una lista de productos en un ticket.
    Parámetros:
        - ticket (list[tuple]): Una lista de tuplas de la forma (producto, precio) que representa los productos en el ticket.
    Retorna:
        float: El total a pagar calculado a partir de los precios de los productos en el ticket.
    """
    total_a_pagar = 0
    for producto, precio in ticket: # desempaquetado directamente las tuplas (producto, precio)
        total_a_pagar += precio 
    return total_a_pagar 