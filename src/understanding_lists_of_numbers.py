"""
 Las listas tambien pueden almacenar
 numero y de hecho, son ideales para esto.
 Python ofrece una gran cantidad de
 herramientas que ayudan a trabajar 
 eficientemente listas de numeros
"""
#Metodo built-in range()

"""
El metodo range() nos ayuda a crear facilmente
 series de numeros:

    Ejemplo:

"""
print("Numeros del 0 al 9:")


for value in range(10): # 10 numeros, del 0-9
    print(value)

print("Numeros del 1 al 9:")

for value in range(1,10): # 10 numeros, del 1-9
    print(value)

print("numeros impares del 1 al 9")
for value in range(1,10,2): # 10 numeros, del 1-9
    print(value)
odd_numbers=list(range(1,10,2))
print(odd_numbers)




print("numeros pares del 1 al 9")
for value in range(0,10,2): # 10 numeros, del 1-9
    print(value)    
even_numbers=list(range(0,10,2))
print(even_numbers)


print("tabla del 9")
for value in range(2,10,2): # 10 numeros, del 1-9
    print(value)
tabla_del_9=list(range(9,91,9))
print(tabla_del_9)


#Cuadrados de los primeros 10 numeros
squares = []
for number in range(1,11):
    square=number**2
    squares.append(square)  
print(squares)

##Mas metodos built-in
# metodo min ()
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits)) #salida: 9

#Metodo sum()
digits = [1,2,3,4,5,6,7,8,9,0]
print(sum(digits)) #salida: 9