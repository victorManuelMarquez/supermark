import sqlite3 as sql

class Conexion():
    def __init__(self, bd='supermark.db'):
        self.__sqlconnection = sql.connect(bd)
        self.__cursor = self.__sqlconnection.cursor()
    

    def ejecutar(self, consulta, argumentos, autocommit=True):
        self.__sqlconnection.executemany(consulta, argumentos)
        if autocommit:
            self.__sqlconnection.commit()
        return self.__cursor.rowcount


    def datos(self):
        return self.__cursor.fetchall()


    def columnas(self):
        return [nombre for nombre in self.__cursor.description]


    def cerrar(self):
        self.__sqlconnection.close()
