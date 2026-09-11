

def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        return None

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        print(i)
    return resultado

print(factorial(6))
