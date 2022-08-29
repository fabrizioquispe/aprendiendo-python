"""
Un iterador es un objeto que contiene un número contable de valores.

Un iterador es un objeto sobre el que se puede iterar, lo que significa que puede recorrer todos los valores.

Técnicamente, en Python, un iterador es un objeto que implementa el protocolo del iterador, que consta de los métodos __iter__() y __next__().

Devuelve un iterador de una tupla e imprime cada valor:
"""

productos_arrays = ["Perro","Gato","Leche","Manzana"]
productos_arraysIT = iter(productos_arrays)
print(next(productos_arraysIT))
print(next(productos_arraysIT))
print(next(productos_arraysIT))
print(next(productos_arraysIT))