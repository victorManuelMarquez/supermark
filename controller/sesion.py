from model.consultas_sesion import grupo_usuario_registrado


def iniciar_sesion(nombre_usuario: str, clave: str) -> str:
    return grupo_usuario_registrado(nombre_usuario, clave)
