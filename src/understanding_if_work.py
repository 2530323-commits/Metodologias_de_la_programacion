
try:
    age = int(input("\nEscribe tu edad :"))

except:
    age = -1
    print("Error, ingresaste un caracter no valido")

if age <= 4 and age >=0:
    print("La entrada es gratuita")
elif age < 18 and age >4:
    print("La entrada cuesta $200")
elif age >= 18:
    print("La entrada cuesta $400")    
else:
    print("Error, edad no valida")

guisos_disponibles = ["salsa verde, deshebrada, mole"]
guisos_a_ordenar= ["deshebrada", "caldo de iguana"]

print("que guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    print(f"deseo {guiso}")
    if guiso in guisos_disponibles:
        print(f"si tenemos{guiso}")
    else:
        print("No tenemos de ese guiso")
        
print("Error, edad no valida")