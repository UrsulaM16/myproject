import math

class poligono:
    def __init__ (self, tipo, parametro1, parametro2:None):
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
            