#lists
 
"""
Las listas nos permiten almacenar informacion
 en un lugar, la cantidad que tenga: ya sean
 poco elementos o millones de elementos.

Se recomienda nombrar una variable del tipo lista en plural.

En python los corchetes [] definen una lista
sus elemento van separados por comas.

Ejemplo:
"""
bicycles=['trek', 'canodale','redline', 'specialized', 'giant']
print(bicycles)
print(bicycles[0].title())

#Los indices comienzan en 0 y terminan en n-1
print(bicycles[4].title())

#accediendo al ultimo elemento
print(bicycles[-1].title()) #ultimo elemento
print(bicycles[-2].title())
print(bicycles[-5].title()) #primer elemento

#Utilizando valores de lista

message="mi primer bicicleta fue una " + bicycles[4].upper() + "."
print(message)

message_f = f"mi primer bicicleta fue una {bicycles[4].title()}."
print(message_f)

##Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("Metodo de la listas para agregar elementos:list_name.append(element)")
bicycles.append("Duccati")
print(bicycles)