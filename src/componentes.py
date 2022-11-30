import eventos as evt
from tkinter import Menu, Label, Entry, Checkbutton, LabelFrame, Frame, Listbox, Button

def menuArchivo(root, barra):
    file = Menu(barra)
    file.add_command(label="Salir", command=lambda:evt.salir(root))
    barra.add_cascade(label="Archivo", menu=file)


def menuCliente(root, barra):
    client = Menu(barra)
    client.add_command(label="Nuevo", command=lambda:evt.nuevoCliente(root))
    client.add_command(label="Editar", command=lambda:evt.editarCliente(root))
    client.add_command(label="Borrar", command=lambda:evt.borrarCliente(root))
    barra.add_cascade(label="Clientes", menu=client)


def menuProducto(root, barra):
    product = Menu(barra)
    product.add_command(label="Nuevo", command=lambda:evt.nuevoProducto(root))
    product.add_command(label="Editar", command=lambda:evt.editarProducto(root))
    product.add_command(label="Borrar", command=lambda:evt.borrarProducto(root))
    barra.add_cascade(label="Productos", menu=product)


def menuCategoria(root, barra):
    category = Menu(barra)
    category.add_command(label="Nueva", command=lambda:evt.nuevaCategoria(root))
    category.add_command(label="Editar", command=lambda:evt.editarCategoria(root))
    category.add_command(label="Borrar", command=lambda:evt.borrarCategoria(root))
    barra.add_cascade(label="Categorías", menu=category)


def menuBar(root):
    barra = Menu(root)
    menuArchivo(root, barra)
    menuCategoria(root, barra)
    menuProducto(root, barra)
    menuCliente(root, barra)
    root.config(menu=barra)


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

    campoUsuario.bind('<Return>', lambda key :evt.iniciarSesion(key, campoUsuario, campoClave, app.nextCampo))
    campoClave.bind('<Return>', lambda key :evt.iniciarSesion(key, campoUsuario, campoClave, app.nextCampo))


def moduloProducto(app):
    master = Frame()
    lf = LabelFrame(master, text="Productos:")

    frame = Frame(lf)

    Label(frame, text="Buscar:").pack(side='left', ipadx=6)

    buscar = Entry(frame, justify='left', bg='#ffffff', width=50)
    buscar.pack(side='left', padx=10)

    frame.pack()

    products = Listbox(lf, justify='left', bg='#ffffff')
    products.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    lf.pack(fill='both', expand=True, padx=6, pady=6)

    master.pack(fill='both', expand=True)

    app.nextCampo = buscar


def moduloCarrito(app):
    master = Frame()
    lf = LabelFrame(master, text="Carrito:")

    frame = Frame(lf)

    cart = Listbox(frame, bg="#ffffff")
    cart.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    frame.pack(fill='both', expand=True)

    lf.pack(side='left', fill='both', expand=True, padx=6, pady=6)

    master.pack(side='left', fill='both', expand=True)


def moduloOperaciones(app):
    master = Frame()
    Button(master, text="Comprar", bg='#f3e244').pack(fill='x', expand=True, pady=6)
    Button(master, text="Cancelar", bg='#f34444').pack(fill='x', expand=True, pady=6)
    Button(master, text="Vaciar\nCarrito", bg='#bfbfbf').pack(fill='x', expand=True, pady=6)

    master.pack(side='left', fill='y', padx=6, pady=6)
