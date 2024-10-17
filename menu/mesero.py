from functions.rescheckingfactory import ReservationChecker
from functions.resupdate import addreservation
from functions.pedupdate import order
import functions.detail_updater as upd
from tabulate import tabulate

def mesero_menu():
    print("Mesero Menu:")
    print("1. Revisar Reservaciones")
    print("2. Agregar Reservación")
    print("3. Iniciar pedido")
    print("4. Agregar a pedido")
    print("5. Salir")

def handle_mesero_choice(choice, id_sede, connection):
    cursor = connection.cursor()
    res_checker = ReservationChecker()  
    if choice == '1':
        res_checker.checkres(cursor, id_sede)  
    elif choice == '2':
        addreservation(cursor, id_sede)  
        connection.commit()
    elif choice == '3':
        print("Menú y Pedido")
        pedido = order(cursor, id_sede)
        connection.commit()
        upd.addproduct(cursor, pedido, connection)
        connection.commit()
    elif choice == '4':
        query = "SELECT id_reserva FROM reserva WHERE fecha_reserva = CURRENT_DATE AND id_sede = %s"
        cursor.execute(query, (id_sede,))
        table = cursor.fetchall()
        print(tabulate(table, headers=['ID Pedido']))
        flag = True
        while flag:
            try:
                id_pedido = int(input("Ingrese el ID del pedido al que desea agregar productos: "))
                query = "SELECT id_reserva FROM reserva WHERE id_reserva = %s"
                cursor.execute(query, (id_pedido,))
                if cursor.fetchone() is None:
                    print("ID de pedido inválido")
                else:
                    flag = False
            except ValueError:
                print("ID inválido")
                return
        upd.addproduct(cursor,id_pedido,connection)
        connection.commit()
    elif choice == '5':
        print("Saliendo...")
        return False
    else:
        print("Elección inválida, por favor intente de nuevo.")
    return True