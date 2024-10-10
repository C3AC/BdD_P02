from tabulate import tabulate
from datetime import datetime
import hashlib

def get_available_tables(cursor, fecha_reserva, hora_reserva):
    query = """
        SELECT m.id_mesa
        FROM mesa m
        LEFT JOIN reserva r ON m.id_mesa = r.id_mesa
        WHERE NOT (r.fecha_reserva = %s AND (r.hora_reserva - %s::time) > INTERVAL '3 hours')
    """
    cursor.execute(query, (fecha_reserva, hora_reserva))
    return cursor.fetchall()

def generate_unique_code(id_cliente, id_mesa, fecha, hora):
    # Combinar los elementos en una cadena
    unique_string = f"{id_cliente}{id_mesa}{fecha}{hora}"
    # Generar un hash de la cadena
    hash_object = hashlib.md5(unique_string.encode())
    # Convertir el hash a un número entero
    unique_code = int(hash_object.hexdigest(), 16) % (10**9)  # Limitar a 9 dígitos para que quepa en un int
    return unique_code

def addreservation(cursor, id_sede):
    cursor.execute("SELECT id_cliente, nombre_cliente FROM cliente;")
    results = cursor.fetchall()
    headers = ["ID Cliente", "Nombre"]
    print(tabulate(results, headers, tablefmt="fancy_outline"))
    id_cliente = input("Ingrese el ID del cliente que desea hacer la reservación: ")
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


    available_tables = get_available_tables(cursor, fecha, hora)
    if not available_tables:
        print("No hay mesas disponibles para la fecha y hora seleccionadas.")
        return

    print("Mesas disponibles:")
    for table in available_tables:
        print(f"ID Mesa: {table[0]}")

    id_mesa = input("Ingrese el ID de la mesa que desea reservar: ")

    # Generar un código único para la reserva
    id_reserva = generate_unique_code(id_cliente, id_mesa, fecha, hora)
    print(f"ID de la reserva: {id_reserva}")

    query = """
        INSERT INTO reserva (id_reserva, id_sede, id_cliente, id_mesa, fecha_reserva, hora_reserva)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (id_reserva, id_sede, id_cliente, id_mesa, fecha, hora))
    print("Reservación agregada exitosamente.")