def run():
    # TODO
    num1 = int(input('Ingrese el primer número: '))
    num2 = int(input('Ingrese el segundo número: '))

    sumar = num1 + num2
    restar = num1 - num2
    multiplicar = num1 * num2
    dividir: float = num1 / num2

    print(num1, '+', num2, '=', sumar, '\n', num1, '-', num2, '=', restar, '\n', num1, '*', num2, '=', multiplicar, '\n', num1, '/', num2, '=', dividir, sep='')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
