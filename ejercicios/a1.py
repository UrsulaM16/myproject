"""def es_par(numero: int) -> str:
    if numero % 2 == 0:
        return 'es numero par'
    else:
        return 'numero impar'

print(es_par(5))

def f(num: int) -> str:
    if num == 1:
        return 'hace 1 minuto'
    else:
        return f'hace {num} minutos'
print(f(5))

nombre = input('ingrese nombre: ').upper()
sexo = input('indique si es H/M: ').upper()

def grupo(nombre:str, sexo: str) -> str:
   
    if (nombre[0] < 'M' and sexo == 'M') or (nombre[0] > 'N' and sexo == 'H'):
         return 'Grupo A'
    else: 
         return 'Grupo B'
print(grupo(nombre, sexo))

nombre = input('Nombre : ')
def saludo(nombre: str) -> str:
     return f'Hola, {nombre}!'
print(saludo(nombre))

def suma_lista(numeros: list[int]) -> int:
    return sum(numeros)
print(suma_lista([1, 2, 3, 5, 8, 9]))

palabra = input('Indique : ').lower()
def p_isograma(palabra: str) -> bool:
    for caracter in palabra:
        if palabra.find(caracter) != palabra.rfind(caracter):
            return False
        else:
            return True
print(p_isograma(palabra))
"""

