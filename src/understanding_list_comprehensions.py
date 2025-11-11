"""
squares = []
for value in range90,11) :
    square = value ** 2
    squares.append(square)  
print(squares)
"""
"""
Una list comprehention combina el ciclo for
y la creacion de nuevos elementos en una sola linea
y automaticamente agrega los nuevos elementos a la lista
es decir, sin utilizar el metodo append.
"""
squares = [value ** 2 for value in range(0,11)]
print(squares)

#Para los numeros pares del 0 al 100

evens_range = [value ** 2 for value in range(0,101,2)]

evens_if = [value for value in range(0,101) if value % 2 == 1]
print(evens_if)