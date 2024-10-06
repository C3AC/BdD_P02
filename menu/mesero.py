def mesero_menu():
    print("Mesero Menu:")
    print("1. Check Reservations")
    print("2. Exit")

def handle_mesero_choice(choice, id_sede):
    if choice == '1':
        print(f"Checking reservations for sede {id_sede}...")
        # Add reservations checking logic here using id_sede
    elif choice == '2':
        print("Exiting...")
        return False
    else:
        print("Invalid choice, please try again.")
    return True