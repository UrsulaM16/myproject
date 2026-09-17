"""Ejercicio 4: Personajes de un juego
Define una clase Personaje para representar a los personajes de un juego. La clase 
tiene los atributos: nombre del personaje, nivel alcanzado y puntos de vida 
(llámalos con los nombres de variables que quieras).  Luego, crea las clases hijas: 
Guerrero y Mago con al menos un parámetro específico para cada una de ellas.

El programa pregunta al usuario si quiere crear un Personaje Guerrero o Mago. 
En función de lo que indique el usuario, el programa pide al usuario los datos 
necesarios para crear el objeto y lo crea. Finalmente, indica por pantalla que el 
objeto ha sido creado y pinta los parámetros del objeto."""
#Define una clase Personaje

class Personaje:
    __PUNTOS_VIDA = 100

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.nivel = 0
        self.puntos_de_vida = Personaje.__PUNTOS_VIDA

    @property
    def nombre(self) -> str:
        return self.__nombre

    @classmethod
    def obtener_puntos_vida_base(cls) -> int:
        return cls.__PUNTOS_VIDA

    @classmethod
    def modificar_puntos_vida_base(cls, nuevos_puntos: int) -> None:
        if nuevos_puntos > 0:
            cls.__PUNTOS_VIDA = nuevos_puntos
        else:
            print("Los puntos de vida deben ser un valor positivo.")


class Guerrero(Personaje):

    def __init__(self, nombre: str, *armamento) -> None:
        super().__init__(nombre)
        self.__armamento = armamento

    def __str__(self) -> str:
        armas = (
            ", ".join(self.__armamento) if self.__armamento else "Sin armas"
        )
        return f"[Guerrero] {self.nombre} | Nivel: {self.nivel} | HP: {self.puntos_de_vida} | Armas: {armas}"


class Mago(Personaje):

    def __init__(self, nombre: str, *poderes) -> None:
        super().__init__(nombre)
        self.__poderes = poderes

    def __str__(self) -> str:
        habilidades = (
            ", ".join(self.__poderes) if self.__poderes else "Sin poderes"
        )
        return f"[Mago] {self.nombre} | Nivel: {self.nivel} | HP: {self.puntos_de_vida} | Poderes: {habilidades}"


# ==========================================
# CLASE GESTORA (Ampliación solicitada)
# ==========================================
class GestorPersonajes:

    def __init__(self) -> None:
        # Permite almacenar un número indeterminado de personajes de cualquier tipo
        self.__personajes: list[Personaje] = []

    def agregar_personaje(self, personaje: Personaje) -> None:
        """Añade un objeto Personaje (o cualquier clase hija) a la lista."""
        if isinstance(personaje, Personaje):
            self.__personajes.append(personaje)
            print(f"✅ ¡Objeto {personaje.nombre} creado y añadido con éxito!")
        else:
            print("❌ Error: Solo se pueden añadir objetos de tipo Personaje.")

    def mostrar_personajes(self) -> None:
        """Muestra por pantalla todos los personajes registrados en el gestor."""
        print("\n================ LISTA DE PERSONAJES ================")
        if not self.__personajes:
            print("No hay personajes registrados en el gestor.")
        else:
            for p in self.__personajes:
                print(f"  - {p}")
        print("=====================================================\n")


# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ in ("__main__", "Ejercicio4"):
    # Instanciamos la clase gestora
    gestor = GestorPersonajes()

    # Bucle interactivo para crear personajes
    while input("¿Desea crear un personaje? [S/N]: ").strip().upper() == "S":
        nombre = input("Introduzca su nombre: ").strip().title()
        tipo = input("Indique si es Mago (M) o Guerrero (G): ").strip().upper()

        match tipo:
            case "G":
                armas_raw = input(
                    "Introduzca su armamento separado por comas: "
                )
                armamento = [a.strip() for a in armas_raw.split(",") if a.strip()]
                # Creamos el objeto y lo añadimos al gestor
                nuevo_guerrero = Guerrero(nombre, *armamento)
                gestor.agregar_personaje(nuevo_guerrero)

            case "M":
                poderes_raw = input(
                    "Introduzca sus poderes separados por comas: "
                )
                poderes = [p.strip() for p in poderes_raw.split(",") if p.strip()]
                # Creamos el objeto y lo añadimos al gestor
                nuevo_mago = Mago(nombre, *poderes)
                gestor.agregar_personaje(nuevo_mago)

            case _:
                print("⚠️ ¡No es un tipo de personaje válido!")

    # Mostramos todos los personajes utilizando el método del gestor
    gestor.mostrar_personajes()