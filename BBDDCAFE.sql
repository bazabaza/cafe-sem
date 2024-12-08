-- Crear la tabla USUARIOS
CREATE TABLE USUARIOS (
    ID_USUARIO NUMBER PRIMARY KEY, -- Clave primaria
    NOMBRE VARCHAR2(100) NOT NULL, -- Nombre del usuario
    EMAIL VARCHAR2(150) NOT NULL UNIQUE, -- Correo electrónico único
    CONTRASEÑA VARCHAR2(150) NOT NULL, -- Contraseña
    TIPO_USUARIO VARCHAR2(50) NOT NULL -- Tipo de usuario (ej: admin, cliente)
);

-- Crear una secuencia para generar valores automáticos para ID_USUARIO
CREATE SEQUENCE USUARIOS_SEQ
START WITH 1 -- Inicia desde el número 1
INCREMENT BY 1; -- Incrementa en 1 cada vez

-- Crear un trigger para asignar automáticamente el ID_USUARIO
CREATE OR REPLACE TRIGGER USUARIOS_BI_TRIGGER
BEFORE INSERT ON USUARIOS
FOR EACH ROW
BEGIN
    IF :NEW.ID_USUARIO IS NULL THEN
        :NEW.ID_USUARIO := USUARIOS_SEQ.NEXTVAL; -- Asigna el siguiente valor de la secuencia
    END IF;
END;
/

CREATE TABLE ADMINISTRADORES (
    ID_ADMINISTRADOR NUMBER PRIMARY KEY, -- Clave primaria que es a la vez clave foránea
    ROL VARCHAR2(50) NOT NULL, -- Rol del administrador

    -- Clave foránea que enlaza con la tabla USUARIOS
    CONSTRAINT FK_ADMIN_USUARIO FOREIGN KEY (ID_ADMINISTRADOR) REFERENCES USUARIOS(ID_USUARIO)
);


CREATE TABLE CLIENTES (
    ID_CLIENTE NUMBER PRIMARY KEY, -- Clave primaria que es a la vez clave foránea
    TELEFONO VARCHAR2(15) NOT NULL, -- Teléfono del cliente

    -- Clave foránea que enlaza con la tabla USUARIOS
    CONSTRAINT FK_CLIENTE_USUARIO FOREIGN KEY (ID_CLIENTE) REFERENCES USUARIOS(ID_USUARIO)
);


CREATE TABLE PRODUCTOS (
    ID_PRODUCTO NUMBER PRIMARY KEY, -- Clave primaria
    NOMBRE VARCHAR2(100) NOT NULL, -- Nombre del producto
    PRECIO NUMBER(10, 2) NOT NULL, -- Precio del producto (2 decimales)
    STOCK NUMBER(10) DEFAULT 0 NOT NULL -- Cantidad en stock, valor predeterminado 0
);


CREATE TABLE DIRECCIONES (
    ID_DIRECCION NUMBER PRIMARY KEY, -- Clave primaria
    ID_CLIENTE NUMBER NOT NULL, -- Clave foránea que enlaza con CLIENTES
    CALLE VARCHAR2(150) NOT NULL, -- Nombre de la calle
    NUMERO VARCHAR2(10) NOT NULL, -- Número del domicilio
    CIUDAD VARCHAR2(100) NOT NULL, -- Ciudad
    CODIGO_POSTAL VARCHAR2(10) NOT NULL, -- Código postal
    APODO_DIRECCION VARCHAR2(50), -- Apodo para la dirección (ej. Casa, Trabajo)

    -- Definir la clave foránea con CLIENTES
    CONSTRAINT FK_DIRECCION_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE)
);

    -- Secuencia para autoincrementar ID_DIRECCION
    CREATE SEQUENCE DIRECCIONES_SEQ
    START WITH 1
    INCREMENT BY 1;

    -- Trigger para asignar automáticamente el ID_DIRECCION
    CREATE OR REPLACE TRIGGER DIRECCIONES_BI_TRIGGER
    BEFORE INSERT ON DIRECCIONES
    FOR EACH ROW
    BEGIN
        IF :NEW.ID_DIRECCION IS NULL THEN
            :NEW.ID_DIRECCION := DIRECCIONES_SEQ.NEXTVAL;
        END IF;
    END;
    /


CREATE TABLE PEDIDOS (
    ID_PEDIDO NUMBER PRIMARY KEY, -- Clave primaria
    FECHA DATE NOT NULL, -- Fecha del pedido
    ID_CLIENTE NUMBER NOT NULL, -- Clave foránea que enlaza con CLIENTES
    ID_DIRECCION NUMBER NOT NULL, -- Clave foránea que enlaza con DIRECCIONES

    -- Clave foránea para enlazar con CLIENTES
    CONSTRAINT FK_PEDIDO_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE),

    -- Clave foránea para enlazar con DIRECCIONES
    CONSTRAINT FK_PEDIDO_DIRECCION FOREIGN KEY (ID_DIRECCION) REFERENCES DIRECCIONES(ID_DIRECCION)
);

  -- Secuencia para autoincrementar ID_PEDIDO
  CREATE SEQUENCE PEDIDOS_SEQ
  START WITH 1
  INCREMENT BY 1;

  -- Trigger para asignar automáticamente el ID_PEDIDO
  CREATE OR REPLACE TRIGGER PEDIDOS_BI_TRIGGER
  BEFORE INSERT ON PEDIDOS
  FOR EACH ROW
  BEGIN
      IF :NEW.ID_PEDIDO IS NULL THEN
          :NEW.ID_PEDIDO := PEDIDOS_SEQ.NEXTVAL;
      END IF;
  END;

CREATE TABLE DETALLE_PEDIDO (
    ID_DETALLE NUMBER PRIMARY KEY, -- Clave primaria
    ID_PEDIDO NUMBER NOT NULL, -- Clave foránea que enlaza con PEDIDOS
    ID_PRODUCTO NUMBER NOT NULL, -- Clave foránea que enlaza con PRODUCTOS
    CANTIDAD NUMBER(10) NOT NULL, -- Cantidad del producto en el pedido
    PRECIO_TOTAL NUMBER(10, 2) NOT NULL, -- Precio total de este detalle del pedido

    -- Clave foránea para enlazar con PEDIDOS
    CONSTRAINT FK_DETALLE_PEDIDO FOREIGN KEY (ID_PEDIDO) REFERENCES PEDIDOS(ID_PEDIDO),

    -- Clave foránea para enlazar con PRODUCTOS
    CONSTRAINT FK_DETALLE_PRODUCTO FOREIGN KEY (ID_PRODUCTO) REFERENCES PRODUCTOS(ID_PRODUCTO)
);

  -- Secuencia para autoincrementar ID_DETALLE
  CREATE SEQUENCE DETALLE_PEDIDO_SEQ
  START WITH 1
  INCREMENT BY 1;

  -- Trigger para asignar automáticamente el ID_DETALLE
  CREATE OR REPLACE TRIGGER DETALLE_PEDIDO_BI_TRIGGER
  BEFORE INSERT ON DETALLE_PEDIDO
  FOR EACH ROW
  BEGIN
      IF :NEW.ID_DETALLE IS NULL THEN
          :NEW.ID_DETALLE := DETALLE_PEDIDO_SEQ.NEXTVAL;
      END IF;
  END;
  

CREATE TABLE TIPO_CATEGORIA (
    CATEGORIA VARCHAR2(50) PRIMARY KEY, -- Clave primaria para la categoría
    ID_PRODUCTO NUMBER NOT NULL, -- Clave foránea que enlaza con PRODUCTOS
    DESCRIPCION VARCHAR2(255), -- Descripción de la categoría

    -- Clave foránea para enlazar con PRODUCTOS
    CONSTRAINT FK_CATEGORIA_PRODUCTO FOREIGN KEY (ID_PRODUCTO) REFERENCES PRODUCTOS(ID_PRODUCTO)
);


CREATE TABLE TIPO_CATEGORIA (
    CATEGORIA VARCHAR2(50) , -- Identificador único para la categoría
    ID_PRODUCTO NUMBER NOT NULL, -- Clave foránea que enlaza con PRODUCTOS
    DESCRIPCION VARCHAR2(255), -- Descripción de la categoría

    -- Clave primaria compuesta por CATEGORIA e ID_PRODUCTO
    CONSTRAINT PK_TIPO_CATEGORIA PRIMARY KEY (CATEGORIA, ID_PRODUCTO),

    -- Clave foránea para enlazar con PRODUCTOS
    CONSTRAINT FK_CATEGORIA_PRODUCTO FOREIGN KEY (ID_PRODUCTO) REFERENCES PRODUCTOS(ID_PRODUCTO)
);



