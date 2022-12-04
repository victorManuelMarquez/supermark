import eventos as evt
import conexion as bd
from tkinter import Toplevel, Label, Entry, Button, Checkbutton, messagebox as mb, Scale, BooleanVar
from tkinter.ttk import Combobox


class Dialogo(Toplevel):
    def __init__(self, root, titulo="Dialogo", ancho=320, alto=240):
        super().__init__(root)
        self.title(titulo)
        self.dimension(ancho, alto)
        self.resizable(width=False, height=False)
    
    def dimension(self, w, h):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry("%dx%d+%d+%d" % (w, h, (sw-w)/2, (sh-h)/2))


class Nuevocliente(Dialogo):
    def __init__(self, root, titulo="Nuevo cliente", ancho=320, alto=150):
        super().__init__(root, titulo, ancho, alto)
        entryProp = {'justify':'right', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="D.N.I:").grid(row=0, column=0, padx=6, pady=6)
        dni = Entry(self, name="dni", **entryProp)
        dni.grid(row=0, column=1, **cmpProp)

        Label(self, text="Nombre:").grid(row=1, column=0, padx=6, pady=6)
        nombre = Entry(self, name="nombre", **entryProp)
        nombre.grid(row=1, column=1, **cmpProp)

        Label(self, text="Apellido:").grid(row=2, column=0, padx=6, pady=6)
        apellido = Entry(self, name="apellido", **entryProp)
        apellido.grid(row=2, column=1, **cmpProp)

        self.__campos = [dni, nombre, apellido]

        Button(self, text="Registrar", command=lambda:self.registrarCliente()).grid(row=3, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=3, column=2, padx=6, pady=6)
    

    def registrarCliente(self):
        datos = []
        invalidado = None
        for campo in self.__campos:
            if evt.validar(campo):
                datos.append(campo.get())
            else:
                invalidado = campo
                break
        if len(self.__campos) == len(datos):
            try:
                conexion = bd.Conexion()
                ins = conexion.ejecutar(f'''
                INSERT INTO personas(dni, nombre_completo, usuario, clave, cliente) 
                VALUES('{datos[0]}', '{datos[1]} {datos[2]}', '{datos[1]}', '{datos[2]}', '{int(True)}')''')
                if ins > 0:
                    mb.showinfo(title="Cliente/Usuario registrado", message="Nuevo cliente registrado: Ok!")
                    evt.salir(self)
            except bd.Conexionerror:
                mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
            finally:
                if conexion:
                    conexion.cerrar()
        else:
            mb.showerror(title="Campo inválido", message=f"El campo `{invalidado.winfo_name()}` no cumple los requisitos.")


class Editarcliente(Dialogo):
    def __init__(self, root, titulo="Editar cliente", ancho=420, alto=252):
        super().__init__(root, titulo, ancho, alto)
        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Buscar:").grid(row=0, column=0, padx=6, pady=6)
        self.buscar = Entry(self, **entryProp)
        self.buscar.grid(row=0, column=1, **cmpProp)

        self.nav = Scale(self, from_=0, to=0, command=lambda indice :self.ponerValores(int(indice)), orient='horizontal', length=400, state='disabled')
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

        Button(self, text="Actualizar", command=lambda:self.actualizarPersona()).grid(row=5, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=5, column=2, padx=6, pady=6)

        self.personas = []

        self.after(100, lambda:self.cargarPersonas())

        self.buscar.bind('<KeyRelease>', lambda key :self.cargarPersonas())


    def cargarPersonas(self):
        try:
            valor = self.buscar.get()
            conexion = bd.Conexion()
            conexion.ejecutar(f'''
            SELECT * FROM personas 
            WHERE dni LIKE "%{valor}%" OR nombre_completo LIKE "%{valor}%"''')
            claves = conexion.columnas()
            self.personas.clear()
            for valor in conexion.datos():
                self.personas.append(dict(zip(claves, valor)))
            self.nav.config(from_=1, to=len(self.personas), tickinterval=len(self.personas)-1, state='normal')
            if len(self.personas) > 0:
                self.ponerValores(0)
            else:
                self.dni.delete(0, 'end')
                self.nombre.delete(0, 'end')
                self.var_cliente.set(value=False)
                self.var_activo.set(value=False)
        except bd.Conexionerror:
            mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
        finally:
            if conexion:
                conexion.cerrar()


    def ponerValores(self, indice):
        persona = self.personas[indice-1]
        self.dni.delete(0, 'end')
        self.dni.insert(0, persona.get('dni'))
        self.nombre.delete(0, 'end')
        self.nombre.insert(0, persona.get('nombre_completo'))
        self.var_cliente.set(value=bool(persona.get('cliente')))
        self.var_activo.set(value=bool(persona.get('activo')))


    def actualizarPersona(self):
        if len(self.personas) > 0:
            try:
                conexion = bd.Conexion()
                updated = conexion.ejecutar(f'''
                UPDATE 
                    personas 
                SET
                    dni = "{self.dni.get()}",
                    nombre_completo = "{self.nombre.get()}",
                    cliente = {int(self.var_cliente.get())},
                    activo = {int(self.var_activo.get())}
                WHERE id = {self.personas[int(self.nav.get()) - 1].get('id')}''')
                if updated > 0:
                    mb.showinfo(title="Datos actualizados", message="Persona actualizada: Ok!")
                    evt.salir(self)
            except bd.Conexionerror:
                mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
            finally:
                if conexion:
                    conexion.cerrar()
        else:
            mb.showerror(title="Operación inválida", message="¡No se puede realizar esta operación!")


class Borrarcliente(Dialogo):
    def __init__(self, root, titulo="Borrar cliente", ancho=420, alto=252):
        super().__init__(root, titulo, ancho, alto)
        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Buscar:").grid(row=0, column=0, padx=6, pady=6)
        self.buscar = Entry(self, **entryProp)
        self.buscar.grid(row=0, column=1, **cmpProp)

        self.nav = Scale(self, from_=0, to=0, command=lambda indice :self.ponerValores(int(indice)), orient='horizontal', length=400, state='disabled')
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

        Button(self, text="Actualizar", command=lambda:self.borrarPersona()).grid(row=5, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=5, column=2, padx=6, pady=6)

        self.personas = []

        self.after(100, lambda:self.cargarPersonas())

        self.buscar.bind('<KeyRelease>', lambda key :self.cargarPersonas())


    def cargarPersonas(self):
        try:
            valor = self.buscar.get()
            conexion = bd.Conexion()
            conexion.ejecutar(f'''
            SELECT * FROM personas 
            WHERE activo = 1 AND (dni LIKE "%{valor}%" OR nombre_completo LIKE "%{valor}%")''')
            claves = conexion.columnas()
            self.personas.clear()
            for valor in conexion.datos():
                self.personas.append(dict(zip(claves, valor)))
            self.nav.config(from_=1, to=len(self.personas), tickinterval=len(self.personas)-1, state='normal')
            if len(self.personas) > 0:
                self.ponerValores(0)
            else:
                self.dni.delete(0, 'end')
                self.nombre.delete(0, 'end')
                self.var_cliente.set(value=False)
                self.var_activo.set(value=False)
        except bd.Conexionerror:
            mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
        finally:
            if conexion:
                conexion.cerrar()


    def ponerValores(self, indice):
        persona = self.personas[indice-1]
        self.dni.delete(0, 'end')
        self.dni.insert(0, persona.get('dni'))
        self.nombre.delete(0, 'end')
        self.nombre.insert(0, persona.get('nombre_completo'))
        self.var_cliente.set(value=bool(persona.get('cliente')))
        self.var_activo.set(value=bool(persona.get('activo')))


    def borrarPersona(self):
        if len(self.personas) > 0:
            try:
                conexion = bd.Conexion()
                deleted = conexion.ejecutar(f'''UPDATE personas SET activo = 0 WHERE id = "{self.personas[int(self.nav.get()) - 1].get('id')}"''')
                if deleted > 0:
                    mb.showinfo(title="Operación completada", message="Persona desafectada: Ok!")
                    evt.salir(self)
            except bd.Conexionerror:
                mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
            finally:
                if conexion:
                    conexion.cerrar()
        else:
            mb.showerror(title="Operación inválida", message="¡No se puede realizar esta operación!")


class Nuevacategoria(Dialogo):
    def __init__(self, root, titulo="Nueva categoría", ancho=320, alto=72):
        super().__init__(root, titulo, ancho, alto)
        Label(self, text="Nombre:").grid(row=0, column=0, padx=6, pady=6)
        self.nombre = Entry(self, justify='right', bg='#ffffff')
        self.nombre.grid(row=0, column=1, columnspan=2, padx=6, pady=6)

        Button(self, text="Registrar", command=lambda:self.registrarCategoria()).grid(row=1, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=1, column=2, padx=6, pady=6)


    def registrarCategoria(self):
        if evt.validar(self.nombre):
            try:
                conexion = bd.Conexion()
                ins = conexion.ejecutar(f'INSERT INTO categorias(nombre) VALUES("{self.nombre.get()}")')
                if ins > 0:
                    mb.showinfo(title="Categoría registrada", message="Nueva categoría: Ok!")
                    evt.salir(self)
            except bd.Conexionerror:
                mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
            finally:
                if conexion:
                    conexion.cerrar()
        else:
            mb.showerror(title="Campo inválido", message=f"El nombre no cumple los requisitos.")


class Editarcategoria(Dialogo):
    def __init__(self, root, titulo="Editar categoría", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)


class Borrarcategoria(Dialogo):
    def __init__(self, root, titulo="Borrar categoría", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)


class Nuevoproducto(Dialogo):
    def __init__(self, root, products, titulo="Nuevo producto", ancho=360, alto=186):
        super().__init__(root, titulo, ancho, alto)
        self.productos = products
        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Categoría:").grid(row=0, column=0, padx=6, pady=6)
        self.categorias = Combobox(self, width=25)
        self.categorias.grid(row=0, column=1, **cmpProp)

        Label(self, text="Descripción:").grid(row=1, column=0, padx=6, pady=6)
        self.descr = Entry(self, **entryProp)
        self.descr.grid(row=1, column=1, **cmpProp)

        Label(self, text="Precio:").grid(row=2, column=0, padx=6, pady=6)
        self.precio = Entry(self, **entryProp)
        self.precio.grid(row=2, column=1, **cmpProp)

        Label(self, text="Stock:").grid(row=3, column=0, padx=6, pady=6)
        self.stock = Entry(self, **entryProp)
        self.stock.grid(row=3, column=1, **cmpProp)

        Button(self, text="Registrar", command=lambda:self.registrarProducto()).grid(row=4, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=4, column=2, padx=6, pady=6)

        self.after(100, lambda: self.cargarCategorias())


    def cargarCategorias(self):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar('SELECT * FROM categorias')
            lista = []
            for valor in conexion.datos():
                lista.append(valor[1])
            self.categorias['values'] = lista
        except bd.Conexionerror:
            mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
        finally:
            if conexion:
                conexion.cerrar()


    def registrarProducto(self):
        idCategoria = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(f'SELECT id FROM categorias WHERE nombre = "{self.categorias.get()}" LIMIT 1')
            idCategoria = int(conexion.datos()[0][0])
        except bd.Conexionerror:
            mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
        finally:
            if conexion:
                conexion.cerrar()

        if idCategoria is not None:
            try:
                conexion = bd.Conexion()
                ins = conexion.ejecutar(f'''
                INSERT INTO productos(id_categoria, descripcion, precio, stock) 
                VALUES(
                    {idCategoria},
                    "{self.descr.get()}",
                    {float(self.precio.get())},
                    {int(self.stock.get())}
                )''')
                if ins > 0:
                    mb.showinfo(title="Producto registrado", message="Nuevo producto registrado: Ok!")
                    evt.salir(self)
                    evt.cargarProductos(None, self.productos)
            except bd.Conexionerror:
                mb.showerror(title="Error al conectar", message="Falló la operación en/con la base de datos.")
            finally:
                if conexion:
                    conexion.cerrar()
        else:
            mb.showerror(title="Categoría no encontrada", message=f"la categoría `{self.categorias.get()}` no fue encontrada.")


class Editarproducto(Dialogo):
    def __init__(self, root, titulo="Editar producto", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)


class Borrarproducto(Dialogo):
    def __init__(self, root, titulo="Borrar producto", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)
