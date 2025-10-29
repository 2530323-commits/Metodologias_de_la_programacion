"""
String variables


Un string es de manera sencilla una serie de caracteres.
En python , todo lo que se encuentre dentro de comillas simples (´´) o dobles(" ") sera considerado
un string.

Ejemplos:
"Esto es un string"
´esto tambien es un string´

`Le dije a un amigo "Python es mi lenguaje favorito"
"El lenguaje ´Python´ lleva el nombre por Monty Python, NO por la serpiente"

"""
name= "clase de programacion"
print (name)

#title
print(name.title())

print (name)


"""
Un metodo es una accion que python puede realizar en un
fragmento de datos o sobre una variable.

    El punto . despues de una variable
    seguido del metodo title() dice que se tiene que ejecutar el metodo title de la variable name.

    Todos los metodos van seguidos de parentesis
    porque en ocasiones necesitan informacion adicional
    para funcionar, la cual iria dentro de los parentesis.

    En esta ocasion, el metodo .title() no requiere informacion adicional para funcionar
"""

print("metodo upper:",name.upper())
print ("Metodo lower:", name.lower())

#Concatenion de Strings

first_name= "santiago"
last_name="chavez"
full_name = first_name +" "+ last_name
print(full_name)
print(full_name.title())