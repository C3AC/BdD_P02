from functions.invcheckingfactory import InventoryChecker
from functions.invupdate import additem
def cocina_menu():
    print("Cocina Menu:")
    print("1. Revisar Inventario")
    print("2. Agregar Objeto al Inventario")
    print("3. Salir")

def handle_cocina_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    inv_checker = InventoryChecker()  
    if choice == '1':
        inv_checker.checkinv(cursor, id_sede)  
    elif choice == '2':
        additem(cursor, id_sede) 
        connection.commit()  
    elif choice == '3':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True