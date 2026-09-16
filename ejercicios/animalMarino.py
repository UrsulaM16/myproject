"""Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga 
«Hola, soy un animal marino!». Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar 
por «Hola soy un Pulpo!».
Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que 
muestre ese mesjae como parámetro."""
class Marino:
    def hablar(self):
        print("Hola, soy un animal marino!")


class Pulpo(Marino):
    # Sobreescribe el método hablar() de la clase padre
    def hablar(self):
        print("Hola soy un Pulpo!")


class Foca(Marino):
    # Recibe el atributo nuevo 'mensaje' en su constructor
    def __init__(self, mensaje: str):
        self.mensaje = mensaje

    # Muestra el mensaje recibido como atributo
    def hablar(self):
        print(self.mensaje)


# ==========================================
# PRUEBA DE EJECUCIÓN (Creación de objetos)
# ==========================================
if __name__ == "__main__":
    animal = Marino()
    pulpo = Pulpo()
    foca = Foca("Hola, soy una foca juguetona!")

    animal.hablar()  # Muestra: Hola, soy un animal marino!
    pulpo.hablar()  # Muestra: Hola soy un Pulpo!
    foca.hablar()  # Muestra: Hola, soy una foca juguetona!
