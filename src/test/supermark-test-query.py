import os
import pandas
import conexion as bd
from password_generator import PasswordGenerator

# devuelve la ruta absoluta a la base de datos (necesario para operar localmente)
def ruta_absoluta(bd_path):
    return os.path.join(os.path.dirname(__file__), bd_path)

def nuevo_cliente(conexion, dni, nombre_completo, usuario):
    clave = PasswordGenerator()
    clave.minlen = 8
    clave.maxlen = 8
    clave.minuchars = 0
    clave.excludelchars = "%)$(^-¿?<>*"
    clave = clave.generate()
    print(f'''
*** Datos ***
DNI: {dni}
NOMBRE COMPLETO: {nombre_completo}
USUARIO: {usuario}
CLAVE: {clave}
CLIENTE: True
ACTIVO: True
    ''')
    try:
        filas = conexion.ejecutar(f"INSERT INTO personas(dni, nombre_completo, usuario, clave) VALUES ('{dni}', '{nombre_completo}', '{usuario}', '{clave}')")
        print(filas, "filas insertadas.")
        mostrar_tabla(conexion, 'personas')
    except bd.sql.IntegrityError as error:
        print(f"ERROR({type(error).__name__})-> El dni/usuario : {dni}, ¡¡¡Ya existe!!!")

def actualizar_cliente(conexion, dni, dni_nuevo, nombre_completo, cambiar, inactivo):
    try:
        print("Actualizando...")
        filas = conexion.ejecutar(f'''
        UPDATE personas 
        SET 
            dni='{dni_nuevo}',
            nombre_completo='{nombre_completo}',
            cliente='{int(cambiar)}',
            activo='{int(inactivo)}'
        WHERE dni == '{dni}' ''')
        print(filas, "filas actualizadas.")
        mostrar_tabla(conexion, 'personas')
    except bd.sql.IntegrityError as error:
        print(f"ERROR({type(error).__name__})-> El dni/usuario : {dni_nuevo}, ¡¡¡Ya existe!!!")

def borrar_cliente(conexion, dni):
    filas = conexion.ejecutar(f"UPDATE personas SET activo = 0 WHERE dni={dni}")
    print(filas, "filas borradas.")
    mostrar_tabla(conexion, 'personas')

def mostrar_tabla(conexion, tabla):
    print("Tabla:", tabla)
    conexion.ejecutar(f"SELECT * FROM {tabla}")
    print(pandas.DataFrame.from_records(data=conexion.datos(), columns=conexion.columnas()))

#********** TEST **********#
conexion = bd.Conexion(ruta_absoluta('supermark.db'))
mostrar_tabla(conexion, 'personas')

# ingresos
nuevo_cliente(conexion, "35030111", "Ariel Juan Ángel Ocampo", "Ariel111")
nuevo_cliente(conexion, "40130333", "Facundo Nahuel Mamaní", "Facu333")

# actualizaciones
actualizar_cliente(conexion, "41103113", "41103113", "Ariel Juan Ángel Ocampo", True, False)

# "borrar"
borrar_cliente(conexion, "3503112")

conexion.cerrar()