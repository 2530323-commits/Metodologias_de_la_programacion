cars = ['audi', 'bmw', 'chevrolet', 'byd', 'tesla']
for car in cars:
    if car == "bmw" or car == "tesla" or car == "audi":
        print(car.upper())
    else:
        print(car)
print ("\n condicional")
#Condicionales : El condicional es el corazon de un if
#Condicional True
car = 'bmw'
print(car == 'bmw')

car_2 = 'Audi'
print(car_2== 'audi')
#condicional false
car_2 = "Audi"
print(car_2.lower()== 'audi') #Salida -> True
 #Condicional ! = para determinar desigualdad
requested_topping = "mushrooms"
if requested_topping != 'anchovies': # -> True
    print("Hold the anchovies")
#comparaciones numericas
age = 18 # -> int
print(age==18)# -> True

answer = 17
if answer !=42:
    print("Esa no es la respuesta correcta. Intenta otra vez")

age = 19
print(age<21) #true
print(age<=21) #true
print(age>21)# false
print(age>=21) #false


#Multiple
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >=21)
print(age_0 >= 21 and age_1 >=18)


age_0 = 22
age_1 = 18
print( "Multiples condiciones")
print("operacione and - pseint(Y)")
print(age_0 >= 21 or age_1 >=21) #True
print(age_0 >= 21 or age_1 >=21) #False

#¿Como nos preguntamos si algun valor esta en una lista?

print("\n A value is in a list")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) #True
print('pepperoni' in requested_toppings) #False

#A value not in a list

banned_users = ["gabriel", "max", "andrik", "quevedo","christofer","angel"]
user = "pedro"
print(user not in banned_users) #True

#Variables de tipo BOOLEANOS
game_active = True
can_edit = False    

"""
    if statement

    if condition
        do something
    if condition
        do something else (true)  
    else:
        do something (false)
"""

#Preguntas la edad de usuario
# y decirle si tiene la edad suficiente para votar
#input("") -> str

age = int(input("\nEscribe tu edad :"))
print(f"\ntu edad es: {age}")

if (age) >= 18:
    print("Tu tienes la edad para votar")  
else:
    print("Tu no tienes la edad para votar")

