import sqlite3 as sql
from controller.operativo import ruta_al_archivo


class Conexion():
    """
    Establece la conexión con la base de datos.
    """

    def __init__(self, bd=ruta_al_archivo("../sources/database/supermark.db")):
        """
        Construye la conexión.
        """

        print(bd)
        self.__connect = sql.connect(bd, detect_types=sql.PARSE_DECLTYPES | sql.PARSE_COLNAMES)
        self.__cursor = self.__connect.cursor()


    def ejecutar(self, consulta: str) -> int:
        """
        Ejecuta la consulta en la base de datos.
        """

        self.__cursor.execute(consulta)
        if 'INSERT' in consulta or 'UPDATE' in consulta or 'DELETE' in consulta:
            self.__connect.commit()
        return self.__cursor.rowcount


    def resultset(self) -> list:
        """
        Devuelve la tabla resultante de la consulta.

        Advertencia: No llamar por segunda vez.
        """

        return self.__cursor.fetchall()


    def metadata(self) -> list:
        """
        Devuelve el nombre de las columnas de la tabla resultante.
        """

        return [col[0] for col in self.__cursor.description]


    def cerrar(self):
        """
        Cierra la conexión existente.
        """

        self.__connect.close()
