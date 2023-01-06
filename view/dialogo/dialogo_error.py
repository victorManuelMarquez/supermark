from tkinter import Tk, Toplevel
from tkinter.ttk import Label, Button, Progressbar
from view.dialogo.dialogo_base import Dialogo
from typing import Type


class DialogoError(Dialogo):
    """
    Ventana modal para mostrar un error sucedido en tiempo de ejecución.
    """

    def __init__(self, root: Type[Tk | Toplevel], mensaje: str = "", btn_txt: str = "Ok", **kwargs) -> Dialogo:
        """
        Construye la ventana modal.

        Parámetros
        ----------
        root: Type[Tk | Toplevel]
            Ventana padre.
        mensaje: str
            Mensaje del error.
        btn_txt: str
            Texto para el botón.
        """

        super(DialogoError, self).__init__(root, **kwargs)

        self.columnconfigure(0, weight=1)

        lbl = Label(self, text=mensaje)
        lbl.grid(row=0, column=0, sticky='we', padx=10, pady=10)

        Progressbar(self, orient='horizontal', mode='determinate', variable=self.tiempo_restante).grid(row=1, column=0, sticky='we')

        btn = Button(self, text=btn_txt, command=self.destroy) # ¡no usar paréntesis en destroy!
        btn.grid(row=2, column=0, padx=10, pady=10)

        self.ajustar_y_posicionar()
