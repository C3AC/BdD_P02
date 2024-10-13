from tabulate import tabulate
from addblame import blaming

def additem(cursor, id_sede): 
    cursor.execute("SELECT id_producto, nombre_producto FROM ingredientes;")
    results = cursor.fetchall()
    headers = ["ID Producto", "Nombre Producto"]
    print(tabulate(results, headers, tablefmt="fancy_outline"))
    id_producto = input("Ingrese el ID del producto que desea agregar: ")
    cantidad = input("Ingrese la cantidad que desea agregar: ")
    fecha_caducidad = input("Ingrese la fecha de caducidad del producto (YYYY-MM-DD): ")
    try :
        cursor.execute('''INSERT INTO inventario(id_sede, id_producto, cantidad, fecha_caducidad) 
                   VALUES (%s, %s, %s, %s);''', (id_sede, id_producto, cantidad, fecha_caducidad))
        print("Producto agregado al inventario.")
        blaming(cursor)
    except Exception as e:
        print("Error al agregar el producto al inventario", e)
    finally:
        return