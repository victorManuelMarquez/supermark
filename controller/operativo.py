from os import path


def ruta_al_archivo(archivo) -> str:
    return path.join(path.dirname(__file__), archivo)
