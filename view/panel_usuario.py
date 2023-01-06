from tkinter import Tk
from tkinter.ttk import Frame, Labelframe, Label, Entry, Button
from typing import Type
from controller.validacion import validar_campo_login


class PanelUsuario(Frame):
    """
    Panel para la gestión de las compras/ventas.
    """

    def __init__(self, root: Type[Tk | Frame | Labelframe], **kwargs) -> Frame:
        """
        Construye el panel con los componentes necesarios.

        Parámetros
        ----------
        root: Type[Tk | Frame | Labelframe]
            Contenedor o ventana donde alojar los componentes.
        """

        super(PanelUsuario, self).__init__(root, **kwargs)

        Label(self, text="Usuario:").grid(row=0, column=0)

        self.__campo_usuario = Entry(self, justify='right')
        self.__campo_usuario.grid(row=0, column=1, padx=10)

        Label(self, text="Contraseña:").grid(row=0, column=2)

        self.__campo_clave = Entry(self, show='*', justify='right')
        self.__campo_clave.grid(row=0, column=3, padx=10)

        btn_logout = Button(self, text="Cerrar sesión")
        btn_logout.grid(row=0, column=4, padx=10)

        valida_nombre = self.register(validar_campo_login)
        self.__campo_usuario.configure(validate='key', validatecommand=(valida_nombre, '%P'))

        valida_clave = self.register(validar_campo_login)
        self.__campo_clave.configure(validate='key', validatecommand=(valida_clave, '%P'))
