def eliminar_duplicados_ordenados(numeros: list[int] | None) -> list[int]:

    if numeros is None or len(numeros) == 0:
        return []

    sin_duplicados = []
    
    for num in numeros:
        if not num in sin_duplicados:
            sin_duplicados.append(num)
        return sin_duplicados

   
