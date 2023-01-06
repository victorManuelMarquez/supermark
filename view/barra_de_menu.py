from tkinter import Menu, Tk


class MenuBar(Menu):
    """
    Barra de menús.
    """

    def __init__(self, master: Tk, **kwargs) -> Menu:
        """
        Construye la barra de menús.
        """

        super(MenuBar, self).__init__(master, **kwargs)

        self.add_cascade(label="Archivo", menu=self.__instalar_menu_archivo(self))
        self.add_cascade(label="Editar", menu=self.__instalar_menu_editar(self))
        self.add_cascade(label="Ayuda", menu=self.__instalar_menu_ayuda(self))


    def __instalar_menu_archivo(self, main: Menu) -> Menu:
        """
        agrega el menú de archivo.
        """

        menu = Menu(main)
        menu.add_cascade(label="Datos", menu=self.__instalar_menu_database(menu))
        menu.add_separator()
        menu.add_command(label="Salir", command=exit)
        return menu


    def __instalar_menu_database(self, main: Menu) -> Menu:
        """
        agrega el menú de respaldo de datos.
        """

        menu = Menu(main)
        menu.add_command(label="Realizar una copia de seguridad")
        menu.add_command(label="Recuperar desde un archivo de respaldo")
        menu.add_separator()
        menu.add_command(label="Respaldar la sesión")
        menu.add_command(label="Recuperar una sesión")
        return menu


    def __instalar_menu_editar(self, main: Menu) -> Menu:
        """
        agrega el menú de edición.
        """

        menu = Menu(main)
        menu.add_command(label="Deshacer")
        menu.add_command(label="Rehacer")
        menu.add_separator()
        menu.add_command(label="Cortar")
        menu.add_command(label="Copiar")
        menu.add_command(label="Pegar")
        return menu


    def __instalar_menu_ayuda(self, main: Menu) -> Menu:
        """
        agrega el menú de ayuda.
        """

        menu = Menu(main)
        menu.add_command(label="Manual del usuario")
        menu.add_separator()
        menu.add_command(label="Acerca de")
        return menu
