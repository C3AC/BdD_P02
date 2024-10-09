from functions.invcheckingfactory import InventoryChecker
from functions.rescheckingfactory import ReservationChecker


def gerente_menu():
    print("Menu:")
    print("1. Revisar Inventario")
    print("2. Revisar Reservaciones")
    print("3. Salir")

def handle_gerente_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    inv_checker = InventoryChecker()  
    res_checker = ReservationChecker()  
    if choice == '1':
        inv_checker.checkinv(cursor, id_sede)  
    elif choice == '2':
        res_checker.checkres(cursor, id_sede)  
    elif choice == '3':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True