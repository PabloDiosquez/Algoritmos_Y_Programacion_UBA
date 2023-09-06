# 3.
def monto_total(ticket):
    """
    Describe el monto total a pagar a partir de un ticket dado.
    Parámetros:
        - ticket list[dict]: Una lista de diccionarios que representan los productos en el ticket dado. 
          Cada producto debe tener nombre, precio por unidad y cantidad.
    Retorna:
        - El monto total a pagar (float).  
    """
    if not ticket: raise ValueError("El ticket está vacío")
    monto_total_al_momento = 0
    for producto in ticket:
        monto_total_al_momento += producto['Precio por unidad'] * producto['Cantidad']
    return monto_total_al_momento