# 4.
def agregar_ingrediente_si_no_está(ingredientes: list, ingrediente: str):
    """
    Agrega el ingrediente dado a la lista de ingredientes si éste no pertenece a la misma.
    En caso contrario, deja igual a la lista.
    """
    if ingrediente not in ingredientes:
        ingredientes.append(ingrediente)

def main():
    ingredientes = ["tomate", "queso", "cebolla", "huevo"]
    agregar_ingrediente_si_no_está(ingredientes, "orégano") 
    print(ingredientes)
    agregar_ingrediente_si_no_está(ingredientes, "queso")
    print(ingredientes)

main()