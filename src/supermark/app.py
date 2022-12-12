from tkinter import Tk, font
import componente as cmp


class App():
    """
    Una clase para contener la aplicación gráfica principal.

    ...
    
    métodos
    -------
    root()
        Devuelve la aplicación gráfica principal.
    preferredSize(w: int, h: int)
        Establece el tamaño de la ventana y la centra.
    iniciar()
        Esta función inicia la interfaz gráfica.
    """

    def __init__(self, titulo="Super Mark"):
        """
        parámetros
        ----------
        titulo : str, opcional
            título para la ventana
        """

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


    root.__doc__ = "Devuelve el componente gui."


    def preferredSize(self, w: int, h: int):
        """
        parámetros
        ----------
        w : int
            ancho determinado.
        h : int
            alto determinado.
        """

        sw = self.__root.winfo_screenwidth()
        sh = self.__root.winfo_screenheight()
        self.__root.geometry('%dx%d+%d+%d' % (w, h, (sw-w)/2, (sh-h)/2))


    preferredSize.__doc__ = "Establece el tamaño de la ventana y la centra."


    def iniciar(self):
        """
        Invoca a la función mainloop()
        """
        
        self.root.mainloop()


    iniciar.__doc__ = "Esta función inicia la interfaz gráfica."


app = App()
app.iniciar()
