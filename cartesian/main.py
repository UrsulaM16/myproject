def run(text1: str, text2: str) -> str:
    resultado = ""

    # Recorremos cada letra del primer texto
    for char1 in text1:
        # Para cada letra del primero, recorremos TODAS las del segundo
        for char2 in text2:
            resultado += char1 + char2

    return resultado


# Ejemplo de prueba
print(run("ab", "xy"))  # Devuelve: 'axaybxby'

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
