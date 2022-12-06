import sqlite3 as lite
import os


def rutaAlArchivo(file_database):
    return os.path.join(os.path.dirname(__file__), file_database)


class Conexion():
    def __init__(self, bd_sqlite3=rutaAlArchivo("supermark.db")):
        self.__con = lite.connect(bd_sqlite3, detect_types=lite.PARSE_DECLTYPES | lite.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()
    

    def ejecutar(self, consulta):
        print("statement ->", consulta)
        self.__cur.execute(consulta)
        print("OK! ")
        if 'INSERT' in consulta or 'UPDATE' in consulta or 'DELETE' in consulta:
            self.__con.commit()
        return self.__cur.rowcount
    

    @property
    def resulset(self):
        return self.__cur.fetchall()
    

    @property
    def metadata(self):
        return [col[0] for col in self.__cur.description]
    

    def cerrar(self):
        self.__con.close()
