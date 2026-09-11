def run(fullname: str) -> str:

    partes = fullname.split(',')
    apellido = partes[0].strip()
    nombre = partes[1].strip()

    nombre_inicial = nombre.split()[0][0].upper() + '.'
    apellido_iniciales = ''  

    for parte in palabras_apellido[:2]:
        apellido_iniciales += parte[0].upper() + '.'

    initials = nombre_inicial + apellido_iniciales
    return initials

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

nombres = [
    'Cervantes, Ursula de la Cruz',
    'Chavez, Hugo',
    'Trump, Donald',
    'Melano, Rosa',
    'De Lucía, Paco',
    'García Márquez, Gabriel',
    'Bolivar, Simón',
    'Canvill, Henry',
    'Sanz Pizarro, Alejandro',
    'Banderas Domínguez, Antonio'
]

for n in nombres:
    print(f"{n} -> {run(n)}")

    """
    nombre_completo = []
    nombre = fullname.split(',')[1].strip()
    apellido = fullname.split(',')[0].split()
    nombre_completo.append(nombre
    for apellido in apellidos:
        nombre_completo.append(apellido)
    iniciales = [cadena[0] for cadena in nombre_completo]
    initials = '.'.join(iniciales).upper() + '.'
    return initials
            """