import consulta
from tkinter import messagebox as mb
import dialog


def iniciarSesion(app, campoUsuario, campoClave, campoBuscar):
    if consulta.validar_sesion(app, campoUsuario.get(), campoClave.get()):
        campoUsuario.delete(0, 'end')
        campoClave.delete(0, 'end')
        campoBuscar.focus_set()
        mb.showinfo(title="Bienvenido/a", message=f"¡Bienvenid@ `{app.cliente['nombre_completo']}`!")
    else:
        mb.showerror(title="Falló", message=f"Usuario o clave incorrecta.")


def cargarProductos(tabla, valorBuscado):
    tabla.vaciar()
    resultados = consulta.filtrar_productos(valorBuscado)
    tabla.columnas = resultados['cols']
    tabla.filas = resultados['rows']


def agregarAlCarrito(productos, carrito, total):
    if len(carrito.filas) + len(productos.cuerpo.selection()) > 30:
        mb.showerror(title="Error", message="No puedes comprar más de 30 productos.")
    else:
        carrito.columnas = productos.columnas
        for iid in productos.cuerpo.selection():
            carrito.filas.append(productos.cuerpo.item(iid).get('values'))
        carrito.refrescar()
        monto = float(total.get())
        for fila in carrito.listaDiccionario():
            monto += float(fila['Precio unitario'])
        total.config(state='normal')
        total.delete(0, 'end')
        total.insert(0, str(monto))
        total.config(state='readonly')


def realizarCompra(app, carrito):
    if len(carrito.filas) and app.cliente:
        if consulta.finalizar_compra(app, carrito.listaDiccionario()):
            carrito.vaciar()
    elif len(carrito.filas) == 0:
        mb.showerror(title="Operación inválida", message="Carrito vacío.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def vaciarCarrito(carrito):
    if len(carrito.filas):
        if mb.askokcancel(title="Atención", message="¿Desea vaciar el carrito de compras?"):
            carrito.vaciar()
    else:
        mb.showerror(title="Operación inválida", message="Carrito vacío.")


def nuevoCliente(app):
    if app.cliente and not app.cliente['cliente']:
        dialog.NuevoCliente(app.root)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def editarCliente(app):
    if app.cliente and not app.cliente['cliente']:
        dialog.EditarCliente(app.root)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def borrarCliente(app):
    if app.cliente and not app.cliente['cliente']:
        dialog.BorrarCliente(app.root)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def nuevoProducto(app, tabla):
    if app.cliente and not app.cliente['cliente']:
        dialog.NuevoProducto(app.root, tabla)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def editarProducto(app, tabla):
    if app.cliente and not app.cliente['cliente']:
        dialog.EditarProducto(app.root, tabla)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def borrarProducto(app, tabla):
    if app.cliente and not app.cliente['cliente']:
        dialog.BorrarProducto(app.root, tabla)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def nuevaCategoria(app):
    if app.cliente and not app.cliente['cliente']:
        dialog.NuevaCategoria(app.root)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def editarCategoria(app, tabla):
    if app.cliente and not app.cliente['cliente']:
        dialog.EditarCategoria(app.root, tabla)
    elif app.cliente:
        mb.showerror(title="Operación denegada", message="No puedes realizar está operación.")
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def verCompras(app):
    if app.cliente and app.cliente['cliente']:
        dialog.Compras(app.root, app.cliente)
    elif app.cliente:
        dialog.Ventas(app.root, app.cliente)
    else:
        mb.showerror(title="Operación inválida", message="No te has registrado.")


def salir(root):
    root.destroy()
