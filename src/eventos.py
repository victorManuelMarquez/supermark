import dialogo
import conexion as bd
from tkinter import messagebox as mb


def nuevoCliente(root):
    dialogo.Nuevocliente(root)


def editarCliente(root):
    dialogo.Editarcliente(root)


def borrarCliente(root):
    dialogo.Borrarcliente(root)


def nuevaCategoria(root):
    dialogo.Nuevacategoria(root)


def editarCategoria(root):
    dialogo.Editarcategoria(root)


def borrarCategoria(root):
    dialogo.Borrarcategoria(root)


def nuevoProducto(root):
    dialogo.Nuevoproducto(root)


def editarProducto(root):
    dialogo.Editarproducto(root)


def borrarProducto(root):
    dialogo.Borrarproducto(root)


def iniciarSesion(key, campoUsuario, campoClave, nextCampo):
    nombre = campoUsuario.get()
    clave = campoClave.get()
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT * FROM usuarios WHERE usuario = "{nombre}" AND clave = "{clave}"')
        if len(conexion.datos()) > 0:
            mb.showinfo(title="Bienvenido/a", message="¡Sesión iniciada!")
            campoUsuario.delete(0, 'end')
            campoClave.delete(0, 'end')
            nextCampo.focus_set()
        else:
            mb.showerror(title="No encontrado", message=f"El usuario `{nombre}` no existe.")
    except bd.Conexionerror:
        mb.showerror(title="Error al conectar", message="Falló la conexión con la base de datos.")
    finally:
        if conexion:
            conexion.cerrar()


def estableceColumnas(tabla, columnas):
    tabla.config(columns=columnas)
    for columna in columnas:
        tabla.heading(columna, text=columna)


def cargarProductos(key, tabla):
    try:
        # vacio los datos anteriores
        tabla.delete(*tabla.get_children())

        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT * FROM productos_disponibles')
        global columnas
        columnas = conexion.columnas()

        estableceColumnas(tabla, columnas)

        for fila in conexion.datos():
            tabla.insert("", "end", values=fila)
        
    except bd.Conexionerror:
        mb.showerror(title="Error al conectar", message="Falló la conexión con la base de datos.")
    finally:
        if conexion:
            conexion.cerrar()


def agregarAlCarrito(input, productos, carrito):
    seleccion = productos.selection()
    estableceColumnas(carrito, columnas)
    for fila in seleccion:
        carrito.insert("", "end", values=productos.item(fila).get('values'))


def validar(campo, min=2, max=30):
    cad = (campo.get()).strip()
    return len(cad) >= min and len(cad) <= max


def salir(root):
    root.destroy()
