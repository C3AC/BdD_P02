from functions.invcheckingfactory import InventoryChecker
from functions.rescheckingfactory import ReservationChecker
from functions.invupdate import additem
from functions.resupdate import addreservation

def admin_menu():
    print("Admin Menu:")
    print("1. Register User")
    print("2. Check Inventory")
    print("3. Check Reservations")
    print("4. Add to Inventory")
    print("5. Add Reservation")
    print("6. Exit")

def handle_admin_choice(choice, connection):
    cursor = connection.cursor()
    inv_checker = InventoryChecker()  
    res_checker = ReservationChecker()  
    if choice == '1':
        print("Registering user...")
        # Add user registration logic here
    elif choice == '2':
        print("Checking inventory...")
        inv_checker.checkinv(cursor)  
    elif choice == '3':
        print("Checking reservations...")
        res_checker.checkres(cursor) 
    elif choice == '4':
        id_sede = input("Ingrese el ID de la sede donde desea agregar el objeto: ")
        additem(cursor, id_sede)  
        connection.commit()  
    elif choice == '5':
        id_sede = input("Ingrese el ID de la sede donde desea hacer la reservación: ")
        addreservation(cursor, id_sede) 
        connection.commit() 
    elif choice == '6':
        print("Exiting...")
        return False
    else:
        print("Invalid choice, please try again.")
    return True