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

#Whitespaces

"""
Un Whitespace se refiere a cualquier caracter que no se imprime, es de cir , un espacio, tabuladore y finales de linea. 
Los whitespaces se utilizan comunmente para organicar las salidas
de tal manera 
que sea mas amigable leer o ver para el usuario.

Ejemplos:
-Tabulador: \t
-Salto de linea: \n
 """

print("Whitespace Tabulador")
print("python")
print("\tpython") 
print("\t\tpython")

print("Languages: \n\tPython\nC\n\tJavaScript")

#Eliminacion de espacios en blaco

programming_languages = "python"
print(programming_languages)
print(programming_languages.rstrip())
print(programming_languages.lstrip())
print(programming_languages.strip())

#Syntax Error con String
message = 'una fortaleza de "python" es su comunidad'
print (message)

# f-strings
famous_person= "Taylor Swift"
message = f"{famous_person} una vez dijo me voy al Oxxo en avion."
print(message)  
print(f"{famous_person.upper()} una vez dijo me voy al Oxxo en avion.")

#actividad
"""
Elige el nombre de una persona (quien tu quieras)
Elige una cita famosa de esta persona.
Iguala ambos strings a una variable.
1)Realiza la concatenacion utilizando el signo de suma 
2)Realiza la concatenacion utilizando fstrings

"""
quote= "Y yo soy Iron Man"
famous_person= "Iron Man"
famous_message = famous_person+ " "+quote
print(famous_person+ " "+quote)

print(famous_message)

f_print_message = f"{famous_person} {quote}"
print (f_print_message)