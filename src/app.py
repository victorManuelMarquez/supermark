import componentes as cmp
from tkinter import Tk, Frame, font


class App():
    def __init__(self, titulo="SuperMark - ¡Bienvenido!"):
        self.__root = Tk()

        # Fuente global
        self.defaultFont = font.nametofont('TkDefaultFont')
        self.defaultFont.configure(family="Segoe Script", size=11)

        # Personalización
        self.root.title(titulo)
        self.preferredSize(720, 522)
        cmp.menuBar(self.root)
        cmp.moduloUsuario(Frame())
        cmp.moduloProducto(Frame())
        cmp.moduloCarrito(Frame())
        cmp.moduloOperaciones(Frame())


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
