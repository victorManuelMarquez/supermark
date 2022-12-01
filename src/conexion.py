import os
import sqlite3 as sql

# devuelve la ruta absoluta a la base de datos (necesario para operar localmente)
def ruta_absoluta(bd_path):
    return os.path.join(os.path.dirname(__file__), bd_path)


class Conexion():

    def __init__(self, db_path=ruta_absoluta("supermark.db")):
        self.__conexion = sql.connect(db_path, detect_types=sql.PARSE_DECLTYPES | sql.PARSE_COLNAMES)
        self.__cursor = self.__conexion.cursor()

    def ejecutar(self, consulta):
        self.__cursor.execute(consulta)
        if 'INSERT' in consulta or 'UPDATE' in consulta or 'DELETE' in consulta:
            self.__conexion.commit()
        return self.__cursor.rowcount

    def datos(self):
        return self.__cursor.fetchall()

    def columnas(self):
        return [nombre[0] for nombre in self.__cursor.description]
    
    def cerrar(self):
        self.__conexion.close()


class Conexionerror(sql.Error):
    pass
