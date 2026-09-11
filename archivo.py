
noches = int(input("Ingrese cuantos días de estadia desea: "))
precio_noche = float(input("Ingrese el precio por noche: "))

total = 0
noche = 1
#
while noche <= noches:  
    if noche == 1:     
        # Primera noche: precio completo
        total += precio_noche
    else:
        # Resto: 10% descuento
        total += precio_noche * 0.9
    
    noche += 1

print(int(round(total)))