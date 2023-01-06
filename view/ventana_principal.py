from tkinter import Tk
from tkinter.ttk import Style
from view.barra_de_menu import MenuBar
from view.panel_usuario import PanelUsuario
from view.panel_stock import PanelStock
from view.panel_cajero import PanelCajero
from view.dialogo.dialogo_salir import DialogoSalir


class App(Tk):
    """Ventana principal del sistema."""

    def __init__(self) -> Tk:
        """
        Construye la ventana principal.
        """

        super(App, self).__init__()

        # configuración
        self.title("SuperMark beta")
        self.configure(bg='#dcdad5')
        self.protocol('WM_DELETE_WINDOW', self.ventana_cerrandose)
        self.estilo = Style(self)
        if 'clam' in self.estilo.theme_names():
            self.estilo.theme_use('clam')

        # barra de menú
        menu_bar = MenuBar(self, tearoff=0)
        self.config(menu=menu_bar)

        # módulos
        self.columnconfigure(0, weight=1)

        PanelUsuario(self).grid(columnspan=2, padx=10, pady=5, sticky='ew')

        self.rowconfigure(1, weight=1)

        PanelStock(self).grid(padx=10, pady=5, sticky='nsew')

        PanelCajero(self).grid(row=1, column=1, rowspan=2, padx=5, pady=5, sticky='nsew')

        # posicionamiento
        self.update_idletasks()
        ancho = 854
        alto = 480
        if ancho*alto > self.winfo_width()*self.winfo_height():
            ancho = self.winfo_width()
            alto = self.winfo_height()
        coord_x_axis = self.winfo_rootx() - self.winfo_x()
        temp_x = ancho + 2 * coord_x_axis
        coord_y_axis = self.winfo_rooty() - self.winfo_y()
        temp_y = alto + coord_y_axis + coord_x_axis
        x = self.winfo_screenwidth() // 2 - temp_x // 2
        y = self.winfo_screenheight() // 2 - temp_y // 2
        self.geometry('%dx%d+%d+%d' % (ancho, alto, x, y))
        self.minsize(width=ancho, height=alto)
        self.deiconify()
        self.attributes('-alpha', 1.0)


    def ventana_cerrandose(self):
        """
        Muestra un diálogo para confirmar la salida.
        """

        DialogoSalir(self, titulo="Atención", mensaje="¿Desea salir del programa?")
