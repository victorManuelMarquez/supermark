# supermark

## Sistema desarrollado en python para el curso "1000 programadores salteños"

El sistema escogido unánimemente fue el [supermark](docs/Proyecto_SG_Supermark-_Com_MyJ-Python-2022.docx__22__0.pdf).

![logo](docs/logo_supermark.avif "Logo para el proyecto")

## Checkpoint # 1

### Diagrama de clases:

![Diagrama de clases](docs/diagrama_de_clases_vmm.png "Diagrama de clases v2 de Víctor Manuel Márquez")

Nota: Persona>>Cliente denota que la clase Cliente extiende a la clase Persona, además las funciones y atributos se omiten visualmente en la clase hija.

## Checkpoint # 2

Sistema de Gestión de Base de Datos (DBMS) escogido para trabajar: [SQLite3](https://www.sqlite.org/index.html).

### Diagrama Entidad Relación:

![Diagrama Entidad Relación](docs/DER-supermark.png "Diagramas Entidad Relación de Víctor Manuel Márquez")

Diagrama realizado con [DBeaver](https://dbeaver.io/).

# Interfaz gráfica de usuario:

### Ventana Principal:

![Ventana Principal-v2](docs/main-gui-supermark-02.png)

### Barra de Menús:

![¡Nueva Apariencia!](docs/supermark-menubar-demo-screen-capture.gif "Demostración de las opciones disponibles por ahora.")

## Notas:

- Las tablas sin relaciones, son tablas temporales (Vistas) o que solo existen en una consulta.
- [Archivos de Respaldo](src/backup).
- [Script SQL (SQLite3)](src/supermark.sql) y [base de datos SQLite3](src/backup/supermark.db) (Estructura); [base de datos SQLite3 cargada](src/supermark-data.db) (Estructura y datos precargados).

## Integrantes:

- [Víctor Manuel Márquez](https://github.com/victorManuelMarquez)
- [Lucas Martin Aramayo Tapia](https://github.com/LTapia2501)
- [Moya Montero Matias Exequiel](https://github.com/Mmoya123)
- [Luz Milagros Gomez Rivera](https://github.com/luzzgomez) 
