elementos = [" 10 ", None, True, 4.8, "hola", 7]

def limpiar_y_convertir_enteros(elementos: list[str | int | float | None] | None) -> list[int]:
    # 1. Guardia de seguridad con 'or'
    if elementos is None or len(elementos) == 0:
        return []

    resultado: list[int] = []

    # 2. Recorremos ELEMENTO POR ELEMENTO
    for item in elementos:
        # Descartar nulos y booleanos (True/False heredan de int en Python)
        if item is None or isinstance(item, bool):
            continue

        # Caso A: Ya es un entero estricto
        if isinstance(item, int):
            resultado.append(item)

        # Caso B: Es un número flotante (ej: 4.8 -> 4)
        elif isinstance(item, float):
            resultado.append(int(item))

        # Caso C: Es una cadena de texto (ej: " 10 " o "hola")
        elif isinstance(item, str):
            texto_limpio = item.strip()
            if texto_limpio:  # Verificar que no quedó vacía ("")
                try:
                    entero_convertido = int(texto_limpio)
                    resultado.append(entero_convertido)
                except ValueError:
                    # Si era "hola", int("hola") falla y cae aquí: lo ignoramos
                    pass

    return resultado

datos = [" 10 ", None, True, 4.8, "hola", 7]
print(limpiar_y_convertir_enteros(datos))
# Salida: [10, 4, 7]