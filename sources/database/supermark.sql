
-- Tablas

CREATE TABLE IF NOT EXISTS persona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT(20) NOT NULL,
    nombre TEXT(60) NOT NULL,
    apellido TEXT(60) NOT NULL,
    domicilio TEXT(140) NOT NULL,
    telefono TEXT(60) NOT NULL,
    correo TEXT(120) NOT NULL,
    activo INTEGER(1) NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS usuario (
    id_persona INTEGER PRIMARY KEY,
    nombre TEXT(30) NOT NULL,
    clave TEXT(8) NOT NULL,
    activo INTEGER(1) NOT NULL DEFAULT 1,
    CONSTRAINT FK_PERSONA_USUARIO 
        FOREIGN KEY (id_persona)
        REFERENCES persona(id)
);

CREATE TABLE IF NOT EXISTS grupo (
    id_usuario INTEGER PRIMARY KEY,
    nombre TEXT(40) NOT NULL DEFAULT "Cliente",
    activo INTEGER(1) NOT NULL DEFAULT 1,
    CONSTRAINT FK_USUARIO_GRUPO
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_persona)
);

-- Índices

CREATE UNIQUE INDEX IF NOT EXISTS DNI_PERSONA on persona(dni);

-- Vistas

DROP VIEW IF EXISTS usuarios;

CREATE VIEW usuarios AS
    SELECT
        persona.id AS `ID`,
        (persona.nombre || " " || persona.apellido) AS `Nombre Completo`,
        usuario.nombre AS `Nombre de Usuario`,
        usuario.clave AS `Clave Personal`,
        grupo.nombre AS `Grupo`,
        usuario.activo AS `Activo`
    FROM (
        persona INNER JOIN usuario 
            ON usuario.id_persona = persona.id
        ) INNER JOIN grupo 
        ON grupo.id_usuario = usuario.id_persona;
