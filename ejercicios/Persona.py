
"""Ejercicio 4
Crear una clase “Persona” que sea la clase padre de otra clase 
“Estudiante”. Por tanto:
En la clase “Persona” su método __init__() debe de estar preparado para 
recibir nombre y apellido. Además, esta clase , debe tener un método para 
mostrar nombre_completo() el cual debe mostrar el nombre acompañado del 
apellido.
La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además 
recibir los argumentos nombre y edad. También la clase “Estudiante”, recibe
 el valor “carrera”, y además contar con un método mostrar_carrera(). 
 Las dos clases son obligatorias."""
class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self) -> None:
        print(f"{self.nombre} {self.apellido}")


class Estudiante(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int, carrera: str) -> None:
        # Pasa nombre y apellido al constructor del padre (Persona)
        super().__init__(nombre, apellido)
        # Guarda lo propio del Estudiante
        self.edad = edad
        self.carrera = carrera

    def mostrar_carrera(self) -> None:
        print(self.carrera)


# Prueba de ejecución
if __name__ == "__main__":
    # Creamos un objeto de la clase Estudiante (no Persona)
    estudiante1 = Estudiante("Ursula", "Millan", 35, "Ingeniería")

    estudiante1.nombre_completo()  # Imprime: Ursula Millan (Heredado de Persona)
    estudiante1.mostrar_carrera()  # Imprime: Ingeniería (Propio de Estudiante)
