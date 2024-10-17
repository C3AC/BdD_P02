from tabulate import tabulate
from datetime import datetime
import hashlib
from functions.genclient import generar_cliente
from functions.addblame import blaming

def get_available_tables(cursor, fecha_reserva, hora_reserva, id_sede):
    query = """
            SELECT *
            FROM mesa
            WHERE id_sede=%s AND id_mesa not in (SELECT id_mesa
                                                FROM reserva 
                                                WHERE fecha_reserva = %s 
                                                AND (hora_reserva - %s) < '3 hours' )
    """
    cursor.execute(query, (id_sede,fecha_reserva, hora_reserva,))
    return cursor.fetchall()

def generate_unique_code(id_cliente, id_mesa, fecha, hora):
    unique_string = f"{id_cliente}{id_mesa}{fecha}{hora}"
    hash_object = hashlib.md5(unique_string.encode())
    unique_code = int(hash_object.hexdigest(), 16) % (10**9) 
    return unique_code

def addreservation(cursor, id_sede):
    cursor.execute("SELECT id_cliente, nombre_cliente FROM cliente;")
    results = cursor.fetchall()
    headers = ["ID Cliente", "Nombre"]
    print(tabulate(results, headers, tablefmt="fancy_outline"))
    try:
        flag = True
        while flag:
            id_cliente = int(input("Ingrese el ID del cliente que desea hacer la reservación (ingrese 0 para crear un usuario): "))
            query = "SELECT id_cliente FROM cliente WHERE id_cliente = %s"
            cursor.execute(query, (id_cliente,))
            if id_cliente == 0:
                id_cliente = generar_cliente(cursor)
                if id_cliente is None:
                    print ("Cliente agregado no pudo ser accesado, reintente la operación de reserva")
                    return 
            elif cursor.fetchone() is None and id_cliente != 0:
                print("El ID de cliente ingresado no existe.")
            else:
                flag = False
    except ValueError:
        print("ID de cliente inválido.")
        return    
    while True:
        try: 
            fecha = input("Ingrese la fecha de la reservación (YYYY-MM-DD): ")
            hora = input("Ingrese la hora de la reservación (HH:MM): ")
            fecha_hora_reserva = datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
            if fecha_hora_reserva < datetime.now():
                print("La fecha y hora de la reservación no pueden ser anteriores a la fecha y hora actuales.")
            else:
                break
        except ValueError:
            print("Formato de fecha u hora incorrecto. Por favor, ingrese la fecha en formato YYYY-MM-DD y la hora en formato HH:MM.")


    available_tables = get_available_tables(cursor, fecha, hora, id_sede)
    if not available_tables:
        print("No hay mesas disponibles para la fecha y hora seleccionadas.")
        return

    print("Mesas disponibles:")
    for table in available_tables:
        print(f"ID Mesa: {table[0]}")

    id_mesa = input("Ingrese el ID de la mesa que desea reservar: ")

   
    id_reserva = generate_unique_code(id_cliente, id_mesa, fecha, hora)
    print(f"ID de la reserva: {id_reserva}")

    query = """
        INSERT INTO reserva (id_reserva, id_sede, id_cliente, id_mesa, fecha_reserva, hora_reserva)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (id_reserva, id_sede, id_cliente, id_mesa, fecha, hora))
    print("Reservación agregada exitosamente.")
    blaming(cursor)
    return id_reserva