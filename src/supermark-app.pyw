import tkinter as tk
from tkinter import font
from tkinter import Menu
from tkinter import BooleanVar
from tktooltip import ToolTip
from tkinter import messagebox

# aplicación principal
class App:

    # constructor
    def __init__(self, root, titulo="SuperMark - Principal"):
        self.__root = root
        self.__fuente = font.Font(name='Verdana', size=12)
        self.__esCliente = BooleanVar(value=True)
        self.root.title(titulo)
        self.menuBar(self.root)
        self.preferredSize(720, 480)
        self.moduloUsuario(tk.Frame())
        self.moduloProductos(tk.Frame())
        self.moduloCarrito(tk.Frame())
        self.moduloOperaciones(tk.Frame())

    # getters
    @property
    def root(self):
        return self.__root

    @property
    def esCliente(self):
        return self.__esCliente

    @property
    def fuente(self):
        return self.__fuente

    # setters
    def preferredSize(self, w, h):
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (w, h, (sw - w) / 2, ((sh - h) - 100) / 2))
    
    # barra
    def menuBar(self, contenedor):
        menubar = Menu(contenedor)
        contenedor.config(menu=menubar)

        self.menuArchivo(menubar)
        self.menuCliente(menubar)
        self.menuCategoria(menubar)
        self.menuProducto(menubar)

    def menuArchivo(self, menubar):
        menu_archivo = Menu(menubar)
        menu_archivo.add_command(label="Salir", command=self.salir)

        menubar.add_cascade(label="Archivo", menu=menu_archivo)
    
    def menuCliente(self, menubar):
        submenu = Menu(menubar)
        submenu.add_command(label="Nuevo")
        submenu.add_command(label="Editar")
        submenu.add_command(label="Borrar")

        menubar.add_cascade(label="Clientes", menu=submenu)
    
    def menuProducto(self, menubar):
        submenu = Menu(menubar)
        submenu.add_command(label="Actualizar Stock")
        submenu.add_command(label="Nuevo")
        submenu.add_command(label="Editar")
        submenu.add_command(label="Borrar")

        menubar.add_cascade(label="Productos", menu=submenu)
    
    def menuCategoria(self, menubar):
        submenu = Menu(menubar)
        submenu.add_command(label="Nueva")
        submenu.add_command(label="Editar")
        submenu.add_command(label="Borrar")

        menubar.add_cascade(label="Categorías", menu=submenu)

    # modulos
    def moduloUsuario(self, contenedor):
        entryProp = {'justify':'right', 'bg':'#ffffff', 'font':self.fuente}
        packLabelProp = {'ipadx':10, 'ipady':10, 'fill':tk.X}

        tk.Label(contenedor, text="Usuario:", font=self.fuente).pack(side='left', **packLabelProp)

        campoUsuario = tk.Entry(contenedor, **entryProp)
        campoUsuario.pack(side='left', fill=tk.X, expand=True)
        ToolTip(campoUsuario, msg="Complete los campos y presione 'Enter' para iniciar la sesión.")

        tk.Label(contenedor, text="Contraseña:", font=self.fuente).pack(side='left', **packLabelProp)

        campoClave = tk.Entry(contenedor, show="*", width=12, **entryProp)
        campoClave.pack(side='left')
        ToolTip(campoClave, msg="Complete los campos y presione 'Enter' para iniciar la sesión.")

        chk = tk.Checkbutton(contenedor, text="¿Es cliente?", font=self.fuente, variable=self.esCliente, onvalue=True, offvalue=False)
        chk.pack(side='left')
        ToolTip(chk, msg="¿Va a logearse como cliente?")

        contenedor.pack()

    def moduloProductos(self, contenedor):
        propiedades = {'justify':'left', 'bg':'#ffffff', 'font':self.fuente, 'state':"disabled"}

        lf = tk.LabelFrame(contenedor, text="Productos:")

        frame = tk.Frame(lf)

        tk.Label(frame, text="Buscar:", font=self.fuente).pack(side='left', ipadx=6)

        campoBuscar = tk.Entry(frame, width=50, **propiedades)
        campoBuscar.pack(side='left', fill=tk.X, padx=10)

        frame.pack()

        ToolTip(campoBuscar, msg="Ingrese la marca o descripción del producto.")

        tk.Listbox(lf, **propiedades).pack(side='left', fill=tk.BOTH, expand=True, padx=10, pady=10)

        lf.pack(fill=tk.BOTH, expand=True, padx=6)

        contenedor.pack(fill=tk.BOTH, expand=True)

    def moduloCarrito(self, contenedor):
        lf = tk.LabelFrame(contenedor, text="Carrito:")

        frame = tk.Frame(lf)

        tk.Button(frame, text="Vaciar\ncarrito", state='disabled', borderwidth='1px', font=self.fuente, bg="#bfbfbf").pack(side='left', anchor=tk.N)

        tk.Listbox(frame, state='disabled', bg="#ffffff").pack(side='left', fill=tk.BOTH, expand=True, padx=6, pady=6)

        frame.pack(fill=tk.BOTH, expand=True)

        lf.pack(side='left', fill=tk.BOTH, expand=True, padx=6, pady=6)

        contenedor.pack(side='left', fill=tk.BOTH, expand=True)

    def moduloOperaciones(self, contenedor):
        tk.Button(contenedor, text="Comprar", state='disabled', borderwidth='1px', font=self.fuente, bg="#f3e244").pack(fill=tk.X, pady=10)

        tk.Button(contenedor, text="Cancelar", state='disabled', borderwidth='1px', font=self.fuente, bg="#f34444").pack(fill=tk.X, pady=10)

        contenedor.pack(side='left', fill=tk.Y, padx=6, pady=10)
    
    # eventos & acciones

    def salir(self):
        self.root.destroy()
        quit() # finaliza la consola

root = tk.Tk()
app = App(root)
root.mainloop()
