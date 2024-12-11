import cx_Oracle

class Usuario:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def get_usuario(self, email):
        cursor = self.connection.cursor()

        sql = f"SELECT ID_USUARIO, NOMBRE, EMAIL, CONTRASENIA, TIPO_USUARIO FROM USUARIOS WHERE EMAIL=:email"
        try:
            cursor.execute(sql, {"email": email})
        except self.connection.Error as error:
            print("Error: ", error)
            return False

        return cursor

    def get_direcciones(self, email):
        cursor = self.connection.cursor()

        sql = (f"SELECT ID_DIRECCION, ID_CLIENTE, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL, APODO_DIRECCION "
               f"FROM DIRECCIONES WHERE ID_CLIENTE = (SELECT ID_USUARIO FROM USUARIOS WHERE EMAIL=:email)")
        try:
            cursor.execute(sql, {"email": email})
        except self.connection.Error as error:
            print("Error: ", error)
            return False

        return cursor

class Pedidos:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def get_pedidos(self, email):
        cursor = self.connection.cursor()

        sql = ("SELECT P.ID_PEDIDO, P.FECHA, SUM(DP.PRECIO_TOTAL) AS PRECIO_TOTAL FROM "
               "PEDIDOS P JOIN DETALLE_PEDIDO DP ON P.ID_PEDIDO = DP.ID_PEDIDO "
               "WHERE P.ID_CLIENTE = (SELECT ID_USUARIO FROM USUARIOS WHERE EMAIL=:email) "
               "GROUP BY P.ID_PEDIDO, P.FECHA ORDER BY P.FECHA")

        try:
            cursor.execute(sql, {"email": email})
        except self.connection.Error as error:
            print("Error: ", error)
            return False

        return cursor
