from tkinter import Menu, Label, Entry, LabelFrame, Frame, Button
import evento as evt
from tabla import Tabla


def menuArchivo(app, barra: Menu):
    menuFile = Menu(barra)
    menuFile.add_command(label="Salir", command=lambda: evt.salir(app.root))
    barra.add_cascade(label="Archivo", menu=menuFile)


def menuCliente(app, barra: Menu):
    menuClient = Menu(barra)
    menuClient.add_command(label="Nuevo", command=lambda : evt.nuevoCliente(app))
    menuClient.add_command(label="Editar", command=lambda : evt.editarCliente(app))
    menuClient.add_command(label="Borrar", command=lambda : evt.borrarCliente(app))
    barra.add_cascade(label="Clientes", menu=menuClient)


def menuProducto(app, barra: Menu):
    menuProduct = Menu(barra)
    menuProduct.add_command(label="Nuevo", command=lambda : evt.nuevoProducto(app, tabla_productos))
    menuProduct.add_command(label="Editar", command=lambda : evt.editarProducto(app, tabla_productos))
    menuProduct.add_command(label="Borrar", command=lambda : evt.borrarProducto(app, tabla_productos))
    barra.add_cascade(label="Productos", menu=menuProduct)


def menuCategoria(app, barra: Menu):
    menuCategory = Menu(barra)
    menuCategory.add_command(label="Nueva", command=lambda : evt.nuevaCategoria(app))
    menuCategory.add_command(label="Editar", command=lambda : evt.editarCategoria(app, tabla_productos))
    barra.add_cascade(label="Categorías", menu=menuCategory)


def menuActividad(app, barra: Menu):
    menuShop = Menu(barra)
    menuShop.add_command(label="Historial de compras", command=lambda : evt.verCompras(app))
    barra.add_cascade(label="Actividad", menu=menuShop)


def menuBar(app):
    barra = Menu(app.root)
    menuArchivo(app, barra)
    menuCategoria(app, barra)
    menuProducto(app, barra)
    menuCliente(app, barra)
    menuActividad(app, barra)
    app.root.config(menu=barra)


def moduloUsuario(app):
    master = Frame()

    lbl_props = {'side':'left', 'ipadx':6, 'ipady':6, 'fill':'x'}

    Label(master, text="Usuario:").pack(**lbl_props)

    entry_props = {'justify':'right', 'bg':'#ffffff'}
    entry_pack_props = {'side':'left', 'fill':'x', 'expand':True}

    fld_usuario = Entry(master, **entry_props)
    fld_usuario.pack(**entry_pack_props)

    Label(master, text="Contraseña:").pack(**lbl_props)

    fld_clave = Entry(master, show="*", **entry_props)
    fld_clave.pack(**entry_pack_props)

    master.pack()

    # eventos

    ## al presionar 'Enter'
    fld_usuario.bind('<Return>', lambda key : evt.iniciarSesion(app, fld_usuario, fld_clave, filtrar))
    fld_clave.bind('<Return>', lambda key : evt.iniciarSesion(app, fld_usuario, fld_clave, filtrar))


def moduloProducto(app):
    master = Frame()
    lf = LabelFrame(master, text="Productos:")

    frame = Frame(lf)

    Label(frame, text="Buscar:").pack(side='left', ipadx=6)

    global filtrar

    filtrar = Entry(frame, justify='left', bg='#ffffff', width=50)
    filtrar.pack(side='left', padx=10)

    frame.pack()

    global tabla_productos

    tabla_productos = Tabla(lf)
    tabla_productos.cuerpo.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    lf.pack(fill='both', expand=True, padx=6, pady=6)
    master.pack(fill='both', expand=True)

    # eventos

    ## al estar 'visible'
    app.root.after(100, lambda : evt.cargarProductos(tabla_productos, ''))

    ## tipeo
    filtrar.bind('<KeyRelease>', lambda key : evt.cargarProductos(tabla_productos, filtrar.get()))

    ## al presionar 'Enter'
    tabla_productos.cuerpo.bind('<Return>', lambda key : evt.agregarAlCarrito(tabla_productos, tabla_carrito, total, filtrar))

    ## doble clic con el ratón
    tabla_productos.cuerpo.bind('<Double-Button>', lambda mbtn : evt.agregarAlCarrito(tabla_productos, tabla_carrito, total, filtrar))


def moduloCarrito():
    master = Frame()
    lf = LabelFrame(master, text="Carrito:")

    frame = Frame(lf)

    global tabla_carrito

    tabla_carrito = Tabla(frame)
    tabla_carrito.cuerpo.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    frame.pack(fill='both', expand=True)

    lf.pack(side='top', fill='both', expand=True, padx=6, pady=6)

    frame = Frame(master)

    Label(master, text="TOTAL:").pack(side='left', padx=6, pady=6)

    global total

    total = Entry(master, justify='right')
    total.insert(0, '0.00')
    total.config(state='readonly')
    total.pack(side='left', padx=6, pady=6)

    frame.pack(side='bottom', fill='x', expand=True)

    master.pack(side='left', fill='both', expand=True)


def moduloOperaciones(app):
    master = Frame()

    btn_comprar = Button(master, text="Comprar", command=lambda: evt.realizarCompra(app, tabla_carrito, total, tabla_productos))
    btn_comprar.pack(fill='x', expand=True, pady=6)

    btn_vaciar = Button(master, text="Vaciar\ncarrito", command=lambda: evt.vaciarCarrito(tabla_carrito, total, filtrar))
    btn_vaciar.pack(fill='x', expand=True, pady=6)

    master.pack(side='left', fill='y', padx=6, pady=6)
