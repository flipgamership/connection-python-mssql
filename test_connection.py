import pyodbc

def establecer_conexion():
    try:
        # Configuración de la conexión a la base de datos
        server = 'connection'
        database = 'db'
        username = 'user'
        password = 'password'


        # Cadena de conexión
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establecer la conexión
        conexion = pyodbc.connect(connection_string)

        print("Conexión establecida correctamente.")

        # Devolver la conexión para su uso
        return conexion

    except Exception as e:
        print(f"Error al establecer la conexión: {str(e)}")
        return None

def cerrar_conexion(conexion):
    try:
        # Cerrar la conexión
        conexion.close()
        print("Conexión cerrada correctamente.")
    except Exception as e:
        print(f"Error al cerrar la conexión: {str(e)}")

# Ejemplo de uso
conexion = establecer_conexion()

# Realizar una operación de suma en la base de datos (1 + 1)
try:
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 + 1 AS Suma")
    resultado = cursor.fetchone()
    print(f"Resultado de la suma en la base de datos: {resultado.Suma}")
except Exception as e:
    print(f"Error al realizar la operación de suma: {str(e)}")
finally:
    if 'cursor' in locals():
        cursor.close()

# Cerrar la conexión al finalizar
cerrar_conexion(conexion)