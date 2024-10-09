from tabulate import tabulate

def checkres(cursor, id_sede):     
    print(f"Revisando reservas para la sede {id_sede}...")
    cursor.execute("SELECT id_reserva, id_cliente, id_mesa, fecha_reserva, hora_reserva, cantidad_personas FROM reservas WHERE id_sede = %s;", (id_sede,))
    results = cursor.fetchall()
    headers = ["ID Reserva", "ID Cliente", "ID Mesa", "Fecha Reserva", "Hora Reserva", "Cantidad Personas"]
    print(tabulate(results, headers, tablefmt="fancy_outline"))
    input("Presione enter para continuar...")

def checkres(cursor):
    print("Revisando reservas...")
    cursor.execute("SELECT id_reserva, id_cliente, id_mesa, fecha_reserva, hora_reserva, cantidad_personas FROM reservas;")
    results = cursor.fetchall()
    headers = ["ID Reserva", "ID Cliente", "ID Mesa", "Fecha Reserva", "Hora Reserva", "Cantidad Personas"]
    print(tabulate(results, headers, tablefmt="fancy_outline"))
    input("Presione enter para continuar...")