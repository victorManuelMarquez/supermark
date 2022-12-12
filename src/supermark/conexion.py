import sqlite3 as lite
import os


def rutaAlArchivo(file_database) -> str:
    """
    Devuelve la ruta absoluta al archivo de la base de datos.
    """
    return os.path.join(os.path.dirname(__file__), file_database)


class Conexion():
    """
    Clase para establecer una conexión con la base de datos.

    ...

    Métodos
    -------
    ejecutar(consulta : str)
        Aplica y devuele el total de filas modificadas (solo en UPDATE, DELETE y INSERT).
    resulset()
        Devuelve los resultados de la consulta.
    metadata()
        Devuelve las columnas de la consulta.
    cerrar()
        Cierra la conexión.
    """

    def __init__(self, bd_sqlite3=rutaAlArchivo("supermark.db")):
        """
        Parámetros
        ----------
        bd_sqlite3 : str, opcional
            Base de datos a conectar.
        """

        self.__con = lite.connect(bd_sqlite3, detect_types=lite.PARSE_DECLTYPES | lite.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()
    

    def ejecutar(self, consulta: str) -> int:
        """
        Parámetros
        ----------
        consulta : str
            Consulta SQL.
        
        Retorna
        -------
        int
            Cantidad de filas.
        """

        self.__cur.execute(consulta)
        print("OK! ")
        if 'INSERT' in consulta or 'UPDATE' in consulta or 'DELETE' in consulta:
            self.__con.commit()
        return self.__cur.rowcount
    

    @property
    def resulset(self) -> list:
        return self.__cur.fetchall()
    

    resulset.__doc__ = "Retorna el resultado de la consulta."


    @property
    def metadata(self) -> list:
        return [col[0] for col in self.__cur.description]
    

    metadata.__doc__ = "Retorna las columnas para los reultados."


    def cerrar(self):
        self.__con.close()


    cerrar.__doc__ = "Cierra la conexión"
