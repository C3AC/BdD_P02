import psycopg2
import json
from menu import admin as a
from menu import gerente as g
from menu import cocina as c
from menu import mesero as m

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
        cursor.execute("SELECT id_rol, id_sede, contrasena FROM usuario u WHERE u.nombre = %s;", (nombre,))
        result = cursor.fetchone()
        if result:
            if result[2] == password:
                return result[0], result[1]  # Devolver id_rol y id_sede
            else:
                return None, None  # Contraseña incorrecta
        else:
            return "Usuario no encontrado", None  # Usuario no encontrado
    except (Exception, psycopg2.Error) as error:
        print("Error al encontrar usuario", error)
        return None, None


def main():
    connection = connect_to_db()
    if connection is None:
        return

    intentos = 3
    while intentos > 0:
        nombre = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        id_rol, id_sede = get_user_role_and_password(nombre, password, connection)
        if id_rol == "Usuario no encontrado":
            print("Usuario no encontrado. Intente de nuevo.")
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")
        elif id_rol is not None:
            print("Inicio de sesión exitoso")
            if id_rol == 0:
                a.admin_menu()
                choice = input("Ingrese su elección: ")
                a.handle_admin_choice(choice, connection)
            elif id_rol == 1:
                g.gerente_menu()
                choice = input("Ingrese su elección: ")
                g.handle_gerente_choice(choice,id_sede, connection)
            elif id_rol == 2:
                c.cocina_menu()
                choice = input("Ingrese su elección: ")
                c.handle_cocina_choice(choice,id_sede, connection)
            elif id_rol == 3:
                m.mesero_menu()
                choice = input("Ingrese su elección: ")
                m.handle_mesero_choice(choice,id_sede, connection)
            return
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
    
    print("Has excedido el número de intentos. El programa se cerrará.")
    connection.close()

if __name__ == "__main__":
    main()