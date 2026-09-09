def run(target: int) -> str:
    suma = 0
    multiplo = 0
    resultado = ""

    # Mientras la suma no llegue al objetivo...
    while suma < target:
        resultado += str(multiplo) + " "  # Pegamos el número y un espacio
        suma += multiplo  # Sumamos al total
        multiplo += 3  # Pasamos al siguiente múltiplo de 3

    return resultado.strip()  # .strip() solo quita el último espacio que sobra

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
