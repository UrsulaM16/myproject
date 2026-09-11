import sys

for elemento in sys.arg:
    print(elemento)

suma = sum([int(i) for i in sys.argv[1:]])
longitud = len (sys.argv[1:])

media = f"{suma/ longitud:.2f}"

print(media)