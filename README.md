# connection-python-mssql

This Python script demonstrates how to establish a connection to a Microsoft SQL Server (MSSQL) database using the pyodbc library. The script defines two functions: establecer_conexion() (establish_connection) to set up the connection and cerrar_conexion(conexion) (close_connection) to close it. The connection parameters, such as server, database, username, and password, are specified in the establecer_conexion() function.

After establishing the connection, the script performs a simple SQL operation of adding 1 + 1 in the database. It uses a try-except block to handle any potential errors during the connection or SQL operation. The result of the addition is then fetched and printed. Finally, the connection is closed using the cerrar_conexion() function.

Users need to replace placeholders like 'tu_servidor' (your_server), 'tu_base_de_datos' (your_database), 'tu_usuario' (your_username), and 'tu_contraseña' (your_password) with their actual MSSQL server details. This script serves as a starting point for connecting to an MSSQL database using Python and can be expanded for more complex database operations.
