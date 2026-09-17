class Helado:
    def __init__(self, sabor: str):
        self.sabor = sabor

# 1. Indicamos (Helado) entre paréntesis para activar la herencia
class Frigopie(Helado):
    def __init__(self, sabor: str):
        super().__init__(sabor)

    def __str__(self) -> str:
        return f'Soy un Frigopie de {self.sabor}'


class SandwichNata(Helado):
    def __init__(self, sabor: str):
        super().__init__(sabor)

    def __str__(self) -> str:
        return f'Soy un SandwichNata de {self.sabor}'

    
class Calippo(Helado):
    def __init__(self, sabor: str):
        super().__init__(sabor)

    def __str__(self) -> str:
        return f'Soy un Calippo de {self.sabor}'

    
# Crear los objetos
helado1 = Frigopie("fresa")
helado2 = SandwichNata("nata y chocolate")
helado3 = Calippo("lima-limón")

# 2. Imprimir uno por uno
print(helado1)
print(helado2)
print(helado3)