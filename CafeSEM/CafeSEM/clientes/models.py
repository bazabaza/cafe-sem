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

    def get_usuario_id(self, email):
        cursor = self.get_usuario(email)
        row = cursor.fetchone()
        return row[0]

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

    def insertar_direccion(self, params):
        cursor = self.connection.cursor()
        print(params)

        sql = ("INSERT INTO DIRECCIONES "
               "(ID_DIRECCION, ID_CLIENTE, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL, APODO_DIRECCION) "
               "VALUES (DIRECCIONES_SEQ.NEXTVAL, :id_cliente, :calle, :numero, :ciudad, :codigo_postal, :apodo_direccion)")
        try:
            cursor.execute(sql, params)
            self.connection.commit()
        except self.connection.Error as error:
            print("Error: ", error)
            return False

        return cursor

    def eliminar_direccion(self, id_direccion):
        cursor = self.connection.cursor()

        try:
            consulta = "DELETE FROM DIRECCIONES WHERE ID_DIRECCION = :id_direccion"
            cursor.execute(consulta, {"id_direccion": id_direccion})
        except self.connection.Error as error:
            print("Error: ", error)

        if cursor.rowcount > 0:
            self.connection.commit()

        return cursor.rowcount

    def get_direcciones_by_id(self, user_id):
        cursor = self.connection.cursor()

        sql = (f"SELECT ID_DIRECCION, ID_CLIENTE, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL, APODO_DIRECCION "
               f"FROM DIRECCIONES WHERE ID_CLIENTE = (SELECT ID_USUARIO FROM USUARIOS WHERE ID_USUARIO=:user_id)")
        try:
            cursor.execute(sql, {"user_id": user_id})
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
               "AND P.ESTADO = 'terminado' "
               "GROUP BY P.ID_PEDIDO, P.FECHA ORDER BY P.FECHA")

        try:
            cursor.execute(sql, {"email": email})
        except self.connection.Error as error:
            print("Error: ", error)
            return False

        return cursor
