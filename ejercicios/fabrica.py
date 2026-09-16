"""Ejercicio 5
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno."""

class Fabrica():
    def __init__(self, llantas: int, color: str, precio: float):
        self.llantas = llantas
        self.color = color
        self.precio = precio


    def nllantas(self):
        #print(f'El numero de llantas es {self.llantas}')
        return self.llantas
       
    def colorvehiculo(self):
        print(f'El color es {self.color}')
       
    def preciovehiculo(self):
        print(f'El precio es {self.precio}')  


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2,color, precio)  


    def __str__(self):
        return f'Esta moto tiene {self.nllantas()} llantas, es de color {self.color} y tiene un precio de {self.precio}'            


class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)


    def __str__(self):
            return f'Este carro tiene {self.llantas} llantas, es de color {self.color} y tiene un precio de {self.precio}'    
           
if __name__ in ('__main__', 'fabrica.py'):
    moto = Moto( 'rojo', 1330.0)
    carro = Carro( 'azul', 3450.0)
    print(moto)
    print(carro)
