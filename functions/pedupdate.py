from tabulate import tabulate
from functions.resupdate import addreservation

def order(cursor, id_sede):
    print('Seleccione una sede: ')
    query = '''
        SELECT id_reserva, r.id_mesa
        FROM reserva r JOIN mesa m on r.id_mesa = m.id_mesa
        WHERE r.id_sede = %s
        AND r.fecha_reserva = CURRENT_DATE
        AND r.id_reserva NOT IN (SELECT id_reserva FROM pedido)
    '''
    cursor.execute(query, (id_sede,))
    reservations = cursor.fetchall()
    print('Reservaciones para hoy: ')
    print(tabulate(reservations, headers=['ID Reserva', 'ID Mesa']))
    if reservations == []:
        print('No hay reservaciones para hoy, ingrese una reservacion antes de empezar un pedido')
        id_reserva = addreservation(cursor, id_sede)
    else:
        print('Seleccione una reservación: ')
        flag = True
        while flag:
            try:
                id_reserva = int(input())
                query = '''
                    SELECT id_reserva
                    FROM reserva
                    WHERE id_reserva = %s
                '''
                cursor.execute(query, (id_reserva,))
                reservation = cursor.fetchone()
                if reservation is None:
                    print('Reservación no encontrada')
                    return
                else:
                    flag = False
            except ValueError:
                print('Entrada inválida')
                return
    query = '''
            INSERT INTO pedido (id_reserva, id_pedido, total)
            VALUES (%s, %s, 0)
        '''
    cursor.execute(query, (id_reserva, id_reserva))
    print('Pedido creado exitosamente')
    input('Presione enter para empezar a agregar productos al pedido')
    return id_reserva