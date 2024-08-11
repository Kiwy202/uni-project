class ClasePrueba():
    atributo_clase=1
    def metodo_objeto(self):
        self.atributo_objeto=2

print(type(ClasePrueba))
print(type(int))

variable_objeto=ClasePrueba()
print(type(variable_objeto))
variable_objeto.metodo_objeto()
print(variable_objeto.atributo_objeto)

print(ClasePrueba.atributo_clase)


import math

class punto():

    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx*dx + dy*dy))

if __name__== '__main__':
    punto1=punto()
    print(punto1.x)
    print(punto1.y)
    punto2=punto(4,5)
    print(punto1.distancia(punto2))
    print(punto2.x)
    print(punto2.y)

    punto1.x=10
    print(punto1.x)
    print(punto1.distancia(punto2))


class Alumno():
    contador=0
    def __init__(self, nombre=""):
        self.nombre=nombre
        Alumno.contador+=1

a1=Alumno("pepe")
print(a1.nombre)
print(Alumno.contador)

a2=Alumno("juan")
print(a2.nombre)
print(Alumno.contador)

class Alumno():
    contador=0
    def __init__(self,nombre=""):
        self.nombre=nombre
        self.__secreto="asasa"
        Alumno.contador+=1

a1=Alumno("ricardo")
print(a1.nombre)
#print(a1.__secreto)

print(a1._Alumno__secreto)

class Calculadora():
    def __init__(self,nombre2):
        self.nombre=nombre2
    def modelo(self):
        return self.nombre
    
    @staticmethod
    def sumar(x,y):
        return x+y
    
c1=Calculadora("basica")

print(c1.nombre)

print(Calculadora.sumar(5,6))

c1=Calculadora("basica")
print(c1.nombre)

print(getattr(c1, "nombre"))

setattr(c1, "nombre", "compleja")

print(getattr(c1,"nombre"))

hasattr(c1,"nombre")

print(getattr(c1,"nombre"))
