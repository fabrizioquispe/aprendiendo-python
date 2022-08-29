"""
Los ejemplos anteriores son clases y objetos en su forma más simple y no son realmente útiles en aplicaciones de la vida real.

Para comprender el significado de las clases, debemos comprender la función __init__() incorporada.

Todas las clases tienen una función llamada __init__(), que siempre se ejecuta cuando se inicia la clase.

Use la función __init__() para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias cuando se crea el objeto:
"""

class Persona:
 def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

p1 = Persona("Fabrizio" , 20)
print(p1.nombre)
print(p1.edad)

#Funcion init concatenado con otra funcion
class Persona2:
    def __init__(self,nombre2,edad2):
        self.nombre2 = nombre2
        self.edad2 = edad2
    def Mensaje(self):
        print('Mi nombre es: '  + self.nombre2 + ' y mi edad es:'  + self.edad2 )

p1 = Persona2("Juan" , "36")
p1.Mensaje()