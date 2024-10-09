from tabulate import tabulate

class ReservationChecker:
    def checkres(self, cursor, id_sede=None):
        if id_sede:
            self.checkres_with_sede(cursor, id_sede)
        else:
            self.checkres_without_sede(cursor)

    def checkres_with_sede(self, cursor, id_sede):
        print(f"Revisando reservas para la sede {id_sede}...")
        cursor.execute("SELECT id_reserva, nombre_cliente, celular, c.hora_reserva FROM reserva r JOIN cliente c on r.id_cliente = c.id_cliente WHERE id_sede =%s;", (id_sede,))
        results = cursor.fetchall()
        headers = ["ID Reserva", "ID Cliente", "ID Mesa", "Fecha Reserva", "Hora Reserva", "Cantidad Personas"]
        print(tabulate(results, headers, tablefmt="fancy_outline"))
        input("Presione enter para continuar...")

    def checkres_without_sede(self, cursor):
        print("Revisando reservas...")
        cursor.execute("SELECT id_reserva, nombre_cliente, celular, c.hora_reserva FROM reserva r JOIN cliente c on r.id_cliente = c.id_cliente;")
        results = cursor.fetchall()
        headers = ["ID Reserva", "ID Cliente", "ID Mesa", "Fecha Reserva", "Hora Reserva", "Cantidad Personas"]
        print(tabulate(results, headers, tablefmt="fancy_outline"))
        input("Presione enter para continuar...")