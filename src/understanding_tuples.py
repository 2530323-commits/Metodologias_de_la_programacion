#Tuples
"""
Las tuplas son listas de elementos que no
cambian de tamaño. Las tuplas son INMUTABLES.

Se utilizan los () para definir una tupla.

"""

rectangle_measurements= (200, 50) # largo , ancho
print(rectangle_measurements[0])
print(rectangle_measurements[1])

for measure in rectangle_measurements:
    print(measure)

print(dir(rectangle_measurements)) #built-in dir


rectangle_measurements = (200, 50) # (lageo, ancho)

#rectangle_measurements[0]=300 #No se puede
#rectangle_measurements[1]=100 #No se puede
rectangle_measurements=(300,100)

"""
No podemos modificar una tupla directamente
lo que si podemos hacer es cambiar la asignacion 
a una variable que almacena una tupla.
"""

