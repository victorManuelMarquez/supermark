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


def iniciarSesion(key, campoUsuario, campoClave):
    nombre = campoUsuario.get()
    clave = campoClave.get()
    try:
        conexion = bd.Conexion()
        res = conexion.ejecutar('SELECT * FROM usuarios WHERE usuario = ? AND clave = ?', [(nombre, clave)])
        if res > 0:
            campoUsuario.delete(0, 'end')
            campoClave.delete(0, 'end')
        else:
            mb.showerror(title="No encontrado", message=f"El usuario `{nombre}` no existe.")
    except bd.Conexionerror:
        mb.showerror(title="Error al conectar", message="Falló la conexión con la base de datos.")
    finally:
        if conexion:
            conexion.cerrar()


def salir(root):
    root.destroy()
