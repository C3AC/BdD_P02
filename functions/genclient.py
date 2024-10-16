from functions.addblame import blaming
def generar_cliente(cursor):
    print("Creando nuevo cliente...")
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    while True:
        try:
            celular = int(input("Ingrese el número de celular del cliente: "))
            break
        except ValueError:
            print("Número de celular inválido.")
    query = '''
        INSERT INTO cliente(nombre_cliente, correo_e, celular, reseña)
	    VALUES (%s,%s,%s,'n/a');
    '''
    cursor.execute(query, (nombre, correo, celular))
    print("Cliente creado exitosamente.")
    cursor.execute("SELECT id_cliente FROM cliente WHERE nombre_cliente = %s", (nombre,))
    blaming(cursor)
    return cursor.fetchone()[0]