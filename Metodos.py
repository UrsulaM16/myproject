class alumno:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def __eq__(self, otro_alumno:alumno):
        return self.nombre == otro_alumno.get_nombre() 

    def __str__(self):
        return f'Soy {self.nombre}'



alumno1 = alumno('Manu')
alumno2 = alumno('Roberto')
alumno3 = alumno('Manu')   


if alumno1 == alumno3:
    print(f'{alumno1.get_nombre()} tiene el mismo nombre que {alumno3.get_nombre()}')
else: 
    print(f'{alumno1.get_nombre()} tiene distinto nombre que  {alumno3.get_nombre()}')

elif  alumno1 == alumno2:
    print(f'{alumno1.get_nombre()} tiene el mismo nombre que {alumno2.get_nombre()}')
else:
    print(f'{alumno1.get_nombre()} tiene distinto nombre que {alumno2.get_nombre()}')