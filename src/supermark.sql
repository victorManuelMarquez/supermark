-- Autor: Víctor Manuel Márquez

-- Tablas

CREATE TABLE IF NOT EXISTS personas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT(10) NOT NULL,
    nombre_completo TEXT(140) NOT NULL,
    cliente INTEGER(1) NOT NULL DEFAULT 1, -- cliente como valor por defecto
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
    precio REAL NOT NULL,
    stock INTEGER(4) NOT NULL,
	activo INTEGER NOT NULL DEFAULT 1,
	CONSTRAINT FK_PROD_CAT FOREIGN KEY (id_categoria) 
        REFERENCES categorias(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS tickets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_consumidor INTEGER NOT NULL, -- id del cliente
    id_facilitador INTEGER NOT NULL, -- puede ser el mismo cliente (COMPRA ONLINE) [El fin es evitar usar NULL]
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    habilitado int(1) NOT NULL DEFAULT 1,
    CONSTRAINT FK_TICKET_CLIENTE FOREIGN KEY (id_consumidor)
        REFERENCES personas(id) ON UPDATE CASCADE,
    CONSTRAINT FK_TICKET_SUMINIS FOREIGN KEY (id_facilitador)
        REFERENCES personas(id) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ventas(
    id INTEGER PRIMARY KEY NOT NULL,
    id_ticket INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    monto REAL NOT NULL,
    CONSTRAINT FK_TICKET_ARTS FOREIGN KEY (id_ticket)
        REFERENCES tickets(id),
    CONSTRAINT FK_COMPRA_PROD FOREIGN KEY (id_producto)
        REFERENCES productos(id) ON UPDATE CASCADE
);

-- Índices

CREATE UNIQUE INDEX IF NOT EXISTS PK_TICKET ON tickets(id, id_consumidor, id_facilitador);

CREATE UNIQUE INDEX IF NOT EXISTS INDX_DNI ON personas(dni);

CREATE INDEX IF NOT EXISTS FECHA_DE_COMPRA ON tickets(fecha);

-- vistas

DROP VIEW IF EXISTS productos_detalles;

CREATE VIEW productos_detalles AS
    SELECT
        productos.id as 'ID',
        (categorias.nombre || " " || productos.descripcion) AS 'Detalles', -- En Mysql la sintáxis es diferente!!!
        productos.precio as 'Precio unitario',
        productos.stock as 'Stock',
        productos.activo as 'Activo'
    FROM (productos INNER JOIN categorias ON categorias.id = productos.id_categoria);

DROP VIEW IF EXISTS productos_disponibles;

CREATE VIEW productos_disponibles AS
    SELECT
        productos_detalles.id,
        productos_detalles.detalles,
        productos_detalles.`Precio unitario`
    FROM productos_detalles 
        WHERE productos_detalles.activo = TRUE AND productos_detalles.stock > 0;

DROP VIEW IF EXISTS ventas_detalles;

CREATE VIEW ventas_detalles AS
    SELECT
        tickets.id AS 'Ticket',
        -- consultas anidadas para cliente y vendedor o él mismo cliente
        (SELECT personas.nombre_completo FROM personas WHERE tickets.id_consumidor = personas.id) AS 'Cliente',
        (SELECT IIF(tickets.id_consumidor = tickets.id_facilitador, "-" , personas.nombre_completo) 
            FROM personas WHERE tickets.id_facilitador = personas.id
        ) AS 'Vendedor',
        tickets.fecha AS 'Fecha de compra',
        productos_detalles.detalles as 'Producto',
        ventas.cantidad AS 'Cantidad',
        ventas.monto AS 'Precio Final',
        tickets.habilitado AS 'Válido'
    FROM (
        (productos_detalles INNER JOIN ventas ON ventas.id_producto = productos_detalles.id) 
            INNER JOIN tickets ON tickets.id = ventas.id_ticket
    ) ORDER BY tickets.fecha DESC;

-- Notas: SQLite no posee procedimientos alamcenados.

-- SELECT last_insert_rowid(); -- usarlo despues de un insert
