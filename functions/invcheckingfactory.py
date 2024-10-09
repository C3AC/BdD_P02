from tabulate import tabulate

class InventoryChecker:
    def checkinv(self, cursor, id_sede=None):
        if id_sede:
            self.checkinv_with_sede(cursor, id_sede)
        else:
            self.checkinv_without_sede(cursor)

    def checkinv_with_sede(self, cursor, id_sede):
        print(f"Revisando inventario para la sede {id_sede}...")
        query = """
            SELECT inv.id_producto, nombre_producto, SUM(cantidad)
            FROM inventario inv
            JOIN ingredientes ing ON inv.id_producto = ing.id_producto
            WHERE id_sede = %s
            GROUP BY inv.id_producto, nombre_producto;
        """
        cursor.execute(query, (id_sede,))
        results = cursor.fetchall()
        headers = ["ID Producto", "Nombre Producto", "Cantidad"]
        print(tabulate(results, headers, tablefmt="fancy_outline"))
        input("Presione enter para continuar...")

    def checkinv_without_sede(self, cursor):
        print("Revisando inventario...")
        query = """
            SELECT inv.id_sede,inv.id_producto, nombre_producto, SUM(cantidad)
            FROM inventario inv
            JOIN ingredientes ing ON inv.id_producto = ing.id_producto
            GROUP BY inv.id_producto, nombre_producto, inv.id_sede
            ORDER BY inv.id_sede;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        headers = ["ID Producto", "Nombre Producto", "Cantidad"]
        print(tabulate(results, headers, tablefmt="fancy_outline"))
        input("Presione enter para continuar...")