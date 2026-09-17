class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.__titular = titular
        self.__saldo = saldo

    # Getters y Setters
    def get_titular(self) -> str:
        return self.__titular

    def set_titular(self, titular: str):
        self.__titular = titular

    def get_saldo(self) -> float:
        return self.__saldo

    def set_saldo(self, saldo: float):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Error: El saldo no puede ser negativo.")

    # Operaciones bancarias
    def ingresar(self, cantidad: float):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Ingreso de {cantidad:.2f}€ realizado correctamente.")
        else:
            print("ERROR: La cantidad a ingresar debe ser mayor que 0.")

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            print("ERROR: La cantidad a retirar debe ser mayor que 0.")
        elif cantidad > self.__saldo:
            print("FONDOS INSUFICIENTES: No puedes retirar más dinero del disponible.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad:.2f}€ realizado correctamente.")

    # Representación en texto
    def __str__(self) -> str:
        return f"Cuenta de {self.__titular} | Saldo: {self.__saldo:.2f}€"


if __name__ == "__main__":
    titular1 = CuentaBancaria("Úrsula Millán", 1200.35)
    print(titular1)

    # Probamos un ingreso
    titular1.ingresar(300)
    print(titular1)

    # Probamos un retiro válido
    titular1.retirar(500)
    print(titular1)

    # Probamos un retiro inválido (sin fondos)
    titular1.retirar(2000)
    