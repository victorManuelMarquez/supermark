from tkinter import Tk, Toplevel, StringVar, BooleanVar
from typing import Type
from controller.aritmeticos import porcentaje


class Dialogo(Toplevel):
    """
    Ventana de tipo modal para el interactuar con el usuario.
    """

    def __init__(self, root: Type[Tk | Toplevel], titulo: str = "Diálogo modal", tiempo_inicial: int = 60, is_resizable: bool = False, **kwargs) -> Toplevel:
        """
        Construye una ventana modal.

        Parámetros
        ----------
        root: Type[Tk | Toplevel]
            Ventana padre.
        titulo: str
            Título para la ventana modal.
        tiempo_inicial: int
            Tiempo predeterminado para cerrar la ventana.
        is_resizable: bool
            La ventana puede o no modificar su tamaño en todas las direcciones.
        """
        
        super(Dialogo, self).__init__(root, **kwargs)

        self.tiempo_inicial = tiempo_inicial

        self.tiempo_restante = StringVar(value=str(tiempo_inicial))

        # no se incluye en el contructor
        self.pausa = BooleanVar(value=False) # usarse solo en tiempo de ejecución si es necesario.

        # configuración
        self.title(titulo)
        self.config(bg='#dcdad5')
        self.attributes('-topmost', True)
        self.resizable(width=is_resizable, height=is_resizable)

        self.wait_visibility()
        # restringue toda la actividad solo a esta ventana.
        self.grab_set() # ¡CUIDADO! bloquea la interfaz del programa.

        # conteo regresivo
        self.__auto_cierre(tiempo_inicial)


    @property
    def tiempo_inicial(self) -> int:
        return self.__tiempo_inicial
    

    @tiempo_inicial.setter
    def tiempo_inicial(self, tiempo: int):
        # 0 -> "ilimitado"
        # 120 -> 2 minutos máximo
        if tiempo >= 0 and tiempo <= 120:
            self.__tiempo_inicial = tiempo
        else:
            self.__tiempo_inicial = 0


    @property
    def tiempo_restante(self) -> StringVar:
        return self.__tiempo_restante


    @tiempo_restante.setter
    def tiempo_restante(self, variable: StringVar):
        self.__tiempo_restante = variable


    @property
    def pausa(self) -> BooleanVar:
        return self.__pausado
    

    @pausa.setter
    def pausa(self, pausar: bool):
        self.__pausado = pausar


    def __auto_cierre(self, tiempo_restante):
        """Inicia el "cronómetro" regresivo para cerrar esta ventana."""

        if not self.pausa.get() and self.tiempo_inicial > 0:
            self.tiempo_restante.set(value=str(porcentaje(tiempo_restante, self.tiempo_inicial)))

            if tiempo_restante > 0:
                tiempo_restante -= 1
                self.after(1000, self.__auto_cierre, tiempo_restante)
            else:
                self.destroy()


    def ajustar_y_posicionar(self):
        """Calcula el tamaño y la posición de esta ventana en pantalla."""

        self.update()

        ancho = self.winfo_width()
        alto = self.winfo_height()

        coord_x_axis = self.winfo_rootx() - self.winfo_x()
        temp_x = ancho + 2 * coord_x_axis
        coord_y_axis = self.winfo_rooty() - self.winfo_y()
        temp_y = alto + coord_y_axis + coord_x_axis
        x = self.winfo_screenwidth() // 2 - temp_x // 2
        y = self.winfo_screenheight() // 2 - temp_y // 2
        self.geometry('%dx%d+%d+%d' % (ancho, alto, x, y))
