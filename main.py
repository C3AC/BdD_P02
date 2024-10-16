import psycopg2
import json
from menu import admin as a
from menu import gerente as g
from menu import cocina as c
from menu import mesero as m
import globvar

def connect_to_db():
    try:
        with open("configuration/config.json") as config_file:
            config = json.load(config_file)
        connection = psycopg2.connect(
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"],
            database=config["database"]
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error al iniciar la base de datos", error)
        return None

def get_user_role_and_password(nombre, password, connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id_rol, id_sede, contrasena, id_usuario FROM usuario u WHERE u.nombre = %s;", (nombre,))
        result = cursor.fetchone()
        if result:
            if result[2] == password:
                globvar.id_usuario = result[3]
                return result[0], result[1]  # Devolver id_rol y id_sede
            else:
                return None, None, None  # Contraseña incorrecta
        else:
            return "Usuario no encontrado", None 
    except (Exception, psycopg2.Error) as error:
        print("Error al encontrar usuario", error)
        return None, None, None


def main():
    connection = connect_to_db()
    if connection is None:
        return

    intentos = 3
    while intentos > 0:
        nombre = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        id_rol, id_sede= get_user_role_and_password(nombre, password, connection)
        if id_rol == "Usuario no encontrado":
            print("Usuario no encontrado. Intente de nuevo.")
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")
        elif id_rol is not None:
            print("Inicio de sesión exitoso")
           
            if id_rol == 0:
                a.admin_menu()
                while True:
                    choice = input("Ingrese su elección: ")
                    a.handle_admin_choice(choice, connection)
                    cont = input("Desea realizar otra acción? (y/n): ")
                    if cont == 'n':
                        break
                    elif cont == 'y':
                        print("Regresando a menu")
                    else:
                        print('Entrada no valida, cerrando programa como opción por defecto')

            elif id_rol == 1:
                g.gerente_menu()
                while True:
                    choice = input("Ingrese su elección: ")
                    g.handle_gerente_choice(choice,id_sede, connection)
                    cont = input("Desea realizar otra acción? (y/n): ")
                    if cont == 'n':
                        break
                    elif cont == 'y':
                        print("Regresando a menu")
                    else:
                        print('Entrada no valida, cerrando programa como opción por defecto')
            elif id_rol == 2:
                c.cocina_menu()
                while True:
                    choice = input("Ingrese su elección: ")
                    c.handle_cocina_choice(choice,id_sede, connection)
                    cont = input("Desea realizar otra acción? (y/n): ")
                    if cont == 'n':
                        break
                    elif cont == 'y':
                        print("Regresando a menu")
                    else:
                        print('Entrada no valida, cerrando programa como opción por defecto')
            elif id_rol == 3:
                m.mesero_menu()
                while True:
                    choice = input("Ingrese su elección: ")
                    m.handle_mesero_choice(choice,id_sede, connection)
                    cont = input("Desea realizar otra acción? (y/n): ")
                    if cont == 'n':
                        break
                    elif cont == 'y':
                        print("Regresando a menu")
                    else:
                        print('Entrada no valida, cerrando programa como opción por defecto')
            return
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
    
    print("Has excedido el número de intentos. El programa se cerrará.")
    connection.close()

if __name__ == "__main__":
    main()