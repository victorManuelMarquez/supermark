import sqlite3 as lite
import os


def rutaAlArchivo(file_database) -> str:
    return os.path.join(os.path.dirname(__file__), file_database)


class Conexion():
    def __init__(self, bd_sqlite3=rutaAlArchivo("supermark.db")):
        self.__con = lite.connect(bd_sqlite3, detect_types=lite.PARSE_DECLTYPES | lite.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()
    

    def ejecutar(self, consulta: str) -> int:
        self.__cur.execute(consulta)
        if 'INSERT' in consulta or 'UPDATE' in consulta or 'DELETE' in consulta:
            self.__con.commit()
        return self.__cur.rowcount
    

    @property
    def resulset(self) -> list:
        return self.__cur.fetchall()


    @property
    def metadata(self) -> list:
        return [col[0] for col in self.__cur.description]


    def cerrar(self):
        self.__con.close()
