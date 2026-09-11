
class cliente:
    __dni: str
    __nombre:str
    __apellidos:str
    def __ init __(self, dni:str, nombre:str, apellidos:str):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def nombre_getter(self):
        return(f'{self.__nombre}, {self.__apellidos}')

    def get_dni(self):
        return self.__dni

class Movimiento:
    __concepto:str
    __cantidad:float
    def __init__(self, concepto:str, cantidad:):
        self.__concepto = concepto
        self.__cantidad = cantidad

class Cuenta:
    __numero: int
    __titular: cliente
    __movimientos:list[Movimiento]
    def __init__(self, titular: cliente):
        self.__titular = titular
        self.__numero = int("".join([str(random.randint(0, 9)) for _ in range(longitud)]))
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def set_movimiento(self, movimiento):
        self.__movimientos.append(movimiento)

        
#Creacion de clientes

Clientes: list[Cliente][]

clientes.append(Cliente(dni='12345678A', nombre='Pedro', apellidos='García López'))
clientes.append(Cliente(dni='87654321B', nombre='Henry William', apellidos='Cavill Serrano'))
clientes.append(Cliente(dni='12345678C', nombre='María Del Valle', apellidos='Perez Martínez'))


for cliente in clientes:
    print(cliente.get_nombre(), ' DNI:', cliente.get_dni())

#Creacion de cuentas
cuentaPepe = Cuenta(titular=clientes[0])
print(f'El saldo de {cuentaPepe.get_titular().get_nombre()} es de {cuentaPepe.get_saldo()}')
print(f'El saldo de {cuentaPed}')


