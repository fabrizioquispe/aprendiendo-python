#Creamos un array o lista y mostramos por consola
myArray = ["Fabrizio","Quispe","20","Senati","San Juan de Miraflores"]
print(myArray)

#Mostramos la columna del array
print(myArray[3])

#La Propiedad Length o len() se utiliza para hace el contado de nuestro array o lista
print(len(myArray))

#Cambiamos un item de la lista
myArray[2] = "19"
print(myArray)

#Agregar items a la lista con la funcion insert()
myArray.insert(2, "30")
print(myArray)

#Concatenar Listas 
array1 = ["Numero1","Numero2","Numero3"]
array2 = ["Numero4","Numero5","Numero6"]
arrayResult = (array1 + array2)
print(arrayResult)