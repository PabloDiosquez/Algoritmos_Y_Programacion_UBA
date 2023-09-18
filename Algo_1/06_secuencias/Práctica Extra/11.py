# 11.
# a.
def calcular_total_a_pagar(ticket: list) -> float:
    """
    Describe el total a pagar a partir de una lista de productos en un ticket.
    Parámetros:
        - ticket (list[tuple]): Una lista de tuplas de la forma (producto, precio) que representa los productos en el ticket.
    Retorna:
        float: El total a pagar calculado a partir de los precios de los productos en el ticket.
    """
    total_a_pagar = 0
    for _, precio in ticket: # desempaquetado directamente las tuplas (producto, precio)
        total_a_pagar += precio 
    return total_a_pagar 

# b.
def calcular_total_en_lista_de_tickets(tickets):
    """
    Calcula el total a pagar a partir de una lista de tickets.
    Parámetros:
        - tickets (list[list]): Una lista de tickets, donde cada ticket es una lista de tuplas (producto, precio).
    Retorna:
        float: El total a pagar calculado a partir de los precios de los productos en la lista de tickets dada.
    """
    total_a_pagar = 0
    for ticket in tickets:
        total_a_pagar += calcular_total_a_pagar(ticket)
    return total_a_pagar

def main():
    ticket = [
        ("Detergente", 123),
        ("Jabón líquido", 456)
    ]
    print(f"Total a pagar: ARS ${calcular_total_a_pagar(ticket)}")

main()