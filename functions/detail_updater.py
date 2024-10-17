from tabulate import tabulate

def addproduct(cursor, id_pedido, connection):
    query = "SELECT id_plato, nombre_plato, precio_plato FROM plato"
    cursor.execute(query)
    results = cursor.fetchall()
    headers = ["ID Plato", "Nombre", "Precio"]
    flag = True
    while flag:
        print(tabulate(results, headers, tablefmt="fancy_outline"))
        try:
            select = int(input('Seleccione un objeto del menú para agregar al pedido'))
            query = "SELECT id_plato FROM plato WHERE id_plato = %s"
            cursor.execute(query, (select,))
            if cursor.fetchone() is None:
                print("ID de plato inválido")
            else:
                flag = True   
                while flag:
                    try:
                        cantidad = int(input('Ingrese la cantidad de platos a agregar: '))
                        if cantidad <= 0:
                            print("Cantidad inválida")
                        else:
                            flag = False
                    except ValueError:
                        print("Entrada inválida")
                        return
                
                query = "INSERT INTO detalle_pedido (id_pedido, id_plato, cantidad) VALUES (%s, %s,%s)"
                cursor.execute(query, (id_pedido, select,cantidad,))
                print("Producto agregado exitosamente")
                if connection.notices:
                    for notice in connection.notices:
                        print("NOTICE:", notice)
                selection = input("¿Desea agregar otro producto? (s/n): ")
                if selection.lower() == 'n':
                    flag = False
                elif selection.lower() == 's':
                    flag = True
                else:
                    print("Entrada inválida")
                    print('Saliendo como opción por defecto')
                    flag = False
        except ValueError:
            print("Entrada inválida")
            return