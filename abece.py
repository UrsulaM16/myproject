#Introducir una frase por teclado y 
# contar el número de veces que aparece cada vocal en la misma. 

frase = input("Ingrese nombre: ").lower()

a = 0
e = 0
i = 0
o = 0
u = 0

posicion = 0
while posicion < len(frase):
    letra = frase[posicion]
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1
    posicion += 1  

print('Conteo de vocales: ')
print('a: ', a)
print('e: ', e)
print('i: ', i)
print('o: ', o)
print('u: ', u)