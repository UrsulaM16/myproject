"""Ejercicio: Hacer una clase que mantenga un agregado de poligonos regulares.
Los poligonos pueden ser al menos: triángulos, cuadrados, rectangulos, pentágonos y círculos
Para cada polígono se ha de guardar el numero de lados o su radio
y los datos necesarios para calcular el área y perímetro
Ha de tener un metodo que calcule el area y otro para el perimetro. 
Implementar dos objetos de la clase y añadirle a cada uno de ellos 3 poligonos 
mostrar para cada agregado el tipo de poligono , su perimetro y area.
"""
import math #TRAE LA LIBRERIA DE FUNCIONES MATEMATICAS. sqrt(), math.pi
from abc import ABC, abstractmethod 
"""from abc modulo de python import ABC-> la herramienta, la clase
ABC: Es la clase base que debemos heredar para convertir nuestra propia clase en abstracta.

abstractmethod: Es un decorador (se usa escribiendo @abstractmethod sobre un método) 
que obliga a las clases hijas a definir obligatoriamente ese método.
"""

import math

class Poligono:
    def __init__(self, tipo, parametro1, parametro2=None):
        self.tipo = tipo
        self.param1 = parametro1
        self.param2 = parametro2
    
    def calcular_area(self):
        if self.tipo == "triángulo":
            return (math.sqrt(3) / 4) * self.param1 ** 2
        elif self.tipo == "cuadrado":
            return self.param1 ** 2
        elif self.tipo == "círculo":
            return math.pi * self.param1 ** 2
        elif self.tipo == "rectángulo":
            return self.param1 * self.param2
        elif self.tipo == "pentágono":
            perimetro = 5 * self.param1
            return (perimetro * self.param2) / 2
    
    def calcular_perimetro(self):
        if self.tipo == "triángulo":
            return 3 * self.param1
        elif self.tipo == "cuadrado":
            return 4 * self.param1
        elif self.tipo == "círculo":
            return 2 * math.pi * self.param1
        elif self.tipo == "rectángulo":
            return 2 * (self.param1 + self.param2)
        elif self.tipo == "pentágono":
            return 5 * self.param1


class AgregadoPoligonos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.poligonos = []
    
    def agregar(self, poligono):
        self.poligonos.append(poligono)
    
    def mostrar_informacion(self):
        print(f"\n{'='*60}")
        print(f"AGREGADO: {self.nombre}")
        print(f"{'='*60}")
        
        for i, poligono in enumerate(self.poligonos, 1):
            print(f"\nPolígono {i}:")
            print(f"  Tipo: {poligono.tipo}")
            print(f"  Perímetro: {poligono.calcular_perimetro():.2f}")
            print(f"  Área: {poligono.calcular_area():.2f}")
        
        area_total = sum(p.calcular_area() for p in self.poligonos)
        perimetro_total = sum(p.calcular_perimetro() for p in self.poligonos)
        
        print(f"\n{'─'*60}")
        print(f"TOTALES del agregado:")
        print(f"  Área total: {area_total:.2f}")
        print(f"  Perímetro total: {perimetro_total:.2f}")


if __name__ == "__main__":
    
    agregado1 = AgregadoPoligonos("AGREGADO 1")
    
    triangulo1 = Poligono("triángulo", 5)
    agregado1.agregar(triangulo1)
    
    cuadrado1 = Poligono("cuadrado", 4)
    agregado1.agregar(cuadrado1)
    
    circulo1 = Poligono("círculo", 3)
    agregado1.agregar(circulo1)
    
    
    agregado2 = AgregadoPoligonos("AGREGADO 2")
    
    rectangulo = Poligono("rectángulo", 6, 4)
    agregado2.agregar(rectangulo)
    
    penta = Poligono("pentágono", 4, 2.75)
    agregado2.agregar(penta)
    
    triangulo2 = Poligono("triángulo", 6)
    agregado2.agregar(triangulo2)
    
    
    agregado1.mostrar_informacion()
    agregado2.mostrar_informacion()
    
    print(f"\n{'='*60}\n")

