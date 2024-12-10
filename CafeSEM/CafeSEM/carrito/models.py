import cx_Oracle

class Carrito:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def detallePedido(self, idPedido):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT D.ID_DETALLE, D.ID_PEDIDO, P.NOMBRE, P.PRECIO, P.IMAGEN, D.CANTIDAD, D.PRECIO_TOTAL"
            consulta += " FROM DETALLE_PEDIDO D LEFT OUTER JOIN PRODUCTOS P ON D.ID_PRODUCTO = P.ID_PRODUCTO"
            consulta += " WHERE D.ID_PEDIDO = " + str(idPedido)

            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def idsEnvio(self, idPedido):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT ID_CLIENTE, ID_DIRECCION, ID_PEDIDO FROM PEDIDOS WHERE ID_PEDIDO = " + str(idPedido)

            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def getDatosDireccionActual(self, idPedido):
        cursor = self.connection.cursor()

        try:
            consulta = ("SELECT NOMBRE, TELEFONO, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL, APODO_DIRECCION"
                        " FROM PEDIDOS P INNER JOIN CLIENTES C ON P.ID_CLIENTE = C.ID_CLIENTE"
                        " INNER JOIN DIRECCIONES D ON P.ID_DIRECCION = D.ID_DIRECCION"
                        " INNER JOIN USUARIOS U ON C.ID_CLIENTE = U.ID_USUARIO"
                        " WHERE P.ID_PEDIDO = " + str(idPedido))

            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor