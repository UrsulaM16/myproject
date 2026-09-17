"""
class SoccerTeam:
    # 1. Añadimos todos los parámetros en el __init__
    def __init__(self, name: str, goalKeeper: str, defense: str, midfielder: str, 
                 striker: str, inChampions: bool, inCup: bool, yearFounded: int):
        
        # 2. Corregimos el punto en self.name y el nombre de midfielder
        self.name = name
        self.goalKeeper = goalKeeper
        self.defense = defense 
        self.midfielder = midfielder
        self.striker = striker
        self.inChampions = inChampions 
        self.inCup = inCup
        self.yearFounded = yearFounded

    def showTeamData(self):
        champions_texto = 'si' if self.inChampions else 'no'
        # 3. Corregimos el nombre de la variable para el print
        inCup_texto = 'si' if self.inCup else 'no'
        
        print(f"--- DATOS DEL EQUIPO: {self.name} ---")
        print(f"Año de fundación: {self.yearFounded}")
        print(f"Portero: {self.goalKeeper}")
        print(f"Defensa: {self.defense}")
        print(f"Centrocampista: {self.midfielder}")
        print(f"Delantero: {self.striker}")
        print(f"¿Juega en Champions?: {champions_texto}")
        print(f"¿Juega en Copa?: {inCup_texto}\n")


# Creación e impresión del objeto
equipo1 = SoccerTeam(
    name="Real Madrid",
    goalKeeper="Courtois",
    defense="Rüdiger",
    midfielder="Bellingham",
    striker="Vinicius",
    inChampions=True,
    inCup=True,
    yearFounded=1902
)

equipo1.showTeamData()


class Jedi:
    def __init__(self, name: str, lightSaberColor: str):
        self.name = name
        self.lightSaberColor = lightSaberColor

    # 2. Método: muestra el mensaje usando las propiedades del Jedi
    def showInfo(self):
        print(f"Soy un Jedi, mi nombre es {self.name} y el color de mi sable de luz es {self.lightSaberColor}")
nombres = ['Luke Skywalker', 'Mace Windu', 'Yoda', 'Qui-Gon Jinn', 'Obi-Wan Kenobi']
colores = ['azul', 'morado', 'verde', 'verde', 'azul']

for nombre, color in zip(nombres, colores):
    jedi_actual = Jedi(nombre, color)
    jedi_actual.showInfo()

class Grifo:
    def __init__(self, litros_deposito: float):
        # Atributos iniciales
        self.litros_deposito = litros_deposito
        self.valvula_abierta = False  # El grifo empieza con la válvula cerrada por seguridad

    def abrir_valvula(self):
        self.valvula_abierta = True
        print("Válvula abierta.")

    def cerrar_valvula(self):
        self.valvula_abierta = False
        print("Válvula cerrada.")

    def usar_grifo(self):
        # Comprobaciones según los requisitos del problema
        if not self.valvula_abierta:
            print("No sale agua: La válvula está cerrada.")
        elif self.litros_deposito <= 0:
            print("No sale agua: El depósito está vacío.")
        else:
            self.litros_deposito -= 1
            print(f"¡Grifo abierto! Gastado 1 litro. Agua restante: {self.litros_deposito}L")

# Creamos un grifo con un depósito de 2 litros de agua
mi_grifo = Grifo(litros_deposito=5)

# 1. Intentamos usarlo con la válvula cerrada
mi_grifo.usar_grifo()

# 2. Abrimos la válvula y gastamos agua
mi_grifo.abrir_valvula()
mi_grifo.usar_grifo()  # Gasta 1L (Queda 1L)
mi_grifo.usar_grifo()  # Gasta 1L (Queda 0L)

# 3. Intentamos usarlo cuando ya no queda agua
mi_grifo.usar_grifo()

class CaldoPollo:
    def __init__(self, ing_sustancia: int):
        self.ingredientes = []
        self.sustancia = False
        self.ing_sustancia = ing_sustancia
        self.max_ingredientes = 10

    def anadir_ingrediente(self, ingrediente: str):
        # 1. Corregido: plural self.ingredientes, añadido ':' y 'return'
        if len(self.ingredientes) >= self.max_ingredientes:
            print(f'No se puede añadir más {ingrediente}. El caldo ya tiene el máximo (10).')
            return

        # 2. Corregido: self.ingredientes.append
        self.ingredientes.append(ingrediente)
        print(f'Añadido: {ingrediente}')

        # 3. Actualizar la sustancia
        if len(self.ingredientes) >= self.ing_sustancia:
            self.sustancia = True

    def ver_receta(self) -> str:
        # 1. Comprobación de sustancia
        texto_sustancia = "Con sustancia" if self.sustancia else "Sin sustancia (está muy aguado)"
    
        # 2. Corregida la sangría del bloque if/else
        if not self.ingredientes:
            lista_ing = "Ninguno"
        else:
            lista_ing = ", ".join(self.ingredientes)

        # 3. Construcción del mensaje final
        receta = f"--- RECETA DEL CALDO DE POLLO ---\n"
        receta += f"Estado: {texto_sustancia}\n"
        receta += f"Ingredientes ({len(self.ingredientes)}/10): {lista_ing}\n"
    
        return receta


# --- Prueba del programa ---
mi_caldo = CaldoPollo(ing_sustancia=2)

mi_caldo.anadir_ingrediente("Agua")
print(mi_caldo.ver_receta())

mi_caldo.anadir_ingrediente("Pollo")
print(mi_caldo.ver_receta())
"""
class TiendaEmbutidos:
    def __init__(self, salchichones: int, chorizos: int, morcillas: int):
        # Guardamos el stock inicial en un diccionario para gestionarlo fácilmente
        self.stock = {
            "salchichon": salchichones,
            "chorizo": chorizos,
            "morcilla": morcillas
        }

    def consultar_stock(self):
        print("--- STOCK ACTUAL EN TIENDA ---")
        print(f"Salchichones: {self.stock['salchichon']}")
        print(f"Chorizos:     {self.stock['chorizo']}")
        print(f"Morcillas:    {self.stock['morcilla']}\n")

    def hacer_venta(self, **pedido):
        """
        Recibe los productos y cantidades a vender usando kwargs.
        Ejemplo de uso: tienda.hacer_venta(salchichon=2, chorizo=5)
        """
        # 1. Comprobar que no hay productos repetidos en el pedido
        # (Al usar argumentos con clave o diccionarios, Python impide duplicar claves automáticamente)

        # 2. VALIDACIÓN: Comprobar si hay stock suficiente de TODO antes de tocar nada
        for producto, cantidad in pedido.items():
            # Verificar si el producto existe en la tienda
            if producto not in self.stock:
                print(f"Error en la venta: El producto '{producto}' no existe en la tienda.\n")
                return
            
            # Verificar si hay suficiente cantidad
            if cantidad > self.stock[producto]:
                print(f"Venta cancelada: No hay suficiente stock de '{producto}'. "
                      f"Solicitado: {cantidad}, Disponible: {self.stock[producto]}.\n")
                return

        # 3. ACTUALIZACIÓN: Si todas las comprobaciones pasaron, descontamos del stock
        for producto, cantidad in pedido.items():
            self.stock[producto] -= cantidad

        print("¡Venta realizada con éxito!")
        for producto, cantidad in pedido.items():
            print(f" - Vendido: {cantidad} de {producto}")
        print()


# --- EJEMPLO DE USO Y PRUEBAS ---

# Creamos la tienda con 10 salchichones, 10 chorizos y 10 morcillas
mi_tienda = TiendaEmbutidos(salchichones=10, chorizos=10, morcillas=10)

# Consultamos el stock inicial
mi_tienda.consultar_stock()

# Venta 1: Venta válida de varios productos
print("Intentando Venta 1...")
mi_tienda.hacer_venta(salchichon=2, chorizo=5, morcilla=1)

# Consultamos el stock para ver el cambio
mi_tienda.consultar_stock()

# Venta 2: Intento de venta donde NO hay suficiente stock de morcillas
print("Intentando Venta 2...")
mi_tienda.hacer_venta(salchichon=1, morcilla=15)  # Quedaban 9 morcillas

# Verificamos que no se descontó tampoco el salchichón
mi_tienda.consultar_stock()































