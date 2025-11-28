### FUNCIONES
# Las funciones son bloques de codigo para realizar
#una tarea en especifico

#Cuando queremos realizar la tarea que se ha definido
#En la funcion, tenemos que llamar el nombre de la 
#funcion que realizar la accion.

"""
    Sintaxis de una funcoin
    def nombre_funcion():
        acciones

    Ejemplo: vamos a definir una funcoin que de un saludo a christopher
"""

def greetting_christopher():
    """
        Funcion para saludar a una persona
        llamada Christopher
    """
    for i in range(0,5):
     print("Hello Christopher")
    
greetting_christopher()

#Ejemplo de una funcion que genere el nombre completo 
# de una persona y que lo regrese 

def create_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name.strip()}{middle_name.strip()} {last_name.strip()}".title()
    return full_name
first_name = input("dame tu primer nombre: ")
middle_name = input("dame tu segundo nombre: (Si no tiene segundo ombre, da enter) ")
last_name = input ("dame tu apellido: ")

generated_fullname = create_full_name(
    first_name.strip().lower(),
    last_name.strip().lower())
print(generated_fullname)


generated_fullname_2(
    middle_name = user_middle_name,
    first_name = user_first_name,
    last_name = user_last_name
)
print(generated_fullname_2)    