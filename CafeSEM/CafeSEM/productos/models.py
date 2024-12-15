import cx_Oracle
import requests

class Producto:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def listadoProductos(self):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN  FROM PRODUCTOS WHERE STOCK>0"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def listadoGestionProductos(self):
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
                            "VALUES (PRODUCTOS_SEQ.NEXTVAL, :P2, :P3, :P4, :P5, :P6, :P7)")

            datosAlta = (nombre, precio, stock, urlImagen, descripcion, categoriaCod)
            print(datosAlta)
            cursor.execute(ConsultaAlta, datosAlta)
            numeroRegistros = cursor.rowcount
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)
            numeroRegistros = error
        return numeroRegistros


    def bajaProducto(self, idProducto):
        cursor = self.connection.cursor()
        try:
            consulta = ("UPDATE productos SET STOCK='0' WHERE ID_PRODUCTO=:P1")

            cursor.execute(consulta, (idProducto,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def modificarProducto(self, nombre, precio, stock, urlImagen,  descripcion, categoriaCod, idProducto):
        cursor = self.connection.cursor()
        try:
            consulta = ("UPDATE productos SET NOMBRE=:P1, PRECIO=:P2, STOCK=:P3, IMAGEN=:P4, DESCRIPCION=:P5, ID_CATEGORIA=:P6 WHERE ID_PRODUCTO=:P7")

            cursor.execute(consulta, (nombre, precio, stock, urlImagen,  descripcion, categoriaCod, idProducto))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def bajarStock(self, idProducto, cantidad):
        cursor = self.connection.cursor()
        try:
            consulta = ("UPDATE productos SET STOCK=(select STOCK from productos where ID_PRODUCTO=:P1)-:P2 WHERE ID_PRODUCTO=:P3")

            cursor.execute(consulta, (idProducto,cantidad,idProducto))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor


class Categoria:

    def __init__(self):
            self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def listadoCategorias(self):
        cursor = self.connection.cursor()

        try:
            consulta = "SELECT id_categoria, descripcion FROM TIPO_CATEGORIA"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor


class Receta():

    def __init__(self):
        self.urlOrigen = "https://www.thecocktaildb.com/api/json/v1/1/"

    def listadoRecetas(self):
        url = "filter.php?i=coffee"
        response = requests.get(self.urlOrigen + url)
        jsonResponse = response.json()
        listado = jsonResponse['drinks']

        return listado

    def elaboracionReceta(self, idReceta):
        url = "lookup.php?i="+ idReceta

        response = requests.get(self.urlOrigen + url)
        jsonResponse = response.json()
        listado = jsonResponse['drinks']

        return listado





