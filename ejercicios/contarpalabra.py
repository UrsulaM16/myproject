


def contar_frecuencia_palabras(elementos: list[str | None] | None) -> dict[str, int]:
    # 1. Validación defensiva de entrada nula o vacía
    if elementos is None or len(elementos) == 0:
        return {}

    frecuencias: dict[str, int] = {}

    # 2. Bucle de procesamiento de la lista
    for elem in elementos:
        # Filtrar solo elementos que sean instancias reales de str
        if isinstance(elem, str):
            palabra_limpia = elem.strip().lower()
            
            # Verificar que la cadena no haya quedado vacía tras la limpieza
            if palabra_limpia:
                # Patrón de acumulación seguro con .get()
                frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0) + 1

    return frecuencias