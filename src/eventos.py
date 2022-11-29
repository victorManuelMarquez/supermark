import dialogo


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

def salir(root):
    root.destroy()
