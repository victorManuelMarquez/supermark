from tkinter import Tk, font
import componente as cmp


class App():

    def __init__(self, titulo="Super Mark"):
        self.__root = Tk()
        self._defaultFont = font.nametofont('TkDefaultFont')
        self._defaultFont.configure(family="Segoe Script", size=11)
        self.root.title(titulo)
        self.preferredSize(990, 600)
        self.cliente = {}
        cmp.menuBar(self)
        cmp.moduloUsuario(self)
        cmp.moduloProducto(self)
        cmp.moduloCarrito()
        cmp.moduloOperaciones(self)


    @property
    def root(self) -> Tk:
        return self.__root


    def preferredSize(self, w: int, h: int):
        sw = self.__root.winfo_screenwidth()
        sh = self.__root.winfo_screenheight()
        self.__root.geometry('%dx%d+%d+%d' % (w, h, (sw-w)/2, (sh-h)/2))


    def iniciar(self):
        self.root.mainloop()


app = App()
app.iniciar()
