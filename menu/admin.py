from functions.invcheckingfactory import InventoryChecker
from functions.rescheckingfactory import ReservationChecker


def admin_menu():
    print("Admin Menu:")
    print("1. Register User")
    print("2. Check Inventory")
    print("3. Check Reservations")
    print("4. Exit")

def handle_admin_choice(choice, connection):
    cursor = connection.cursor()
    inv_checker = InventoryChecker()  # Crear una instancia de InventoryChecker
    res_checker = ReservationChecker()  # Crear una instancia de ReservationChecker
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
        print("Exiting...")
        return False
    else:
        print("Invalid choice, please try again.")
    return True