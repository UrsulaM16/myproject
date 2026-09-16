nombre = input("Nombre: ")
genero = input("Género (M/H): ")
nombre_lower = nombre.lower()
genero_upper = genero.upper()

if (genero_upper == 'M' and nombre_lower < 'm') or (genero_upper == 'H' and nombre_lower > 'n'):
    grupo = 'A'
else:
    grupo = 'B'
print(f"{nombre} pertenece al Grupo {grupo}")