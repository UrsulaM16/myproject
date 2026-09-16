"""Realizar un programa en el cual se declaren dos valores enteros por 
teclado utilizando el método __init__. Calcular después la suma, resta, 
multiplicación y división. Utilizar un método para cada una e imprimir 
los resultados obtenidos. Llamar a la clase Calculadora"""

class Calculadora:
    def __init__(self) -> None:
        """Pide dos valores enteros por teclado al instanciar la clase."""
        # Lectura defensiva del primer número
        try:
            self._num1: int = int(input("Ingrese el primer número entero: "))
        except ValueError:
            print("Entrada inválida. Se asignará 0 por defecto.")
            self._num1 = 0

        # Lectura defensiva del segundo número
        try:
            self._num2: int = int(input("Ingrese el segundo número entero: "))
        except ValueError:
            print("Entrada inválida. Se asignará 0 por defecto.")
            self._num2 = 0

    def sumar(self) -> int:
        """Calcula y devuelve la suma de los dos números."""
        return self._num1 + self._num2

    def restar(self) -> int:
        """Calcula y devuelve la resta de los dos números."""
        return self._num1 - self._num2

    def multiplicar(self) -> int:
        """Calcula y devuelve la multiplicación de los dos números."""
        return self._num1 * self._num2

    def dividir(self) -> float | None:
        """Calcula y devuelve la división protegiendo contra división por cero."""
        try:
            return self._num1 / self._num2
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero.")
            return None


# ==========================================
# CÓDIGO DE EJECUCIÓN E IMPRESIÓN DE RESULTADOS
# ==========================================
if __name__ == "__main__":
    # 1. Se crea el objeto (dispara el __init__ y pide los números por teclado)
    calc = Calculadora()

    # 2. Se invocan los métodos e imprimen los resultados
    print(f"\nSuma: {calc.sumar()}")
    print(f"Resta: {calc.restar()}")
    print(f"Multiplicación: {calc.multiplicar()}")

    resultado_div = calc.dividir()
    if resultado_div is not None:
        print(f"División: {resultado_div:.2f}")