def run(xmin: int, xmax: int) -> list:
    # TODO
    """lista = []
    

    while (xmin<= xmax):
        lista.append(3 * xmin + 2)
        xmin += 1
    return lista
    """"

import sys
list=["a",3,4,5,6,7,8,9,1] #creamos la lista
suma=0 #creamos la variable suma

for i in list[1:]: #hacemos que el for vaya de 1 hasta el final

    suma=i+suma #vamos sumando todos los valores
    
media=suma/len(list[1:]) #hacemos la media dividienod la suma entre la longitud de la lista
print (media) 


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
