

def gerente_menu():
    print("Menu:")
    print("1. Revisar Inventario")
    print("2. Revisar Reservaciones")
    print("3. Salir")

def handle_gerente_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    if choice == '1':
        c.checkinv(cursor, id_sede)
    elif choice == '2':
        print(f"Revisando reservaciones para la sede {id_sede}...")
        cursor.execute
    elif choice == '3':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True