import cx_Oracle

class Usario:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def get_usario(self, email):
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


    def get_pedidos(self, email):
        pass