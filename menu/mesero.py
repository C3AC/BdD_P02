from functions.rescheckingfactory import ReservationChecker


def mesero_menu():
    print("Mesero Menu:")
    print("1. Revisar Reservaciones")
    print("2. Salir")

def handle_mesero_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    res_checker = ReservationChecker()  # Crear una instancia de ReservationChecker
    if choice == '1':
        res_checker.checkres(cursor, id_sede)  # Usar la instancia para llamar a checkres
    elif choice == '2':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True