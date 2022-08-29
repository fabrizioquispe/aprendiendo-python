"""
Un bucle for se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, 
un conjunto o una cadena).
Esto se parece menos a la palabra clave for en otros lenguajes de programación 
y funciona más como un método iterador
como se encuentra en otros lenguajes de programación orientados a objetos.
Con el bucle for podemos ejecutar un conjunto de sentencias, una vez por cada 
elemento de una lista, tupla, conjunto, etc.

"""

frutas = ["Manzana" , "Pera" ,"Freza"]

for x in frutas:
    print(x)
    if x == "Manzana":
        break