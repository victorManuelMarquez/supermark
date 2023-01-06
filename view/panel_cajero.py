from tkinter import Tk, Listbox
from tkinter.ttk import Frame, Labelframe, Label, Entry, Button, Scrollbar
from typing import Type


class PanelCajero(Frame):
    """
    Panel para gestionar la compra/venta.
    """
    
    def __init__(self, root: Type[Tk | Frame | Labelframe], **kwargs):
        """
        Construye el panel con los componentes necesarios.

        Parámetros
        ----------
        root: Type[Tk | Frame | Labelframe]
            Contenedor o ventana donde alojar los componentes.
        """

        super(PanelCajero, self).__init__(root, **kwargs)

        Label(self, text="TOTAL:").grid(padx=10, pady=5)

        total = Entry(self, state='readonly')
        total.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        btn_comprar = Button(self, text="Comprar")
        btn_comprar.grid(padx=10, pady=5)

        btn_cancelar = Button(self, text="Cancelar")
        btn_cancelar.grid(row=1, column=1, padx=10, pady=5)

        self.rowconfigure(2, weight=1)

        marco = Labelframe(self, text="Ticket:")

        marco.rowconfigure(0, weight=1)
        marco.columnconfigure(0, weight=1)

        panel = Frame(marco)
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(0, weight=1)

        lista_compras = Listbox(panel)
        lista_compras.grid(sticky='nsew')

        xsb = Scrollbar(panel, orient='horizontal', command=lista_compras.xview)
        ysb = Scrollbar(panel, command=lista_compras.yview)

        lista_compras.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)

        xsb.grid(sticky='ew')
        ysb.grid(row=0, column=1, sticky='ns')

        panel.grid(padx=5, pady=5, sticky='nsew')

        marco.grid(columnspan=2, padx=5, pady=5, sticky='nsew')

        btn_vaciar_lista = Button(self, text="Vaciar lista")
        btn_vaciar_lista.grid(padx=10, pady=5)
