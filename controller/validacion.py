from re import compile, fullmatch


def validar_campo_estandar(txt: str) -> bool:
    """Permite solo el ingreso de `letras`, `números`, `espacios` y solo un par de caracteres especiales."""

    return fullmatch(compile('^[a-zA-Z0-9 _@!#]+$'), txt) != None or len(txt) == 0 # necesario para limpiar el campo.


def validar_campo_login(txt: str) -> bool:
    """Permite solo el ingreso de `letras`, `números` y `guiones de subrayado`."""

    return fullmatch(compile('^[a-zA-Z0-9_!@#]+$'), txt) != None or len(txt) == 0
