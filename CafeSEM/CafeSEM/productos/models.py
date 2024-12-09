import cx_Oracle

class Producto:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def listadoProductos(self):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN  FROM PRODUCTOS"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor