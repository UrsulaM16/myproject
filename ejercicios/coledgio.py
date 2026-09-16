"""Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos 
el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

class Estudiante:
    def __init__(self, nombre: str, nota: float):
        # Usamos atributos privados con __
        self.__nombre = nombre
        self.__nota = nota

    # Getters (sin parámetros adicionales)
    def get_nombre(self) -> str:
        return self.__nombre

    def get_nota(self) -> float:
        return self.__nota

    # Setters (reciben el nuevo valor a asignar)
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_nota(self, nota: float):
        self.__nota = nota

    # Método para imprimir datos
    def imprimir(self):
        print(f"Nombre: {self.__nombre} | Nota: {self.__nota:.2f}")

    # Método para evaluar el resultado
    def resultados(self):
        if self.__nota >= 5:
            print(f"El estudiante {self.__nombre} ha aprobado.")
        else:
            print(f"El estudiante {self.__nombre} ha reprobado.")

    # Representación en string (formateo correcto dentro de la llave)
    def __str__(self):
        return f"El estudiante {self.__nombre} tiene una nota de {self.__nota:.2f}"


if __name__ == "__main__":
    estudiante1 = Estudiante("Luis", 10)
    estudiante1.imprimir()
    estudiante1.resultados()

    print("-" * 30)

    estudiante2 = Estudiante("Úrsula", 8)
    estudiante2.imprimir()
    estudiante2.resultados()