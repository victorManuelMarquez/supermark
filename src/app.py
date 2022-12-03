import componentes as cmp
from tkinter import Tk, font, BooleanVar


class App():
    def __init__(self, titulo="SuperMark - ¡Bienvenido!"):
        self.__root = Tk()

        # Fuente global
        self.defaultFont = font.nametofont('TkDefaultFont')
        self.defaultFont.configure(family="Segoe Script", size=11)

        # Personalización
        self.root.title(titulo)
        self.preferredSize(720, 522)

        # Estáticos
        self.cliente = BooleanVar(value=True)
        self.nextCampo = None
        self.sesion = False

        cmp.menuBar(self)
        cmp.moduloUsuario(self)
        cmp.moduloProducto(self)
        cmp.moduloCarrito(self)
        cmp.moduloOperaciones(self)


    @property
    def root(self):
        return self.__root


    def preferredSize(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (w, h, (sw-w)/2, (sh-h)/2))


    def iniciar(self):
        self.root.mainloop()


app = App()
app.iniciar()
