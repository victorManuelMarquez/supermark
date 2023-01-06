from tkinter import Tk, StringVar, IntVar
from tkinter.ttk import Frame, Labelframe, Label, Entry, Spinbox, Scale
from typing import Type
from view.componente.tabla import Tabla


class PanelStock(Labelframe):
    """
    Panel para la exhibición de los productos en venta.
    """

    def __init__(self, root: Type[Tk | Frame | Labelframe], **kwargs) -> Labelframe:
        """
        Construye el panel con los componentes necesarios.

        Parámetros
        ----------
        root: Type[Tk | Frame | Labelframe]
            Contenedor o ventana donde alojar los componentes.
        """

        super(PanelStock, self).__init__(root, text="Stock:", **kwargs)

        Label(self, text="Buscar").grid(row=0, column=0, padx=10, pady=5)

        campo_buscar = Entry(self)
        campo_buscar.grid(row=0, column=1, columnspan=2, sticky='we', padx=10, pady=5)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        tabla_stock = Tabla(self)
        tabla_stock.grid(row=1, column=0, columnspan=4, sticky='nswe')

        Label(self, text="# de filas").grid(padx=5, pady=5)

        total_filas = StringVar(value="100")

        limitar_filas = Spinbox(self, from_=100, to=1000, values=tuple(range(100, 1001, 100)), textvariable=total_filas, wrap=True, width=5)
        limitar_filas.grid(row=2, column=1, padx=5, pady=5)

        info = Label(self, text="0 filas en 0.000 segundos")
        info.grid(row=2, column=2, padx=2, pady=5, sticky='ew')

        paginas = IntVar(value=0)

        paginador = Scale(self, from_=0, to=0, variable=paginas, orient='horizontal')
        paginador.grid(row=2, column=3, padx=10, pady=5, sticky='ew')
