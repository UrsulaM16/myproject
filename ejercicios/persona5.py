"""Ejercicio 2
Crea una clase “Persona”. Con atributos nombre y edad. Además, 
hay que crear un método “cumpleaños”, que aumente en 1 la edad de la 
persona cuando se invoque sobre un objeto creado con “Persona”.

Este es uno de los ejercicios de POO en Python más básicos para 
entender el concepto de métodos que modifican atributos.
Tendríamos que lograr ejecutar el siguiente código con la clase 
creada:
"""

class Persona:
    def __init__(self, nombre: str | None, edad: int | str | None) -> None:
        # Validacion defensiva del nombre
        if isinstance(nombre, str) and nombre.strip():
            self._nombre: str = nombre.strip()
        else:
            self._nombre: str = "Anónimo"

        # Validacion defensiva de la edad (evitando bools)
        if isinstance(edad, int) and not isinstance(edad, bool) and edad >= 0:
            self._edad: int = edad
        elif isinstance(edad, str):
            try:
                parsed = int(edad)
                self._edad = parsed if parsed >= 0 else 0
            except ValueError:
                self._edad = 0
        else:
            self._edad: int = 0

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    def cumpleaños(self) -> None:
        """Incrementa en 1 la edad del objeto."""
        self._edad += 1

    def __str__(self) -> str:
        return f"Persona: {self._nombre} | Edad: {self._edad}"

    # Creación de instancia y modificación de atributo por método
p = Persona("Juan", 20)
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")
# Salida: Juan cumple 21 años