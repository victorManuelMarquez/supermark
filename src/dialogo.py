import eventos as evt
import conexion as bd
from tkinter import Toplevel, Label, Entry, Button, Checkbutton, messagebox as mb


class Dialogo(Toplevel):
    def __init__(self, root, titulo="Dialogo", ancho=320, alto=240):
        super().__init__(root)
        self.title(titulo)
        self.dimension(ancho, alto)
        self.resizable(width=False, height=False)
    
    def dimension(self, w, h):
        self.geometry("%dx%d" % (w, h))


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
                VALUES('{datos[0]}', '{datos[1]} {datos[2]}', '{datos[1]}', '{datos[2]}', '{True}')''')
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
    def __init__(self, root, titulo="Editar cliente", ancho=360, alto=276):
        super().__init__(root, titulo, ancho, alto)
        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Buscar:").grid(row=0, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=0, column=1, **cmpProp)

        Label(self, text="0 resultados").grid(row=1, column=0, padx=6, pady=6)
        Button(self, text="Anterior").grid(row=1, column=1, padx=6, pady=6)
        Button(self, text="Siguiente").grid(row=1, column=2, padx=6, pady=6)

        Label(self, text="D.N.I:").grid(row=2, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=2, column=1, **cmpProp)

        Label(self, text="Nombre:").grid(row=3, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=3, column=1, **cmpProp)

        Label(self, text="Apellido:").grid(row=4, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=4, column=1, **cmpProp)

        Checkbutton(self, text="Cliente").grid(row=5, column=1, columnspan=2)

        Checkbutton(self, text="Habilitado").grid(row=6, column=1, columnspan=2)

        Button(self, text="Actualizar").grid(row=7, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=7, column=2, padx=6, pady=6)


class Borrarcliente(Dialogo):
    def __init__(self, root, titulo="Borrar cliente", ancho=360, alto=228):
        super().__init__(root, titulo, ancho, alto)
        entryProp = {'justify':'left', 'bg':'#ffffff', 'width':25}
        cmpProp = {'columnspan':2, 'padx':6, 'pady':6}

        Label(self, text="Buscar:").grid(row=0, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=0, column=1, **cmpProp)

        Label(self, text="0 resultados").grid(row=1, column=0, padx=6, pady=6)
        Button(self, text="Anterior").grid(row=1, column=1, padx=6, pady=6)
        Button(self, text="Siguiente").grid(row=1, column=2, padx=6, pady=6)

        Label(self, text="D.N.I:").grid(row=2, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=2, column=1, **cmpProp)

        Label(self, text="Nombre:").grid(row=3, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=3, column=1, **cmpProp)

        Label(self, text="Apellido:").grid(row=4, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=4, column=1, **cmpProp)

        Button(self, text="Borrar").grid(row=5, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=5, column=2, padx=6, pady=6)


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
    def __init__(self, root, titulo="Nuevo producto", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)


class Editarproducto(Dialogo):
    def __init__(self, root, titulo="Editar producto", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)


class Borrarproducto(Dialogo):
    def __init__(self, root, titulo="Borrar producto", ancho=320, alto=240):
        super().__init__(root, titulo, ancho, alto)
