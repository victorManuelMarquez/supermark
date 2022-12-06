from tkinter.ttk import Treeview


class Tabla():
    def __init__(self, master, columnas = [], filas=[]):
        self.__tree = Treeview(master, show='headings', selectmode='extended', height=5)
        self.__cols = columnas
        self.__rows = filas
        self.__cargar_columnas()
        self.__cargar_filas()
    

    @property
    def cuerpo(self):
        return self.__tree
    

    @property
    def columnas(self):
        return self.__cols
    

    @columnas.setter
    def columnas(self, cols):
        self.__cols = cols
        self.__cargar_columnas()
    

    @property
    def filas(self):
        return self.__rows
    

    @filas.setter
    def filas(self, rows):
        self.__rows = rows
        self.__cargar_filas()
    

    def listaDiccionario(self):
        datos = []
        for fila in self.filas:
            datos.append(dict(zip(self.columnas, fila)))
        return datos
    

    def __cargar_columnas(self):
        self.cuerpo.config(columns=self.columnas)
        for columna in self.columnas:
            self.cuerpo.column(columna, minwidth=40, width=120, stretch=False)
            self.cuerpo.heading(columna, text=columna)


    def __cargar_filas(self):
        self.cuerpo.delete(*self.cuerpo.get_children())
        for fila in self.filas:
            self.cuerpo.insert('', 'end', values=fila)


    def refrescar(self):
        self.__cargar_columnas()
        self.__cargar_filas()


    def vaciar(self):
        self.columnas.clear()
        self.filas.clear()
        self.__cargar_columnas()
        self.__cargar_filas()
