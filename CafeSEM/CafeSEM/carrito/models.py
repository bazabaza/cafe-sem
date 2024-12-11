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

    def getDirecciones(self, idUsuario):
        cursor = self.connection.cursor()

        try:
            consulta = ("SELECT ID_DIRECCION, APODO_DIRECCION, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL "
                        "FROM DIRECCIONES WHERE ID_CLIENTE =" + str(idUsuario))

            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def cambiarDireccion(self, nuevaDireccion):
        cursor = self.connection.cursor()
        mensaje = "-1"

        try:
            consulta = "UPDATE PEDIDOS SET ID_DIRECCION = :p1 WHERE ID_PEDIDO = :p2"

            cursor.execute(consulta, nuevaDireccion)

            if cursor.rowcount > 0:
                mensaje = "0"
            else:
                mensaje = "-1"

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        cursor.close()
        self.connection.close()

        return mensaje

    def terminarPedido(self, datos):
        cursor = self.connection.cursor()
        mensaje = "-1"

        try:
            consulta = "UPDATE PEDIDOS SET ESTADO = 'finalizado' WHERE ID_PEDIDO = :p1"

            cursor.execute(consulta, datos)

            if cursor.rowcount > 0:
                mensaje = "0"
            else:
                mensaje = "-1"

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        cursor.close()
        self.connection.close()

        return mensaje

    def getIdPedido(self, idUsuario):
        cursor = self.connection.cursor()

        try:
            consulta = ("select ID_PEDIDO from pedidos where id_cliente = "+ str(idUsuario) +" and estado = 'pendiente'")

            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def addProducto(self, datos):
        cursor = self.connection.cursor()
        mensaje = ""

        try:
            consulta = "INSERT INTO DETALLE_PEDIDO(ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)"
            consulta += " VALUES (DETALLE_PEDIDO_SEQ.NEXTVAL, :p1, :p2, :p3, :p4 )"

            print(consulta)

            cursor.execute(consulta, datos)

            if cursor.rowcount > 0:
                mensaje = "Datos insertados satisfactoriamente"
            else:
                mensaje = "Error, no se han podido insertar los datos"

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        cursor.close()
        self.connection.close()

        return mensaje

class Pedido:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")


    def pedidosAdmin(self):

        cursor = self.connection.cursor()

        try:
            consulta = ("SELECT p.id_pedido, p.id_cliente, SUM(d.precio_total) AS Total_Pedido, dir.ciudad FROM pedidos p "
                        " INNER JOIN detalle_pedido d ON p.id_pedido=d.id_pedido"
                        " INNER JOIN usuarios u ON p.id_cliente=u.id_usuario"
                        " INNER JOIN direcciones dir ON p.id_direccion=dir.id_direccion"
                        " GROUP BY P.ID_PEDIDO, P.ID_CLIENTE, dir.ciudad"
                        " ORDER BY p.id_pedido")

            cursor.execute(consulta)


        except self.connection.Error as error:
            print("Error: ", error)

        return cursor