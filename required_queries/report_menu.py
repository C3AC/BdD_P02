from tabulate import tabulate

def report_menus(connection):
    print("Reportes: ")
    print("1. Platillos más vendidos")
    print('2. Clientes frecuentes')
    print('3. Clientes preferidos')
    print('4. Insumos a vencer')
    print('5. Mejores sucursales')
    print('6. Regresar')
    choice = input("Ingrese su elección: ")
    handle_report_choice(choice, connection)

def handle_report_choice(choice, connection):
    cursor = connection.cursor()
    if choice == '1':
        query = """
            SELECT p.id_plato, nombre_plato, sum(dp.cantidad)
            FROM detalle_pedido dp join plato p on p.id_plato = dp.id_plato
            GROUP BY p.id_plato
            LIMIT 10;     
        """
        cursor.execute(query)
        results = cursor.fetchall()
        headers = ['ID',"Platillo", "Cantidad vendida"]
        print(tabulate(results, headers, tablefmt="fancy_grid"))
    elif choice == '2':
        query = """
            SELECT c.nombre_cliente, COUNT(r.id_reserva) AS cantidad_reservas
            FROM cliente c JOIN reserva r ON c.id_cliente = r.id_cliente
            GROUP BY c.nombre_cliente
            ORDER BY cantidad_reservas DESC
            LIMIT 10;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        headers = ["Cliente", "Cantidad de reservas"]
        print(tabulate(results, headers, tablefmt="fancy_grid"))
    elif choice == '3':
        query = """
            SELECT c.nombre_cliente, COUNT(r.id_reserva) AS total_reservas, 
                STRING_AGG(DISTINCT p.nombre_plato, ', ') AS platos_preferidos
            FROM CLIENTE c JOIN RESERVA r 
            ON c.id_cliente = r.id_cliente LEFT JOIN cliente_plato cp 
            ON c.id_cliente = cp.id_cliente LEFT JOIN PLATO p 
            ON cp.id_plato = p.id_plato
            GROUP BY c.id_cliente, c.nombre_cliente
            ORDER BY total_reservas DESC
            LIMIT 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        headers = ["Cliente", "Cantidad de reservas"]
        print(tabulate(results, headers, tablefmt="fancy_grid"))
    elif choice == '4':
        query = """
            SELECT i.nombre_producto, inv.cantidad, inv.fecha_caducidad, s.nombre_sede
            FROM INVENTARIO inv JOIN INGREDIENTES i 
            ON inv.id_producto = i.id_producto JOIN SEDE s 
            ON inv.id_sede = s.id_sede
            WHERE inv.cantidad > 0 
            AND (inv.fecha_caducidad <= CURRENT_DATE + INTERVAL '7 days'
            OR inv.cantidad - nivel_minimo <= 5)
            ORDER BY inv.fecha_caducidad ASC, inv.cantidad ASC;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        headers = ["Insumo",'Cantidad', "Fecha de vencimiento",'Sede']
        print(tabulate(results, headers, tablefmt="fancy_grid"))
    elif choice == '5':
        query = """
            SELECT s.nombre_sede, COUNT(r.id_reserva) AS total_reservas
            FROM sede s JOIN reserva r ON s.id_sede = r.id_sede
            GROUP BY s.nombre_sede
            ORDER BY total_reservas DESC
            LIMIT 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        headers = ["Sede", "Total de reservas"]
        print(tabulate(results, headers, tablefmt="fancy_grid"))