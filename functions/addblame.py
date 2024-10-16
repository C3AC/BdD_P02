import globvar

def blaming(cursor):

    try:
        query = '''
            SELECT MAX(id_cambio) FROM cambios;
        '''
        cursor.execute(query)
        id_cambio = cursor.fetchone()[0]
        query = '''
            UPDATE cambios
            SET usuario_responsable = %s
            WHERE id_cambio = %s;
        '''
        cursor.execute(query, (globvar.id_usuario, id_cambio))
        cursor.connection.commit()      
    except Exception as e:
        print(f"Error: {e}")
        cursor.connection.rollback()
    finally:
        cursor.close()