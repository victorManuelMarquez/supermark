from view.dialogo.dialogo_base import Dialogo
from tkinter import Tk, Toplevel
from tkinter.ttk import Label, Button
from typing import Type


class DialogoSalir(Dialogo):
    """
    Ventana modal para que el usuario pueda elegir salir o no del sistema.
    """

    def __init__(self, root: Type[Tk | Toplevel], mensaje="¿Está seguro de salir?", **kwargs) -> Dialogo:
        """
        Construye el diálogo para salir o no del sistema.

        Parámetros
        ----------
        root: Type[Tk | Toplevel]
            ventana padre.
        """

        super(DialogoSalir, self).__init__(root, tiempo_inicial=0, **kwargs)

        self.columnconfigure(0, weight=1)

        lbl = Label(self, text=mensaje)
        lbl.grid(row=0, column=0, sticky='we', padx=10, pady=10, columnspan=2)

        btn_salir = Button(self, text="Salir", command=root.destroy)
        btn_salir.grid(row=1, column=0, padx=10, pady=10)

        btn_cancelar = Button(self, text="Cancelar", command=self.destroy)  # ¡no usar paréntesis en destroy!
        btn_cancelar.grid(row=1, column=1, padx=10, pady=10)

        self.ajustar_y_posicionar()
