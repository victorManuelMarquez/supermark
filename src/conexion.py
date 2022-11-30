import os
import sqlite3 as sql

# devuelve la ruta absoluta a la base de datos (necesario para operar localmente)
def ruta_absoluta(bd_path):
    return os.path.join(os.path.dirname(__file__), bd_path)

class Conexion():
    def __init__(self, bd=ruta_absoluta('supermark.db')):
        self.__sqlconnection = sql.connect(bd)
        self.__cursor = self.__sqlconnection.cursor()
    

    def ejecutar(self, consulta, parametros):
        self.__sqlconnection.executemany(consulta, parametros)
        return self.__cursor.rowcount


    def datos(self):
        return self.__cursor.fetchall()


    def columnas(self):
        return [nombre for nombre in self.__cursor.description]


    def cerrar(self):
        self.__sqlconnection.close()


class Conexionerror(sql.Error):
    pass
