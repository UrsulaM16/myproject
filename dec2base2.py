import math
from abc import ABC, abstractmethod


class Poligono(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float | None:
        pass


class Triangulo(Poligono):
    def __init__(self, base: float, altura: float):
        self.base: float = base
        self.altura: float = altura

    def area(self) -> float:
        return 0.5 * self.base * self.altura

    def perimetro(self) -> float:
        # Supuesto que es equilátero
        return 3 * self.base


class Cuadrado(Poligono):
    def __init__(self, lado: float):
        self.lado: float = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado