"""Ejercicio 3: Clase Usuario de Red Social
Crea una clase UsuarioRedSocial para representar a los usuarios de una red social. La clase 
tiene los siguientes atributos: el nombre del usuario, una lista de amigos y una lista de 
publicaciones (llámalos con los nombres de variables que quieras).  La clase debe incluir un 
método que pinte por pantalla todos los parámetros del objeto UsuarioRedSocial, incluyendo los 
amigos que tiene y las publicaciones que ha hecho.

El programa pide al usuario que introduzca su nombre, los nombres de 3 amigos y los títulos de 
3 publicaciones que haya hecho en la red Social. A continuación, con los datos introducidos 
crea un objeto UsuarioRedSocial y pinta por pantalla los parámetros del objeto, empleando el 
método de la clase UsuarioRedSocial.  """
from xxlimited import Str

"""Ejercicio 3: Clase Usuario de Red Social
Crea una clase UsuarioRedSocial para representar a los usuarios de una red social. La clase 
tiene los siguientes atributos: el nombre del usuario, una lista de amigos y una lista de 
publicaciones (llámalos con los nombres de variables que quieras).  La clase debe incluir un 
método que pinte por pantalla todos los parámetros del objeto UsuarioRedSocial, incluyendo los 
amigos que tiene y las publicaciones que ha hecho.

El programa pide al usuario que introduzca su nombre, los nombres de 3 amigos y los títulos de 
3 publicaciones que haya hecho en la red Social. A continuación, con los datos introducidos 
crea un objeto UsuarioRedSocial y pinta por pantalla los parámetros del objeto, empleando el 
método de la clase UsuarioRedSocial.  """

class UsuarioRedSocial:

    def __init__(
        self, nombre: str, amigos: list[str], publicaciones: list[str]
    ) -> None:
        self.nombre = nombre
        self.amigos = amigos
        self.publicaciones = publicaciones

    def mostrar_informacion(self) -> None:
       
        print(f"USUARIO: {self.nombre}")
     

        print("Lista de Amigos:")
        for amigo in self.amigos:
            print(f"  - {amigo}")

    
        print("Publicaciones:")
        for pub in self.publicaciones:
            print(f"  - {pub}")
        print("========================================\n")



if __name__ == "__main__":
    # Pedir el nombre del usuario
    nombre_user = input("Introduce tu nombre de usuario: ")

    # 2Pedir 3 amigos usando un bucle
    amigos_user = []
    print("\n--- Introduce 3 amigos ---")
    for i in range(1, 4):
        amigo = input(f"Nombre del amigo {i}: ")
        amigos_user.append(amigo)

    #  Pedir 3 publicaciones usando un bucle
    publicaciones_user = []
    print("\n--- Introduce 3 títulos de publicaciones ---")
    for i in range(1, 4):
        titulo = input(f"Título de la publicación {i}: ")
        publicaciones_user.append(titulo)

    #  Crear el objeto de la clase UsuarioRedSocial
    usuario = UsuarioRedSocial(
        nombre=nombre_user,
        amigos=amigos_user,
        publicaciones=publicaciones_user,
    )

    #  Mostrar por pantalla los datos mediante el método de la clase
    usuario.mostrar_informacion()
        