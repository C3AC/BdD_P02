def cocina_menu():
    print("Cocina Menu:")
    print("1. Check Inventory")
    print("2. Exit")

def handle_cocina_choice(choice, id_sede):
    if choice == '1':
        print(f"Checking inventory for sede {id_sede}...")
        # Add inventory checking logic here using id_sede
    elif choice == '2':
        print("Exiting...")
        return False
    else:
        print("Invalid choice, please try again.")
    return True