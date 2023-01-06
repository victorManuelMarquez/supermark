

def porcentaje(valor: int, total: int) -> float:
    if valor > total:
        raise ValueError(f"Se esperaba 100% se obtuvo: {valor} > {total} = {valor * 100 / total}%")
    try:
        return valor * 100 / total
    except ZeroDivisionError:
        return 0
