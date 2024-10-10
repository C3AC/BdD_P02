from functions.invcheckingfactory import InventoryChecker
from functions.rescheckingfactory import ReservationChecker
from functions.invupdate import additem
from functions.resupdate import addreservation

def gerente_menu():
    print("Menu:")
    print("1. Revisar Inventario")
    print("2. Revisar Reservaciones")
    print("3. Agregar Objeto al Inventario")
    print("4. Agregar Reservación")
    print("5. Salir")

def handle_gerente_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    inv_checker = InventoryChecker()  
    res_checker = ReservationChecker()  
    if choice == '1':
        inv_checker.checkinv(cursor, id_sede)  
    elif choice == '2':
        res_checker.checkres(cursor, id_sede)  
    elif choice == '3':
        additem(cursor, id_sede)  
        connection.commit()  
    elif choice == '4':
        addreservation(cursor, id_sede)  
        connection.commit()  
    elif choice == '5':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True