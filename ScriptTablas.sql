CREATE TABLE USUARIOS (
	ID_USUARIO NUMBER(4) PRIMARY KEY,
	NOMBRE VARCHAR2(100) NOT NULL,
	EMAIL VARCHAR2(150) NOT NULL UNIQUE,
	CONTRASENIA VARCHAR2(150) NOT NULL,
	TIPO_USUARIO VARCHAR2(50) NOT NULL
	);
	
CREATE SEQUENCE USUARIOS_SEQ
START WITH 1 
INCREMENT BY 1;

CREATE OR REPLACE TRIGGER USUARIOS_BI_TRIGGER
BEFORE INSERT ON USUARIOS
FOR EACH ROW
BEGIN
    IF :NEW.ID_USUARIO IS NULL THEN
        :NEW.ID_USUARIO := USUARIOS_SEQ.NEXTVAL; 
    END IF;
END;

/

CREATE TABLE ADMINISTRADORES (
    ID_ADMINISTRADOR NUMBER PRIMARY KEY,
    ROL VARCHAR2(50) NOT NULL,
  
    CONSTRAINT FK_ADMIN_USUARIO FOREIGN KEY (ID_ADMINISTRADOR) REFERENCES USUARIOS(ID_USUARIO)
);

CREATE TABLE CLIENTES (
    ID_CLIENTE NUMBER PRIMARY KEY,
    TELEFONO VARCHAR2(15) NOT NULL,
   
    CONSTRAINT FK_CLIENTE_USUARIO FOREIGN KEY (ID_CLIENTE) REFERENCES USUARIOS(ID_USUARIO)
);

CREATE TABLE DIRECCIONES (
    ID_DIRECCION NUMBER PRIMARY KEY,
    ID_CLIENTE NUMBER NOT NULL,
    CALLE VARCHAR2(150) NOT NULL,
    NUMERO VARCHAR2(10) NOT NULL,
    CIUDAD VARCHAR2(100) NOT NULL,
    CODIGO_POSTAL VARCHAR2(10) NOT NULL,
    APODO_DIRECCION VARCHAR2(50),

    CONSTRAINT FK_DIRECCION_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE)
);

CREATE SEQUENCE DIRECCIONES_SEQ
    START WITH 1
    INCREMENT BY 1;
	
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
    ID_PEDIDO NUMBER PRIMARY KEY,
    FECHA DATE NOT NULL,
    ID_CLIENTE NUMBER NOT NULL,
    ID_DIRECCION NUMBER NOT NULL,

    
    CONSTRAINT FK_PEDIDO_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE),
    CONSTRAINT FK_PEDIDO_DIRECCION FOREIGN KEY (ID_DIRECCION) REFERENCES DIRECCIONES(ID_DIRECCION)
);

 CREATE SEQUENCE PEDIDOS_SEQ
  START WITH 1
  INCREMENT BY 1;
  
 CREATE OR REPLACE TRIGGER PEDIDOS_BI_TRIGGER
  BEFORE INSERT ON PEDIDOS
  FOR EACH ROW
  BEGIN
      IF :NEW.ID_PEDIDO IS NULL THEN
          :NEW.ID_PEDIDO := PEDIDOS_SEQ.NEXTVAL;
      END IF;
  END;

/

CREATE TABLE TIPO_CATEGORIA (
    ID_CATEGORIA NUMBER PRIMARY KEY,
    DESCRIPCION VARCHAR2(255)
);

CREATE TABLE PRODUCTOS (
    ID_PRODUCTO NUMBER PRIMARY KEY,
    NOMBRE VARCHAR2(100) NOT NULL,
    PRECIO NUMBER(10, 2) NOT NULL,
    STOCK NUMBER(10) DEFAULT 0 NOT NULL,
	IMAGEN VARCHAR2(255),
	DESCRIPCION VARCHAR2(255),
	ID_CATEGORIA NUMBER NOT NULL,

	CONSTRAINT FK_CATEGORIAS_PRODUCTOS FOREIGN KEY (ID_CATEGORIA) REFERENCES TIPO_CATEGORIA(ID_CATEGORIA)
);

CREATE SEQUENCE PRODUCTOS_SEQ
START WITH 1
INCREMENT BY 1;

CREATE OR REPLACE TRIGGER PRODUCTOS_BI_TRIGGER
BEFORE INSERT ON PRODUCTOS
FOR EACH ROW
BEGIN
    IF :NEW.ID_PRODUCTO IS NULL THEN
        :NEW.ID_PRODUCTO := PRODUCTOS_SEQ.NEXTVAL;
    END IF;
END;


CREATE TABLE DETALLE_PEDIDO (
    ID_DETALLE NUMBER PRIMARY KEY,
    ID_PEDIDO NUMBER NOT NULL,
    ID_PRODUCTO NUMBER NOT NULL,
    CANTIDAD NUMBER(10) NOT NULL,
    PRECIO_TOTAL NUMBER(10, 2) NOT NULL,

    CONSTRAINT FK_DETALLE_PEDIDO FOREIGN KEY (ID_PEDIDO) REFERENCES PEDIDOS(ID_PEDIDO),
    CONSTRAINT FK_DETALLE_PRODUCTO FOREIGN KEY (ID_PRODUCTO) REFERENCES PRODUCTOS(ID_PRODUCTO)
);

  CREATE SEQUENCE DETALLE_PEDIDO_SEQ
  START WITH 1
  INCREMENT BY 1;

  CREATE OR REPLACE TRIGGER DETALLE_PEDIDO_BI_TRIGGER
  BEFORE INSERT ON DETALLE_PEDIDO
  FOR EACH ROW
  BEGIN
      IF :NEW.ID_DETALLE IS NULL THEN
          :NEW.ID_DETALLE := DETALLE_PEDIDO_SEQ.NEXTVAL;
      END IF;
  END;