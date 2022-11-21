import os
import pandas
import conexion as bd

# devuelve la ruta absoluta a la base de datos (necesario para operar localmente)
def ruta_absoluta(bd_path):
    return os.path.join(os.path.dirname(__file__), bd_path)

def mostrar_tabla(conexion, tabla):
    print("Tabla:", tabla)
    conexion.ejecutar(f"SELECT * FROM {tabla}")
    print(pandas.DataFrame.from_records(data=conexion.datos(), columns=conexion.columnas()))

#********** TEST **********#
conexion = bd.Conexion(ruta_absoluta('supermark-data.db'))
mostrar_tabla(conexion, 'personas')
mostrar_tabla(conexion, 'categorias')
mostrar_tabla(conexion, 'productos')
mostrar_tabla(conexion, 'ventas_detalles')
conexion.cerrar()
