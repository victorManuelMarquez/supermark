-- Autor: Víctor Manuel Márquez

-- Tablas

CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT(10) NOT NULL,
    nombre_completo TEXT(140) NOT NULL,
    activo INTEGER NOT NULL DEFAULT 1 -- actúa como booleano
);

CREATE TABLE IF NOT EXISTS categorias(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre TEXT(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS productos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_categoria INTEGER NOT NULL,
	descripcion TEXT(140) NOT NULL,
	activo INTEGER NOT NULL DEFAULT 1,
	CONSTRAINT FK_PROD_CAT FOREIGN KEY (id_categoria) 
        REFERENCES categorias(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS articulos(
	id_producto INTEGER PRIMARY KEY,
	precio REAL NOT NULL,
	stock INTEGER NOT NULL,
	CONSTRAINT FK_ART_PROD FOREIGN KEY (id_producto)
        REFERENCES productos(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS empleados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT(10) NOT NULL,
    nombre_completo TEXT(140) NOT NULL,
    activo INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS ventas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_articulo INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL,
    fecha TEXT(30) NOT NULL,
    precio REAL NOT NULL,
    CONSTRAINT FK_COMPRA_ART FOREIGN KEY (id_articulo)
        REFERENCES articulos(id_producto) ON UPDATE CASCADE,
    CONSTRAINT FK_COMPRA_CLI FOREIGN KEY (id_cliente)
        REFERENCES clientes(id) ON UPDATE CASCADE,
    CONSTRAINT FK_COMPRA_EMP FOREIGN KEY (id_empleado)
        REFERENCES empleados(id) ON UPDATE CASCADE
);

-- Índices

CREATE INDEX IF NOT EXISTS FECHA_DE_COMPRA ON ventas(fecha);

-- vistas

DROP VIEW IF EXISTS articulos_detalles;

CREATE VIEW articulos_detalles AS
    SELECT
        productos.id as 'ID',
        categorias.nombre as 'Categoría',
        productos.descripcion as 'Descripción',
        articulos.precio as 'Precio',
        articulos.stock as 'Stock',
        productos.activo as 'Activo'
    FROM (
        (articulos INNER JOIN productos ON articulos.id_producto = productos.id) 
            INNER JOIN categorias ON categorias.id = productos.id_categoria
    );

DROP VIEW IF EXISTS articulos_disponibles;

CREATE VIEW articulos_disponibles AS
    SELECT  * FROM articulos_detalles 
        WHERE articulos_detalles.activo = TRUE AND articulos_detalles.stock > 0;

DROP VIEW IF EXISTS compras_clientes;

CREATE VIEW compras_clientes AS
    SELECT
        ventas.fecha as 'Fecha',
        clientes.id as 'ID del cliente',
        clientes.dni as 'DNI del cliente',
        clientes.nombre_completo as 'Cliente',
        empleados.id as 'ID del empleado',
        empleados.nombre_completo as 'Empleado',
        articulos_detalles.id as 'ID del artículo',
        articulos_detalles.`Categoría`,
        articulos_detalles.`Descripción`,
        ventas.precio as 'Precio de compra'
    FROM (
        ((articulos_detalles INNER JOIN ventas ON ventas.id_articulo = articulos_detalles.id)
            INNER JOIN empleados ON empleados.id = ventas.id_empleado)
        INNER JOIN clientes ON clientes.id = ventas.id_cliente
    ) ORDER BY ventas.fecha DESC;
