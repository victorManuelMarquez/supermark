from model.conexion import Conexion


def grupo_usuario_registrado(nombre_usuario: str, clave: str) -> object:
    try:
        conexion = Conexion()
        conexion.ejecutar("""
        SELECT Grupo 
        FROM usuarios 
        WHERE `Nombre de Usuario` = '%s' AND `Clave Personal` = '%s' LIMIT 1
        """ % (nombre_usuario, clave))
        return conexion.resultset()
    except Exception as error:
        return error
    finally:
        if conexion:
            conexion.cerrar()
