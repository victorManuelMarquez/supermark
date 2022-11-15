import os
import sqlite3 as sql
import pandas

# devuelve la ruta absoluta a la base de datos (necesario para operar localmente)
def ruta_absoluta(bd_path):
    return os.path.join(os.path.dirname(__file__), bd_path)

class Conexion():

    def __init__(self, bd):
        self.__conexion = sql.connect(bd, detect_types=sql.PARSE_DECLTYPES | sql.PARSE_COLNAMES)
        self.__cursor = self.__conexion.cursor()

    def ejecutar(self, consulta):
        self.__cursor.execute(consulta)
        if 'INSERT' in consulta or 'UPDATE' in consulta or 'DELETE' in consulta:
            self.__conexion.commit()
    
    def datos(self):
        return self.__cursor.fetchall()

    def columnas(self):
        return [nombre[0] for nombre in self.__cursor.description]

    def deshacer(self):
        self.__conexion.rollback()
    
    def cerrar(self):
        self.__conexion.close()

def mostrar_tabla(conexion, tabla):
    print("Tabla:", tabla)
    conexion.ejecutar(f"SELECT * FROM {tabla}")
    print(pandas.DataFrame.from_records(data=conexion.datos(), columns=conexion.columnas()))

#********** TEST **********#
conexion = Conexion(ruta_absoluta('supermark-data.db'))
mostrar_tabla(conexion, 'personas')
mostrar_tabla(conexion, 'categorias')
mostrar_tabla(conexion, 'articulos_detalles')
mostrar_tabla(conexion, 'ventas_detalles')
conexion.cerrar()
