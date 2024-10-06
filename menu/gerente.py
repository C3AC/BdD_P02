def gerente_menu():
    print("Gerente Menu:")
    print("1. Check Inventory")
    print("2. Check Reservations")
    print("3. Exit")

def handle_gerente_choice(choice, id_sede):
    if choice == '1':
        print(f"Checking inventory for sede {id_sede}...")
        # Add inventory checking logic here using id_sede
    elif choice == '2':
        print(f"Checking reservations for sede {id_sede}...")
        # Add reservations checking logic here using id_sede
    elif choice == '3':
        print("Exiting...")
        return False
    else:
        print("Invalid choice, please try again.")
    return True