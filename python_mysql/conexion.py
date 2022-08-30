import mysql.connector

conexionBD = mysql.connector.connect(
    host = "localhost",
    user = "customer",
    password = "123456789"
)

print(conexionBD , "La conexion fue exitosa")