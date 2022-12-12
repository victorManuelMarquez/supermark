from tkinter import Toplevel, Label, Entry, Button, Scale, BooleanVar, Checkbutton, messagebox as mb, Frame
from tkinter.ttk import Combobox
import evento as evt
import consulta
from tabla import Tabla


class Dialogo(Toplevel):
    def __init__(self, root, titulo="Dialogo", ancho=320, alto=240):
        super().__init__(root)
        self.title(titulo)
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry('%dx%d+%d+%d' % (ancho, alto, (sw-ancho)/2, (sh-alto)/2))
        self.resizable(width=False, height=False)


class NuevoCliente(Dialogo):
    def __init__(self, root, titulo="Dialogo", ancho=320, alto=150):
        super().__init__(root, titulo, ancho, alto)
        entryProp = {'justify':'right', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="D.N.I:").grid(row=0, column=0, padx=6, pady=6)
        self.dni = Entry(self, name="dni", **entryProp)
        self.dni.grid(row=0, column=1, **cmpProp)

        Label(self, text="Nombre:").grid(row=1, column=0, padx=6, pady=6)
        self.nombre = Entry(self, name="nombre", **entryProp)
        self.nombre.grid(row=1, column=1, **cmpProp)

        Label(self, text="Apellido:").grid(row=2, column=0, padx=6, pady=6)
        self.apellido = Entry(self, name="apellido", **entryProp)
        self.apellido.grid(row=2, column=1, **cmpProp)

        Button(self, text="Registrar", command=lambda : self.registrar()).grid(row=3, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda : evt.salir(self)).grid(row=3, column=2, padx=6, pady=6)


    def registrar(self):
        datos = {
            'dni':self.dni.get(), 
            'nombre_completo':self.nombre.get() + " " + self.apellido.get(), 
            'usuario':self.nombre.get(),
            'clave':self.apellido.get()
        }
        if consulta.registrar_cliente(datos):
            evt.salir(self)


class EditarCliente(Dialogo):
    def __init__(self, root, titulo="Editar cliente", ancho=420, alto=246):
        super().__init__(root, titulo, ancho, alto)
        self.__personas = []

        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Buscar:").grid(row=0, column=0, padx=6, pady=6)
        self.buscar = Entry(self, **entryProp)
        self.buscar.grid(row=0, column=1, **cmpProp)

        self.nav = Scale(self, from_=0, to=0, command=lambda pos :self.ponerValores(int(pos)), orient='horizontal', length=400, state='disabled')
        self.nav.grid(row=1, column=0, padx=6, pady=6, columnspan=3)

        Label(self, text="D.N.I:").grid(row=2, column=0, padx=6, pady=6)
        self.dni = Entry(self, **entryProp)
        self.dni.grid(row=2, column=1, **cmpProp)

        Label(self, text="Nombre completo:").grid(row=3, column=0, padx=6, pady=6)
        self.nombre = Entry(self, **entryProp)
        self.nombre.grid(row=3, column=1, **cmpProp)

        self.var_cliente = BooleanVar(value=False)

        self.cliente = Checkbutton(self, text="Cliente", variable=self.var_cliente, onvalue=True, offvalue=False)
        self.cliente.grid(row=4, column=0)

        self.var_activo = BooleanVar(value=False)

        self.activo = Checkbutton(self, text="Habilitado", variable=self.var_activo, onvalue=True, offvalue=False)
        self.activo.grid(row=4, column=1)

        Button(self, text="Actualizar", command=lambda : self.aplicar()).grid(row=5, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda : evt.salir(self)).grid(row=5, column=2, padx=6, pady=6)

        # eventos

        # al estar 'visible'
        self.after(100, lambda : self.cargarPersonas())

        # al tipear
        self.buscar.bind('<KeyRelease>', lambda key : self.cargarPersonas())


    def cargarPersonas(self):
        self.__personas = consulta.todas_las_personas(self.buscar.get())
        if not self.__personas:
            self.dni.delete(0, 'end')
            self.nombre.delete(0, 'end')
            self.var_cliente.set(value=False)
            self.var_activo.set(value=False)
            self.nav.config(from_=0, to=0, tickinterval=0, state='disabled')
        else:
            self.nav.config(from_=1, to=len(self.__personas), tickinterval=len(self.__personas)-1, state='normal')


    def ponerValores(self, pos):
        try:
            self.__persona_actual = self.__personas[pos-1]
            # limpio los campos
            self.dni.delete(0, 'end')
            self.nombre.delete(0, 'end')
            # establezco los datos
            self.dni.insert(0, self.__persona_actual['dni'])
            self.nombre.insert(0, self.__persona_actual['nombre_completo'])
            self.var_cliente.set(value=bool(self.__persona_actual['cliente']))
            self.var_activo.set(value=bool(self.__persona_actual['activo']))
        except IndexError:
            self.__persona_actual = None


    def aplicar(self):
        if self.__persona_actual:
            # el id ya está almacenado
            self.__persona_actual['dni'] = self.dni.get()
            self.__persona_actual['nombre_completo'] = self.nombre.get()
            self.__persona_actual['cliente'] = self.var_cliente.get()
            self.__persona_actual['activo'] = self.var_activo.get()
            if consulta.actualizar_cliente(self.__persona_actual):
                evt.salir(self)
        else:
            mb.showerror(title="Error", message="No hay resultados.")


class BorrarCliente(Dialogo):
    def __init__(self, root, titulo="Borrar cliente", ancho=420, alto=246):
        super().__init__(root, titulo, ancho, alto)
        self.__personas = []

        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Buscar:").grid(row=0, column=0, padx=6, pady=6)
        self.buscar = Entry(self, **entryProp)
        self.buscar.grid(row=0, column=1, **cmpProp)

        self.nav = Scale(self, from_=0, to=0, command=lambda pos :self.ponerValores(int(pos)), orient='horizontal', length=400, state='disabled')
        self.nav.grid(row=1, column=0, padx=6, pady=6, columnspan=3)

        Label(self, text="D.N.I:").grid(row=2, column=0, padx=6, pady=6)
        self.dni = Entry(self, **entryProp)
        self.dni.grid(row=2, column=1, **cmpProp)

        Label(self, text="Nombre completo:").grid(row=3, column=0, padx=6, pady=6)
        self.nombre = Entry(self, **entryProp)
        self.nombre.grid(row=3, column=1, **cmpProp)

        self.var_cliente = BooleanVar(value=False)

        self.cliente = Checkbutton(self, text="Cliente", variable=self.var_cliente, onvalue=True, offvalue=False)
        self.cliente.grid(row=4, column=0)

        self.var_activo = BooleanVar(value=False)

        self.activo = Checkbutton(self, text="Habilitado", variable=self.var_activo, onvalue=True, offvalue=False)
        self.activo.grid(row=4, column=1)

        Button(self, text="Eliminar", command=lambda : self.aplicar()).grid(row=5, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda : evt.salir(self)).grid(row=5, column=2, padx=6, pady=6)

        # eventos

        # al estar 'visible'
        self.after(100, lambda : self.cargarPersonas())

        # al tipear
        self.buscar.bind('<KeyRelease>', lambda key : self.cargarPersonas())


    def cargarPersonas(self):
        self.__personas = consulta.todas_las_personas(self.buscar.get())
        if not self.__personas:
            self.dni.delete(0, 'end')
            self.nombre.delete(0, 'end')
            self.var_cliente.set(value=False)
            self.var_activo.set(value=False)
            self.nav.config(from_=0, to=0, tickinterval=0, state='disabled')
        else:
            self.nav.config(from_=1, to=len(self.__personas), tickinterval=len(self.__personas)-1, state='normal')


    def ponerValores(self, pos):
        try:
            self.__persona_actual = self.__personas[pos-1]
            # activo los campos
            self.dni.config(state='normal')
            self.nombre.config(state='normal')
            self.cliente.config(state='normal')
            self.activo.config(state='normal')
            # limpio los campos
            self.dni.delete(0, 'end')
            self.nombre.delete(0, 'end')
            # establezco los datos
            self.dni.insert(0, self.__persona_actual['dni'])
            self.nombre.insert(0, self.__persona_actual['nombre_completo'])
            self.var_cliente.set(value=bool(self.__persona_actual['cliente']))
            self.var_activo.set(value=bool(self.__persona_actual['activo']))
            # desactivo los campos
            self.dni.config(state='readonly')
            self.nombre.config(state='readonly')
            self.cliente.config(state='disabled')
            self.activo.config(state='disabled')
        except IndexError:
            self.__persona_actual = None


    def aplicar(self):
        if self.__persona_actual:
            # el id ya está almacenado
            self.__persona_actual['dni'] = self.dni.get()
            self.__persona_actual['nombre_completo'] = self.nombre.get()
            self.__persona_actual['cliente'] = self.var_cliente.get()
            self.__persona_actual['activo'] = self.var_activo.get()
            if consulta.borrar_cliente(self.__persona_actual):
                evt.salir(self)
        else:
            mb.showerror(title="Error", message="No hay resultados.")


class NuevoProducto(Dialogo):
    def __init__(self, root, tabla, titulo="Nuevo producto", ancho=360, alto=186):
        super().__init__(root, titulo, ancho, alto)
        self.__tabla = tabla

        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Categoría:").grid(row=0, column=0, padx=6, pady=6)
        self.__categorias = Combobox(self, width=25)
        self.__categorias.grid(row=0, column=1, **cmpProp)

        Label(self, text="Descripción:").grid(row=1, column=0, padx=6, pady=6)
        self.__descr = Entry(self, **entryProp)
        self.__descr.grid(row=1, column=1, **cmpProp)

        Label(self, text="Precio:").grid(row=2, column=0, padx=6, pady=6)
        self.__precio = Entry(self, **entryProp)
        self.__precio.grid(row=2, column=1, **cmpProp)

        Label(self, text="Stock:").grid(row=3, column=0, padx=6, pady=6)
        self.__stock = Entry(self, **entryProp)
        self.__stock.grid(row=3, column=1, **cmpProp)

        Button(self, text="Registrar", command=lambda : self.registrar()).grid(row=4, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda : evt.salir(self)).grid(row=4, column=2, padx=6, pady=6)

        # eventos

        # al hacerse 'visible'
        self.after(100, self.cargarCategorias())


    def cargarCategorias(self):
        self.__categorias['values'] = consulta.todas_las_categorias()


    def registrar(self):
        datos = {
            'id_categoria':None,
            'descripcion':self.__descr.get(),
            'precio':self.__precio.get(),
            'stock':self.__stock.get()
        }
        id = consulta.id_categoria(self.__categorias.get())
        if id:
            print("ID CAT ->",id)
            datos['id_categoria'] = id
            print(datos)
            if consulta.registrar_producto(datos):
                evt.salir(self)
                evt.cargarProductos(self.__tabla, '')
        else:
            mb.showerror(title="Error", message="No hay resultados.")


class EditarProducto(Dialogo):
    def __init__(self, root, tabla, titulo="Editar producto", ancho=420, alto=294):
        super().__init__(root, titulo, ancho, alto)
        self.__tabla = tabla
        self.__productos = []

        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Categoría:").grid(row=0, column=0, padx=6, pady=6)
        self.__categorias = Combobox(self, width=25)
        self.__categorias.grid(row=0, column=1, **cmpProp)

        Label(self, text="Descripción:").grid(row=1, column=0, padx=6, pady=6)
        self.__descr = Entry(self, **entryProp)
        self.__descr.grid(row=1, column=1, **cmpProp)

        Label(self, text="Precio:").grid(row=2, column=0, padx=6, pady=6)
        self.__precio = Entry(self, **entryProp)
        self.__precio.grid(row=2, column=1, **cmpProp)

        Label(self, text="Stock:").grid(row=3, column=0, padx=6, pady=6)
        self.__stock = Entry(self, **entryProp)
        self.__stock.grid(row=3, column=1, **cmpProp)

        self.__var_activo = BooleanVar(value=False)

        self.activo = Checkbutton(self, text="Habilitado", variable=self.__var_activo, onvalue=True, offvalue=False)
        self.activo.grid(row=4, column=1, padx=6, pady=6)

        self.nav = Scale(self, from_=0, to=0, command=lambda pos : self.ponerValores(int(pos)),orient='horizontal', length=400)
        self.nav.grid(row=5, column=0, padx=6, pady=6, columnspan=3)

        Button(self, text="Actualizar", command=lambda : self.aplicar()).grid(row=6, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda : evt.salir(self)).grid(row=6, column=2, padx=6, pady=6)

        # eventos

        # al hacerse 'visible'
        self.after(100, self.cargarProductos())


    def cargarProductos(self):
        self.__categorias['values'] = consulta.todas_las_categorias()
        self.__productos = consulta.todos_los_productos()
        if not self.__productos:
            self.__descr.delete(0, 'end')
            self.__precio.delete(0, 'end')
            self.__stock.delete(0, 'end')
            self.__var_activo.set(value=False)
        else:
            self.nav.config(from_=1, to=len(self.__productos), tickinterval=len(self.__productos)-1)


    def ponerValores(self, pos):
        try:
            self.__producto_actual = self.__productos[pos-1]
            # limpio los campos
            self.__descr.delete(0, 'end')
            self.__precio.delete(0, 'end')
            self.__stock.delete(0, 'end')
            # cargo los datos
            self.__categorias.set(consulta.nombre_categoria(self.__producto_actual['id_categoria']))
            self.__descr.insert(0, self.__producto_actual['descripcion'])
            self.__precio.insert(0, self.__producto_actual['precio'])
            self.__stock.insert(0, self.__producto_actual['stock'])
            self.__var_activo.set(value=bool(self.__producto_actual['activo']))
        except IndexError:
            self.__producto_actual = None


    def aplicar(self):
        if self.__producto_actual:
            self.__producto_actual['id_categoria'] = consulta.id_categoria(self.__categorias.get())
            self.__producto_actual['descripcion'] = self.__descr.get()
            self.__producto_actual['precio'] = self.__precio.get()
            self.__producto_actual['stock'] = self.__stock.get()
            self.__producto_actual['activo'] = self.__var_activo.get()
            if consulta.actualizar_producto(self.__producto_actual):
                evt.salir(self)
                evt.cargarProductos(self.__tabla, '')
        else:
            mb.showerror(title="Error", message="No hay resultados.")


class BorrarProducto(Dialogo):
    def __init__(self, root, tabla, titulo="Borrar producto", ancho=420, alto=294):
        super().__init__(root, titulo, ancho, alto)
        self.__tabla = tabla
        self.__productos = []

        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Categoría:").grid(row=0, column=0, padx=6, pady=6)
        self.__categoria = Entry(self, **entryProp)
        self.__categoria.grid(row=0, column=1, **cmpProp)

        Label(self, text="Descripción:").grid(row=1, column=0, padx=6, pady=6)
        self.__descr = Entry(self, **entryProp)
        self.__descr.grid(row=1, column=1, **cmpProp)

        Label(self, text="Precio:").grid(row=2, column=0, padx=6, pady=6)
        self.__precio = Entry(self, **entryProp)
        self.__precio.grid(row=2, column=1, **cmpProp)

        Label(self, text="Stock:").grid(row=3, column=0, padx=6, pady=6)
        self.__stock = Entry(self, **entryProp)
        self.__stock.grid(row=3, column=1, **cmpProp)

        self.__var_activo = BooleanVar(value=False)

        self.activo = Checkbutton(self, text="Habilitado", variable=self.__var_activo, onvalue=True, offvalue=False)
        self.activo.grid(row=4, column=1, padx=6, pady=6)

        self.nav = Scale(self, from_=0, to=0, command=lambda pos : self.ponerValores(int(pos)),orient='horizontal', length=400)
        self.nav.grid(row=5, column=0, padx=6, pady=6, columnspan=3)

        Button(self, text="Actualizar", command=lambda : self.aplicar()).grid(row=6, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda : evt.salir(self)).grid(row=6, column=2, padx=6, pady=6)

        # eventos

        # al hacerse 'visible'
        self.after(100, self.cargarProductos())


    def cargarProductos(self):
        self.__productos = consulta.todos_los_productos()
        if not self.__productos:
            self.__categoria.delete(0, 'end')
            self.__descr.delete(0, 'end')
            self.__precio.delete(0, 'end')
            self.__stock.delete(0, 'end')
            self.__var_activo.set(value=False)
        else:
            self.nav.config(from_=1, to=len(self.__productos), tickinterval=len(self.__productos)-1)


    def ponerValores(self, pos):
        try:
            self.__producto_actual = self.__productos[pos-1]
            # habilito los campos
            self.__categoria.config(state='normal')
            self.__descr.config(state='normal')
            self.__precio.config(state='normal')
            self.__stock.config(state='normal')
            self.activo.config(state='normal')
            # limpio los campos
            self.__descr.delete(0, 'end')
            self.__precio.delete(0, 'end')
            self.__stock.delete(0, 'end')
            # cargo los datos
            self.__categoria.insert(0, consulta.nombre_categoria(self.__producto_actual['id_categoria']))
            self.__descr.insert(0, self.__producto_actual['descripcion'])
            self.__precio.insert(0, self.__producto_actual['precio'])
            self.__stock.insert(0, self.__producto_actual['stock'])
            self.__var_activo.set(value=bool(self.__producto_actual['activo']))
            # deshabilito los campos
            self.__categoria.config(state='readonly')
            self.__descr.config(state='readonly')
            self.__precio.config(state='readonly')
            self.__stock.config(state='readonly')
            self.activo.config(state='disabled')
        except IndexError:
            self.__producto_actual = None


    def aplicar(self):
        if self.__producto_actual:
            if consulta.borrar_producto(self.__producto_actual):
                evt.salir(self)
                evt.cargarProductos(self.__tabla, '')
        else:
            mb.showerror(title="Error", message="No hay resultados.")


class NuevaCategoria(Dialogo):
    def __init__(self, root, titulo="Nueva categoría", ancho=320, alto=78):
        super().__init__(root, titulo, ancho, alto)
        Label(self, text="Nombre:").grid(row=0, column=0, padx=6, pady=6)
        self.__nombre = Entry(self, justify='right', bg='#ffffff')
        self.__nombre.grid(row=0, column=1, columnspan=2, padx=6, pady=6)

        Button(self, text="Actualizar", command=lambda:self.registrar()).grid(row=1, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=1, column=2, padx=6, pady=6)


    def registrar(self):
        if consulta.registrar_categoria(self.__nombre.get()):
            evt.salir(self)


class EditarCategoria(Dialogo):
    def __init__(self, root, tabla, titulo="Editar categoría", ancho=320, alto=156):
        super().__init__(root, titulo, ancho, alto)
        self.__tabla_productos = tabla
        self.__categorias = []
        self.__categoria_actual = None

        Label(self, text="Nombre:").grid(row=0, column=0, padx=6, pady=6)
        self.__nombre = Entry(self, justify='right', bg='#ffffff')
        self.__nombre.grid(row=0, column=1, columnspan=2, padx=6, pady=6)

        self.nav = Scale(self, command=lambda pos : self.ponerValor(int(pos)), orient='horizontal', length=300)
        self.nav.grid(row=1, column=0, padx=6, pady=6, columnspan=3)

        Button(self, text="Registrar", command=lambda:self.aplicar()).grid(row=2, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=2, column=2, padx=6, pady=6)

        self.after(100, lambda : self.cargarCategorias())


    def cargarCategorias(self):
        self.__categorias = consulta.todas_las_categorias()
        if not self.__categorias:
            self.__nombre.delete(0, 'end')
        else:
            self.nav.config(from_=1, to=len(self.__categorias), tickinterval=len(self.__categorias)-1)


    def ponerValor(self, pos):
        try:
            self.__categoria_actual = self.__categorias[pos-1]
            self.__nombre.delete(0, 'end')
            self.__nombre.insert(0, self.__categoria_actual)
        except IndexError:
            self.__categoria_actual = None


    def aplicar(self):
        if consulta.actualizar_categoria(self.__categoria_actual, self.__nombre.get()):
            evt.salir(self)
            evt.cargarProductos(self.__tabla_productos, '')


class Compras(Dialogo):
    def __init__(self, root, cliente, titulo="Compras", ancho=720, alto=372):
        super().__init__(root, titulo, ancho, alto)
        self.resizable(width=True, height=True)
        self.__cliente = cliente

        frame = Frame(self)

        self.__tabla_compras = Tabla(frame)
        self.__tabla_compras.cuerpo.config(height=15)
        self.__tabla_compras.cuerpo.pack(side='left', fill='both', expand=True)

        frame.pack(fill='both', expand=True, padx=6, pady=6)

        Button(self, text="Cerrar", command=lambda : evt.salir(self)).pack(side='bottom')

        self.after(100, lambda : self.cargarCompras())


    def cargarCompras(self):
        resultados = consulta.compras_cliente(self.__cliente)
        self.__tabla_compras.columnas = resultados['cols']
        self.__tabla_compras.filas = resultados['rows']


class Ventas(Dialogo):
    def __init__(self, root, titulo="Ventas", ancho=642, alto=372):
        super().__init__(root, titulo, ancho, alto)

        frame = Frame(self)

        self.__tabla_ventas = Tabla(self)
        self.__tabla_ventas.cuerpo.config(height=15)
        self.__tabla_ventas.cuerpo.pack(side='left', fill='both', expand=True)

        frame.pack(fill='both', expand=True, padx=6, pady=6)

        Button(self, text="Cerrar", command=lambda : evt.salir(self)).pack(padx=6, pady=6)

        self.after(100, lambda : self.cargarVentas())


    def cargarVentas(self):
        resultados = consulta.todas_las_ventas_de()
        self.__tabla_ventas.columnas = resultados['cols']
        self.__tabla_ventas.filas = resultados['rows']
