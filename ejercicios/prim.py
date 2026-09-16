def obtener_primer_y_ultimo(listado: list[int] | None) -> list[int]:
    # 1. Caso A: Si es None o está vacía, devuelve []
    if listado is None or len(listado) == 0:
        return []

    # 2. Caso B: Si tiene 1 o 2 elementos, la devuelve tal cual
    if len(listado) <= 2:
        return listado

    # 3. Caso C: Si tiene más de 2 elementos, toma el primero y el último
    return [listado[0], listado[-1]]