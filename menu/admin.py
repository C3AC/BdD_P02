def admin_menu():
    print("Admin Menu:")
    print("1. Register User")
    print("2. Check Inventory")
    print("3. Check Reservations")
    print("4. Exit")

def handle_admin_choice(choice):
    if choice == '1':
        print("Registering user...")
        # Add user registration logic here
    elif choice == '2':
        print("Checking inventory...")
        # Add inventory checking logic here
    elif choice == '3':
        print("Checking reservations...")
        # Add reservations checking logic here
    elif choice == '4':
        print("Exiting...")
        return False
    else:
        print("Invalid choice, please try again.")
    return True