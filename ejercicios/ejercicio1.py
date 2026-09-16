#precio = float(input("¿Cual es el precio? "))
#porcentaje_impuesto = float(input("¿Cual es el %  de impuesto?" ))
#impuesto = precio * (porcentaje_impuesto / 100)
#total = precio + impuesto
#print(f"precio: {precio}€")
#print(f"impuesto ({porcentaje_impuesto}%): {impuesto}€")
# print(f"total: {total}€")

num1 = int(input("inserte un numero: "))
num2 = int(input("inserte un numero: "))
num3 = int(input("inserte un numero: "))
if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
else:
    mayor = num3
print (f"el mayor es: {mayor}")
2
