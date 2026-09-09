def run(num1: int, num2: int, op: str) -> float:
    # TODO
    match op :
        case "+":
            result = num1 + num2
        case "-":
            resulta = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2
        case _:
            result = None

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
