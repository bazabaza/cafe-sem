
-- Usuarios
INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASENIA, TIPO_USUARIO)
VALUES (1, 'Juan Pérez', 'juan.perez@example.com', 'contraseña123', 'cliente');

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASENIA, TIPO_USUARIO)
VALUES (2, 'María López', 'maria.lopez@example.com', 'admin1234', 'administrador');


INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASENIA, TIPO_USUARIO)
VALUES (3, 'Manuel Relinque', 'manuel.relinque@example.com', 'administrador2', 'administrador');

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASENIA, TIPO_USUARIO)
VALUES (4, 'Antonio Garcia', 'antonio.garcia@example.com', 'contraseña123', 'cliente');

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASENIA, TIPO_USUARIO)
VALUES (5, 'Julia Novoa', 'julia.novoa@example.com', 'contraseña123', 'cliente');

--clientes
INSERT INTO CLIENTES (ID_CLIENTE, TELEFONO)
VALUES (1, '600123456');

INSERT INTO CLIENTES (ID_CLIENTE, TELEFONO)
VALUES (4, '650987654'); 

INSERT INTO CLIENTES (ID_CLIENTE, TELEFONO)
VALUES (5, '690123789'); 

--administradores

INSERT INTO ADMINISTRADORES (ID_ADMINISTRADOR, ROL)
VALUES (2, 'Super Admin');

INSERT INTO ADMINISTRADORES (ID_ADMINISTRADOR, ROL)
VALUES (3, 'Super Admin');

--DIRECCIONES
INSERT INTO DIRECCIONES (ID_DIRECCION, ID_CLIENTE, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL, APODO_DIRECCION)
VALUES (1, 1, 'Calle Mayor', '10', 'Madrid', '28013', 'Casa');

INSERT INTO DIRECCIONES (ID_DIRECCION, ID_CLIENTE, CALLE, NUMERO, CIUDAD, CODIGO_POSTAL, APODO_DIRECCION)
VALUES (2, 1, 'Avenida de la Paz', '5', 'Barcelona', '08002', 'Oficina');


--productos

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN)
VALUES (1, 'Café en Grano Premium', 12.50, 100, 'cafe_en_grano_premium.jpg');

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN)
VALUES (2, 'Café Molido Clásico', 9.99, 200, 'cafe_molido_clasico.jpg');

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN)
VALUES (3, 'Cápsulas de Café Intenso', 15.99, 150, 'capsulas_cafe_intenso.jpg'); 

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN)
VALUES (4, 'Taza Cerámica Personalizada', 6.99, 50, 'taza_ceramica.jpg');

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK, IMAGEN)
VALUES (5, 'Cafetera Italiana', 29.99, 30, 'cafetera_italiana.jpg');

-- tipo categoria

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Café', 1, 'Bolsa de café en grano de alta calidad');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Café', 2, 'Café molido para cafeteras tradicionales');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Cápsulas', 3, 'Cápsulas compatibles con cafeteras');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Accesorios', 4, 'Tazas de cerámica para café');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Cafeteras', 5, 'Cafeteras italianas de diseño clásico');



-- pedido

INSERT INTO PEDIDOS (ID_PEDIDO, FECHA, ID_CLIENTE, ID_DIRECCION)
VALUES (1, TO_DATE('2024-12-01', 'YYYY-MM-DD'), 1, 1);

INSERT INTO PEDIDOS (ID_PEDIDO, FECHA, ID_CLIENTE, ID_DIRECCION)
VALUES (2, TO_DATE('2024-12-02', 'YYYY-MM-DD'), 1, 2);

-- detalle pedido

-- Pedido 1: Cliente compra café molido y una taza
INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (1, 1, 2, 2, 19.98);

INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (2, 1, 4, 1, 6.99); 

-- Pedido 2: Cliente compra cápsulas de café y una cafetera
INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (3, 2, 3, 3, 47.97);

INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (4, 2, 5, 1, 29.99); 



select * from user_errors where type = 'TRIGGER' and name = 'PEDIDOS_BI_TRIGGER' 
-- PLS-00103: Encountered the symbol "/" The symbol "/" was ignored.



commit;