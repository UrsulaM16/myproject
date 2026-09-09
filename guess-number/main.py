def run(target_number: int) -> None:
    intentos = 0

    while True:
        num_usuario = int(input("Introduzca número: "))
        intentos += 1

        if num_usuario < target_number:
            print("Mayor")
        elif num_usuario > target_number:
            print("Menor")
        else:
            print(f"Enhorabuena has encontrado el número en {intentos} intentos")
            break

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
