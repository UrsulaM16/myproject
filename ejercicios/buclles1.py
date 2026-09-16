"""#Bucle for. esto  es para que escriba en consola los pares
for i in range(2, 202, 2):
    print(i)


saltos_restantes = 0

for i in range(0, 52):
    if saltos_restantes > 0:
        saltos_restantes -= 1   
        continue
    if i % 3 == 0:
        print(f'{i}  <-- DIVISIBLE POR 3!')
        saltos_restantes = 4
    else:
        print(i)

num1 = ['d', '4', 'f']
num2 = ['7', 'n', 'o']
#coloca el str concatenado entre comillas, zip une las listas. 
resultado = "".join(a + b for a, b in zip(num1, num2))
print(resultado)

num1 = ['d', '4', 'f']
num2 = ['7', 'n', 'o']
#tradicional
resultado = ""
for a, b in zip(num1, num2):
    resultado += a + b
    print(resultado)

caracteres = ['a', 'b', 'c', 'd', 'a', 'e', 'o', 'u', 'i', 'z', 'r', 's']
cadena = ""

for char in caracteres:
    if char == 'z':
        break
    cadena += char
print(cadena)

num_naturales = [2, 0, 1, 5, 6, 7, 4, 3, 8, 9]

for num in range(10):
    if num in num_naturales:
        print(num)

#recuerda que         

import random

# Crear el tablero de 3x3 lleno de espacios vacíos
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Inicializar el jugador actual
jugador_actual = 'X'

# Hay 9 casillas en total, por lo que el juego dura máximo 9 turnos
for turno in range(1, 10):
    print(f"--- Turno {turno}: Juega {jugador_actual} ---")
    
    # Buscar todas las posiciones libres disponibles (fila, columna)
    libres = []
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == ' ':
                libres.append((fila, col))
    
    # Seleccionar una posición libre al azar
    fila_elegida, col_elegida = random.choice(libres)
    
    # Colocar la ficha en el tablero
    tablero[fila_elegida][col_elegida] = jugador_actual
    
    # Mostrar el tablero por pantalla
    for fila in tablero:
        print(f"| {fila[0]} | {fila[1]} | {fila[2]} |")
    print()
    
    # Alternar el turno entre 'X' u 'O'
    if jugador_actual == 'X':
        jugador_actual = 'O'
    else:
        jugador_actual = 'X'

print("¡Juego terminado! El tablero está lleno.")
"""
