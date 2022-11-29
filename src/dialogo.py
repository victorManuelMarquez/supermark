import eventos as evt
from tkinter import Toplevel, Label, Entry, Button, Checkbutton


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
        Entry(self, **entryProp).grid(row=0, column=1, **cmpProp)

        Label(self, text="Nombre:").grid(row=1, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=1, column=1, **cmpProp)

        Label(self, text="Apellido:").grid(row=2, column=0, padx=6, pady=6)
        Entry(self, **entryProp).grid(row=2, column=1, **cmpProp)

        Button(self, text="Registrar").grid(row=3, column=1, padx=6, pady=6)
        Button(self, text="Cancelar", command=lambda:evt.salir(self)).grid(row=3, column=2, padx=6, pady=6)


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
    def __init__(self, root, titulo="Nueva categoría", ancho=320, alto=66):
        super().__init__(root, titulo, ancho, alto)

        Label(self, text="Nombre:").grid(row=0, column=0, padx=6, pady=6)
        Entry(self, justify='right', bg='#ffffff').grid(row=0, column=1, columnspan=2, padx=6, pady=6)

        Button(self, text="Registrar").grid(row=1, column=1, padx=6, pady=6)
        Button(self, text="Cancelar").grid(row=1, column=2, padx=6, pady=6)


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
