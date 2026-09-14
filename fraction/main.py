'''from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.__num = num
        sef.__den = den

    def __str__(self):
        print(f'{self.__num} / {self.__den}')
     #   print(f'{self.num // self.gcd} / {self.den // self.gcd}')

    def gcd(self, a: int, b: int):
        """Algoritmo de Euclides para cálculo del Máximo Común Divisor"""
        a = self.__num
        b= self.__den

        while b > 0:
            a, b = b, a % b
        return a

    def get__fraccion():
        return self.__num, self.__den
    
    def simplify(self):
        gcd = self.gcd()
        self.__num //= gcd
        self.__den //= gcd

        #print(f'{self.__num // self.gcd} / {self.den // self.__gcd}')


    def __add__(self, otra_fraccion: Fraction):
        fraccion = otra_fraction.get._fraccion()
        self.__num = self.__num * fraccion [1] + fraccion[0] + self.__den
        self.__den = self.__den * fraccion[1]
        self.simplify


f1 = Fraction(25,30)
f2 = Fraction(40,25) 

f1 + f2
return f1
print(f1)
'''



from __future__ import annotations

class Fraction:
    def __init__(self,num:int , den:int):
        self.__num = num
        self.__den= den

    def get_fraccion(self):
        return self.__num, self.__den   

    def __str__(self) :
        return (f"{self.__num} / {self.__den} ")

    def gcd(self) :
        a= self.__num
        b = self.__den

        while b > 0 :
            a, b = b , a % b
        return  a

    def simplify(self) :
        gcd= self.gcd()
        self.__num  //= gcd 

hola = Fraction(25,30)
adios  = Fraction(40,45)   

hola+adios
print(hola) 

        

