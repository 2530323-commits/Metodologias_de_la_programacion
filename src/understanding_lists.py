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

print("\n--- Agregar elementos a una lista metodo append() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida, ['honda', 'yamaha', 'suzuki']
motorcycles.append ('Duccati')
print(motorcycles) #Salida:'honda', 'yamaha', 'suzuki', 'Duccati]

"""
Agregar elementos a una lista  en una posicion especifica
- insert(): Inserta un elemento en una posicion especifica
"""
print("\n--- Agregar elementos a una lista metodo insert()---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)#Salida, ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) #Salida: ['ducati', 'honda', 'yamaha', 'suzuki']

"""
Eliminar elementos de una lista
- del: Elimina un elemento de una posicion especifica
""" 
print("\n--- Eliminar elementos de una lista metodo del ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida, ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) #Salida: ['yamaha', 'suzuki']
"""
Eliminar elementos de una lista
- pop(): Elimina el ultimo elemento de la lista y lo devuelve           
"""
print("\n--- Eliminar elementos de una lista metodo pop() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']       
print(motorcycles) #Salida, ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) #Salida: ['honda', 'yamaha']
print(popped_motorcycle) #Salida: suzuki
"""
Eliminar elementos de una lista por valor
- remove(): Elimina un elemento por su valor            
"""             
print("\n--- Eliminar elementos de una lista metodo remove() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) #Salida, ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('yamaha')    
print(motorcycles) #Salida: ['honda', 'suzuki', 'ducati']

#Usando el valor eliminado
print("\n--- Usando el valor eliminado con remove() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) #Salida, ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
print(f"\nA {too_expensive.title()} is too expensive for me.")
"""

Ordenar una lista permanentemente
- sort(): Ordena una lista de forma permanente en orden alfabetico  
"""
print("\n--- Ordenar una lista permanentemente con sort() ---")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #Salida, ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #Salida: ['audi', 'bmw', 'subaru', 'toyota']

