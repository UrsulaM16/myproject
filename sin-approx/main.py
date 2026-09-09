def run(x: float) -> float:
    # TODO
    resto = 180 - x
    numerador = 4 * x * resto
    denominador = 40_500 - x * resto
    sin = numerador / denominador
    print(f"sin({x}) = {sin}")
    return sin
    return sin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
