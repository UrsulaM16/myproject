"""**Reto 1 (Reiterado):** Implementa una función que reciba una lista de 
números enteros y devuelva la suma de todos los números pares.

**Tiempo objetivo:** 5 minutos.


def sumarpares(numeros: list[int]): -> int:
    suma_total = 0
    return sum(n for n in numeros if n % 2 == 0)
print(sumarpares()) #quiero verlo en consola

**Reto 2 (Reiterado):** Debes demostrar que puedes operar 
con la mutabilidad de los diccionarios.

**`word_counts = {"python": 2, "code": 1, "function": 3, 
"test": 1}`**

Implementa una función que realice ambas tareas:
1.  **Filtrar:** Retorne solo las palabras cuya frecuencia 
es estrictamente mayor que 1.
2.  **Mutar (Eficiencia):** Modifica el diccionario 
original (`word_counts`) para que solo contenga las 
palabras que aparecen más de una vez.


word_counts = {"python": 2, "code": 1, "function": 3, "test": 1}
def str_mut(palabras: str): -> str
pfrecuencia = [""]
     for palabra en palabras:
         if palabra > 1:
    return pfrecuencia
else:
"*Tiempo objetivo:** 10 minutos.
class DataProcessor:
    def __init__(self, data: dict): -> dict
        self.data = data 

    def filter_duplicates(self, data: dict): -> dict

edad: int = 30
altura : float = 1.75
nombre : str = "José"

print(f'Nombre: {nombre} | {type(nombre)}|| Edad {edad} | {type(edad)} || Altura {altura}cm  | {type(altura)})')
 ----------------------------------------------------------------------------------------    
def procesar_registros(datos: list[dict[str, int | str]] | None) -> tuple[int, int]:
    # Cortocircuito: si datos es None o está vacío, retorna de inmediato
    if not datos:
        return (0, 0)
    
    suma_prioridad: int = 0
    registros_validos: int = 0
    
    for registro in datos:
        # 1. Validar que el elemento sea realmente un diccionario
        if not isinstance(registro, dict):
            continue
            
        # 2. Obtener el valor de "prioridad"
        valor_prioridad = registro.get("prioridad")
        
        # 3. Validar que la clave exista y que su valor sea estrictamente un entero (excluyendo bool, ya que bool hereda de int en Python)
        if isinstance(valor_prioridad, int) and not isinstance(valor_prioridad, bool):
            suma_prioridad += valor_prioridad
            registros_validos += 1
            
    return (suma_prioridad, registros_validos)
--------------------------------------------------------------------------------
def calcular_promedio_puntuaciones(partidas: list[dict[str,int | str]] | None) -> float:
    if not partidas:
        return 0.0
    
    suma_puntuacion: float = 0.0
    validos: int = 0

    for registro in partidas:
        if not isinstance(registro, dict):
            continue
        
        valor = registro.get('puntuacion')
        if isinstance(valor, (int, float)) and not isinstance(valor, bool):
            suma_puntuacion += valor
            validos += 1
    if validos == 0:
        return 0.0

    return suma_puntuacion / validos

------------------------------------------------------------

def obtener_mayores_de_edad(usuarios: list[dict[str, str | int]] | None) -> list[str]:
    if not usuarios:
        return []

    mayores_de_edad: list[str] = []

    for registro in usuarios:
        if not isinstance(registro, dict):
            continue
            
        nombre = registro.get("nombre")
        edad = registro.get("edad")

        # Validación estricta: nombre es str, edad es int (excluyendo bool), y edad >= 18
        if (
            isinstance(nombre, str)
            and isinstance(edad, int)
            and not isinstance(edad, bool)
            and edad >= 18
        ):
            mayores_de_edad.append(nombre)

    return mayores_de_edad
-----------------------------------------------------------------------------------------

def filtrar_productos_caros(productos: list[dict[str, str | float | int]] | None) -> list[str]:
    if not productos:
        return []

    nombre: list[str] = []

    for registro in productos:
        if not isinstance(registro, dict):
            continue
            
        nombre = registro.get("nombre")
        precio = registro.get("precio")

        # Validación estricta: nombre es str, edad es int (excluyendo bool), y edad >= 18
        if (
            isinstance(nombre, str)
            and isinstance(precio, (int, float))
            and not isinstance(precio, bool)
            and precio >= 50
        ):
            productos_caros.append(nombre)

    return productos_caros
  
def separar_y_unir(cadena: str) -> list[str]:
    limpio = cadena.strip()
    partes = limpio.split(",")
    return partes
----------------------------------------------
# Enfoque A: Forma idiomatica en Python
if not lista:
    print("La lista está vacía")

# Enfoque B: Comprobación por longitud
if len(lista) == 0:
    print("La lista está vacía")
---------------------------------

def es_lista_valida(elementos: list[str]) -> bool:
    if not elementos:
        return False
    else:
        return True

def es_cadena_valida(texto: str) -> bool:
    if not texto:
        return False
    else:
        return True
------------------------------------------------------------------------
# Ejemplo de acumulación básica
numeros: list[int] = [10, 20, 30]
total: int = 0  # Inicialización del acumulador

for num in numeros:
    total += num  # Equivale a: total = total + num

print(total)  # Muestra 60
-----------------------------------------------------------------------------------


def sumar_elementos(elementos: list[int]) -> int:  # 1. Dos puntos obligatorios
    suma: int = 0  # 2. Sangría de 4 espacios
    
    for numero in elementos:  # 3. Nombre en singular para el elemento
        suma += numero  # 4. Usar la MISMA variable acumuladora
        
    return suma  # 5. El return va FUERA del bucle (al nivel de 'suma')

----------------------------------------------------------------------------------------    

def contar_y_sumar(numeros: list[int]) -> int:
    acumulador: int = 0
    for n in numeros:
            acumulador += n   
    return acumulador
    --------------------------------------------------------------------------

def contar_positivos(numeros:list[int]) -> int:
    contador:int = 0
    for n in numeros:
        if n > 0:
            contador += 1
    return contador
-------------------------------------------------------------------------------

def contar_pares(numeros: list[int]) -> int:
    total_pares: int = 0
    for n in numeros:
        if n % 2 == 0:
            total_pares += 1  # Usamos el MISMO nombre de variable declarada
    return total_pares

--------------------------------------------------------------------------------------

def contar_impares(numeros: list[int]) -> int:
    total_impares: int = 0
    for n in numeros:
        if n % 2 != 0:  # O también: if n % 2 == 1:
            total_impares += 1
    return total_impares
---------------------------------------------------------------------------------------
 

def filtrar_palabras_largas(palabras: list[str]) -> list[str]:
    resultado: list[str] = []
    for p in palabras:
        if len(p) > 4:
            resultado.append(p)
    return resultado
----------------------------------------------------------------------------------------
  
def sumar_enteros_defensiva(elementos: list[int | str] | None) -> int:
    if not elementos:
        return 0
    
    suma: int = 0

    for e in elementos:
        if isinstance(e, int) and not isinstance(e, bool):
            suma += e
    return suma
    --------------------------------------------------------------------
 
def convertir_y_sumar_floats(datos: list[str | float | int | None] | None) -> float:
    if not datos:
        return 0.0

    suma_total: float = 0.0

    for item in datos:
        if item is None:
            continue

        if isinstance(item, bool):
            continue

        if isinstance(item, str):
            texto_limpio = item.strip()
            if not texto_limpio:
                continue
            try:
                suma_total += float(texto_limpio)
            except ValueError:
                continue  # Ignora cadenas no numéricas como "hola"

        # 5. Caso int o float numérico directo
        elif isinstance(item, (int, float)):
            suma_total += float(item)

    return suma_total
   ----------------------------------------------------------------------------------   
 """
def contar_frecuencia_palabras(elementos: list[str | None] | None) -> dict[str, int]:
    if not elementos:
        return {}
    
    conteo: dict[str, int] = {}

    for e in elementos:
        if not isinstance(e, str):
            continue

        palabra = e.strip().lower()
        if not palabra:
            continue

        # .get(palabra, 0) devuelve 0 si la clave no existe aún
        conteo[palabra] = conteo.get(palabra, 0) + 1

    return conteo






















