"""
La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.

La clase principal es la clase de la que se hereda, también llamada clase base.

La clase secundaria es la clase que hereda de otra clase, también llamada clase derivada.
"""

class Persona:
    def __init__(self,nombre ,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def printname(self):
        print(self.nombre,self.apellido)

x = Persona("Fabrizio", "Quispe")
x.printname()