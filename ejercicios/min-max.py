def obtener_min_max_suma(numeros: tuple[int, ...] | None) -> tuple[int, int, int]:
    # 1. Validación defensiva de entrada nula o vacía
    if numeros is None or len(numeros) == 0:
        return (0, 0, 0)

    # 2. Cálculo directo usando las funciones globales nativas
    minimo = min(numeros)
    maximo = max(numeros)
    suma_total = sum(numeros)

    # 3. Retorno de la tupla con los tres valores
    return (minimo, maximo, suma_total)