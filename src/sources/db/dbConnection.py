import psycopg2

def connection():
    
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '123456',
            database = 'Parqueadero'
        )

        cursor = connection.cursor()
        return cursor

    except Exception:
        print("Error conexión en base de datos")