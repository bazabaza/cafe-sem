
-- Usuarios
INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASE�A, TIPO_USUARIO)
VALUES (1, 'Juan P�rez', 'juan.perez@example.com', 'contrase�a123', 'cliente');

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASE�A, TIPO_USUARIO)
VALUES (2, 'Mar�a L�pez', 'maria.lopez@example.com', 'admin1234', 'administrador');


INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASE�A, TIPO_USUARIO)
VALUES (3, 'Manuel Relinque', 'manuel.relinque@example.com', 'administrador2', 'administrador');

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASE�A, TIPO_USUARIO)
VALUES (4, 'Antonio Garcia', 'antonio.garcia@example.com', 'contrase�a123', 'cliente');

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE, EMAIL, CONTRASE�A, TIPO_USUARIO)
VALUES (5, 'Julia Novoa', 'julia.novoa@example.com', 'contrase�a123', 'cliente');

--clientes
INSERT INTO CLIENTES (ID_CLIENTE, TELEFONO)
VALUES (1, '600123456');

INSERT INTO CLIENTES (ID_CLIENTE, TELEFONO)
VALUES (4, '650987654'); -- Cliente con un nuevo n�mero de tel�fono

INSERT INTO CLIENTES (ID_CLIENTE, TELEFONO)
VALUES (5, '690123789'); -- Otro cliente con un n�mero diferente

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

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK)
VALUES (1, 'Caf� en Grano Premium', 12.50, 100); -- Bolsa de caf� en grano

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK)
VALUES (2, 'Caf� Molido Cl�sico', 9.99, 200); -- Caf� molido

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK)
VALUES (3, 'C�psulas de Caf� Intenso', 15.99, 150); -- C�psulas compatibles con cafeteras

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK)
VALUES (4, 'Taza Cer�mica Personalizada', 6.99, 50); -- Taza personalizada para caf�

INSERT INTO PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, STOCK)
VALUES (5, 'Cafetera Italiana', 29.99, 30); -- Cafetera de estilo tradicional

-- tipo categoria

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Caf�', 1, 'Bolsa de caf� en grano de alta calidad');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Caf�', 2, 'Caf� molido para cafeteras tradicionales');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('C�psulas', 3, 'C�psulas compatibles con cafeteras');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Accesorios', 4, 'Tazas de cer�mica para caf�');

INSERT INTO TIPO_CATEGORIA (CATEGORIA, ID_PRODUCTO, DESCRIPCION)
VALUES ('Cafeteras', 5, 'Cafeteras italianas de dise�o cl�sico');



-- pedido

INSERT INTO PEDIDOS (ID_PEDIDO, FECHA, ID_CLIENTE, ID_DIRECCION)
VALUES (1, TO_DATE('2024-12-01', 'YYYY-MM-DD'), 1, 1);

INSERT INTO PEDIDOS (ID_PEDIDO, FECHA, ID_CLIENTE, ID_DIRECCION)
VALUES (2, TO_DATE('2024-12-02', 'YYYY-MM-DD'), 1, 2);

-- detalle pedido

-- Pedido 1: Cliente compra caf� molido y una taza
INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (1, 1, 2, 2, 19.98); -- 2 bolsas de caf� molido

INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (2, 1, 4, 1, 6.99); -- 1 taza personalizada

-- Pedido 2: Cliente compra c�psulas de caf� y una cafetera
INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (3, 2, 3, 3, 47.97); -- 3 paquetes de c�psulas

INSERT INTO DETALLE_PEDIDO (ID_DETALLE, ID_PEDIDO, ID_PRODUCTO, CANTIDAD, PRECIO_TOTAL)
VALUES (4, 2, 5, 1, 29.99); -- 1 cafetera italiana



select * from user_errors where type = 'TRIGGER' and name = 'PEDIDOS_BI_TRIGGER' 
-- PLS-00103: Encountered the symbol "/" The symbol "/" was ignored.



commit;
