
palabra = input("Inserte una palabra: ")


texto_limpio = ""
for char in palabra.lower():
    if char != " ":
        texto_limpio += char

# 3. Comprobamos y mostramos el mensaje por pantalla
if texto_limpio == texto_limpio[::-1]:
    print("La palabra es un palíndromo")
else:
    print("No es un palíndromo")
