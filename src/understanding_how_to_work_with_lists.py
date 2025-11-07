#Trabajando con listas
"""
Recorrer una lista sin importar la cantidad
 de elementos que tenga
"""



magicians = ["ron", "hermione", "harry", "hagrid", "cedrik" ]

for magician in magicians:
    print(magician)
    print(magician.upper())
    print("\n")
    print(f"{magician.title()} ese fue un gran hechizo.")
    print (f"\t{magician.lower()} No podemos esperar para ver tu siguiente hechizo:")

print("gracias a todos, fue un gran espectaculo")

"""
Identacion:

Python utiliza la identacion para determinar 
cuando una linea de codigo esta conectada a
la linea de codigo anterior.

Basicamente, se utilizan 4 espacios en blanco
para obligarnos a escribir codigo ordenado y
estructurado.
"""
#No olvidemos identar
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
    print("I can't wait to see the next trick!{magician.title()}")

#Identacion innecesaria
message = "hola Python"
print(message)

