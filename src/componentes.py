import eventos as evt
from tkinter import Menu, Label, Entry, Checkbutton, LabelFrame, Frame, Button
from tkinter.ttk import Treeview

def menuArchivo(app, barra):
    file = Menu(barra)
    file.add_command(label="Salir", command=lambda:evt.salir(app.root))
    barra.add_cascade(label="Archivo", menu=file)


def menuCliente(app, barra):
    client = Menu(barra)
    client.add_command(label="Nuevo", command=lambda:evt.nuevoCliente(app.root, app.sesion))
    client.add_command(label="Editar", command=lambda:evt.editarCliente(app.root, app.sesion))
    client.add_command(label="Borrar", command=lambda:evt.borrarCliente(app.root, app.sesion))
    barra.add_cascade(label="Clientes", menu=client)


def menuProducto(app, barra):
    product = Menu(barra)
    product.add_command(label="Nuevo", command=lambda:evt.nuevoProducto(app.root, products, app.sesion))
    product.add_command(label="Editar", command=lambda:evt.editarProducto(app.root, app.sesion))
    product.add_command(label="Borrar", command=lambda:evt.borrarProducto(app.root, app.sesion))
    barra.add_cascade(label="Productos", menu=product)


def menuCategoria(app, barra):
    category = Menu(barra)
    category.add_command(label="Nueva", command=lambda:evt.nuevaCategoria(app.root, app.sesion))
    category.add_command(label="Editar", command=lambda:evt.editarCategoria(app.root, app.sesion))
    category.add_command(label="Borrar", command=lambda:evt.borrarCategoria(app.root, app.sesion))
    barra.add_cascade(label="Categorías", menu=category)


def menuBar(app):
    barra = Menu(app.root)
    menuArchivo(app, barra)
    menuCategoria(app, barra)
    menuProducto(app, barra)
    menuCliente(app, barra)
    app.root.config(menu=barra)


def moduloUsuario(app):
    master = Frame()
    lblPackProps = {'side':'left','ipadx':10, 'ipady':10, 'fill':'x'}
    Label(master, text="Usuario:").pack(**lblPackProps)

    entryProp = {'justify':'right', 'bg':'#ffffff'}
    entryPackProp = {'side':'left', 'fill':'x', 'expand':True}

    campoUsuario = Entry(master, **entryProp)
    campoUsuario.pack(**entryPackProp)

    Label(master, text="Contraseña:").pack(**lblPackProps)

    campoClave = Entry(master, show='*', **entryProp)
    campoClave.pack(**entryPackProp)

    check = Checkbutton(master, text='¿Eres cliente?', variable=app.cliente, onvalue=True, offvalue=False)
    check.pack(side='left')

    master.pack()

    campoUsuario.bind('<Return>', lambda key :evt.iniciarSesion(key, app, campoUsuario, campoClave))
    campoClave.bind('<Return>', lambda key :evt.iniciarSesion(key, app, campoUsuario, campoClave))


def moduloProducto(app):
    master = Frame()
    lf = LabelFrame(master, text="Productos:")

    frame = Frame(lf)

    Label(frame, text="Buscar:").pack(side='left', ipadx=6)

    buscar = Entry(frame, justify='left', bg='#ffffff', width=50)
    buscar.pack(side='left', padx=10)

    frame.pack()

    global products
    products = Treeview(lf, show='headings', selectmode='extended')
    products.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    lf.pack(fill='both', expand=True, padx=6, pady=6)

    master.pack(fill='both', expand=True)

    app.nextCampo = buscar

    app.root.after(100, lambda:evt.cargarProductos(None, products))

    buscar.bind('<Return>', lambda key :evt.cargarProductos(key, products))
    products.bind('<Return>', lambda key:evt.agregarAlCarrito(key, products, cart))
    products.bind('<Double-Button>', lambda btn:evt.agregarAlCarrito(btn, products, cart))


def moduloCarrito(app):
    master = Frame()
    lf = LabelFrame(master, text="Carrito:")

    frame = Frame(lf)

    global cart
    cart = Treeview(frame, show='headings')
    cart.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    frame.pack(fill='both', expand=True)

    lf.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    master.pack(side='left', fill='both', expand=True)


def moduloOperaciones(app):
    master = Frame()
    Button(master, text="Comprar", bg='#f3e244', command=lambda:evt.comprar(cart)).pack(fill='x', expand=True, pady=6)
    Button(master, text="Cerrar\nSesión", bg='#f34444').pack(fill='x', expand=True, pady=6)
    Button(master, text="Vaciar\nCarrito", bg='#bfbfbf', command=lambda:evt.limpiar(cart)).pack(fill='x', expand=True, pady=6)

    master.pack(side='left', fill='y', padx=6, pady=6)
