# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
# 	if valor%2==0:

num = int(input("Ingrese números: "))
pares = 0
impares = 0
for i in range(num):
    num = int(input(f"Ingrese el numero {i + 1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Total de pares: {pares}")  # Muestra: Total de pares: 2
print(f"Total de impares: {impares}")


# cant_par = 0
# cant_impar = 0
# while True:
#    n_numeros = input('Ingresa cantidad de números a contar [MAX:10 - MIN:2]: ')
#    if n_numeros.isdigit():
#        n_numeros = int(n_numeros)
#        if 2 <= n_numeros <= 10:
#            break

#    print('Error: Ingrese un número dentro del rango indicado [MAX:10 - MIN:2]\n')


# for i in range(n_numeros):
#    numero = int(input(f'Ingrese el número {i + 1}: '))
#    if numero % 2 == 0:
#        cant_par += 1
#    else:
#        cant_impar += 1

# print(f'\nNúmeros Pares: {cant_par} - Números Impares: {cant_impar}')
