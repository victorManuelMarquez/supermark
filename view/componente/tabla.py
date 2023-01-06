from tkinter import Tk, Toplevel
from tkinter.ttk import Labelframe, Frame, Treeview, Scrollbar
from typing import Type


class Tabla(Frame):
    """
    Tabla personalizada para mostrar un gran volumen de datos en espacios reducidos.
    """

    def __init__(self, root: Type[Tk | Toplevel | Frame | Labelframe], columnas: list = ['A', 'B', 'C'], filas: list = [], **kwargs) -> Frame:
        """
        Construye una tabla para mostrar información.

        Se usa la función `grid` para posicionar todos los componentes internos.

        Parámetros
        ----------
        root: Type[Tk | Toplevel | Frame, Labelframe]
            Ventana o contenedor.
        """

        super(Tabla, self).__init__(root, **kwargs)

        self._columnas = columnas
        self._filas = filas

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._tabla = Treeview(self, columns=self._columnas, show='headings', selectmode='extended')
        self._tabla.grid(row=0, column=0, sticky='nsew')

        xsb = Scrollbar(self, orient='horizontal', command=self._tabla.xview)
        ysb = Scrollbar(self, command=self._tabla.yview)

        self._tabla.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)

        xsb.grid(row=1, column=0, sticky='ew')
        ysb.grid(row=0, column=1, sticky='ns')

        self.grid(padx=5, pady=5, sticky='nsew')

        # mostrar datos al instanciar
        for columna in self._columnas:
            self._tabla.heading(columna, text=columna)

        for fila in self._filas:
            self._tabla.insert('', 'end', values=fila)


    @property
    def _columnas(self) -> list:
        return self.__columnas


    @_columnas.setter
    def _columnas(self, columnas):
        self.__columnas = columnas
    

    @property
    def _filas(self) -> list:
        return self.__filas
    

    @_filas.setter
    def _filas(self, filas):
        self.__filas = filas


    def agregar_fila(self, fila: list):
        """Agrega nuevos datos a la celdas."""

        self._filas.append(fila)
        self._tabla.insert('', 'end', values=fila)


    def agregar_columna(self, columna: str):
        """Agrega una columna nueva."""

        self._columnas.append(columna)
        self._tabla.heading(columna, text=columna)


    def refrescar(self):
        """Actualiza el todo el contenido de la tabla."""

        self._tabla.delete(*self._tabla.column())
        self._tabla.delete(*self._tabla.get_children())

        for columna in self._columnas:
            self._tabla.heading(columna, text=columna)

        for fila in self._filas:
            self._tabla.insert('', 'end', values=fila)


    def limpiar_datos(self):
        """Elimina todas las filas."""

        self._filas.clear()
        self._tabla.delete(*self._tabla.get_children())


    def purgar(self):
        """Remueve filas y columnas."""

        self._columnas.clear()
        self._filas.clear()
        self.refrescar()
