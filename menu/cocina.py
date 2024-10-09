from functions.invcheckingfactory import InventoryChecker


def cocina_menu():
    print("Cocina Menu:")
    print("1. Revisar Inventario")
    print("2. Salir")

def handle_cocina_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    inv_checker = InventoryChecker()  # Crear una instancia de InventoryChecker
    if choice == '1':
        inv_checker.checkinv(cursor, id_sede)  # Usar la instancia para llamar a checkinv
    elif choice == '2':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True