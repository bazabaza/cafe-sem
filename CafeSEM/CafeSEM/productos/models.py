import cx_Oracle

class Producto:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "Mananas", "localhost/XE")

    def listadoProductos(self):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN  FROM PRODUCTOS"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def detalleProducto(self, id):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN, DESCRIPCION, ID_CATEGORIA"
            consulta += " FROM PRODUCTOS WHERE ID_PRODUCTO = "+ str(id)
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def altaProducto(self, nombre, precio, stock, urlImagen,  descripcion, categoriaCod):
        cursor = self.connection.cursor()
        try:
            ConsultaAlta = ("INSERT INTO productos (ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN, DESCRIPCION, ID_CATEGORIA)"
                            "VALUES (:P1, :P2, :P3, :P4, :P5, :P6, :P7)")

            datosAlta = (6,nombre, precio, stock, urlImagen, descripcion, categoriaCod)
            print(datosAlta)
            cursor.execute(ConsultaAlta, datosAlta)
            numeroRegistros = cursor.rowcount
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)
            numeroRegistros = error
        return numeroRegistros


class Categoria:

    def __init__(self):
            self.connection = cx_Oracle.connect("system", "Mananas", "localhost/XE")

    def listadoCategorias(self):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT id_categoria, descripcion FROM TIPO_CATEGORIA"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor





