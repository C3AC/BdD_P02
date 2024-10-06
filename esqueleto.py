import psycopg2
import json
import menu.admin as a
import menu.gerente as g
import menu.cocina as c
import menu.mesero as m

def connect_to_db():
    try:
        # Leer las credenciales desde el archivo config.json
        with open('config.json', 'r') as config_file:
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

def get_user_role_and_password(user_id, password, connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id_rol, id_sede, contraseña FROM usuarios WHERE id_usuario = %s;", (user_id,))
        result = cursor.fetchone()
        if result and result[2] == password:
            return result[0], result[1]  # Devolver id_rol y id_sede
        else:
            return None, None
    except (Exception, psycopg2.Error) as error:
        print("Error al encontrar usuario", error)
        return None, None

def main():
    connection = connect_to_db()
    if not connection:
        print("Exiting...")
        return

    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    user_role, user_sede = get_user_role_and_password(user_id, password, connection)

    if user_role is None:
        print("Invalid user ID or password")
        return

    while True:
        if user_role == 0:  # Admin
            a.admin_menu()
            choice = input("Enter your choice: ")
            if not a.handle_admin_choice(choice):
                break
        elif user_role == 1:  # Gerente
            g.gerente_menu()
            choice = input("Enter your choice: ")
            if not g.handle_gerente_choice(choice, user_sede):
                break
        elif user_role == 2:  # Cocina
            c.cocina_menu()
            choice = input("Enter your choice: ")
            if not c.handle_cocina_choice(choice, user_sede):
                break
        elif user_role == 3:  # Mesero
            m.mesero_menu()
            choice = input("Enter your choice: ")
            if not m.handle_mesero_choice(choice, user_sede):
                break
        else:
            print("Invalid role")
            break

    connection.close()
    print("PostgreSQL connection is closed")

if __name__ == "__main__":
    main()