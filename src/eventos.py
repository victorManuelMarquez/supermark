import dialogo
import conexion as bd


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
    res = bd.ejecutar('SELECT COUNT(*) FROM usuarios WHERE nombre = ? AND clave = ?', (nombre, clave))
    if res > 0:
        campoUsuario.delete(0, 'end')
        campoClave.delete(0, 'end')


def salir(root):
    root.destroy()
