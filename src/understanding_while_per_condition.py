"""
    Vamos a realizar un programa que defina un PIN 
    para dar acceso a un usuario.

    El usuario va a tener maximo de intentos para 
    colocar bien el pin

    Si usuario sobrepasa este maximo de intentos
    se le va a bloquear la cuenta y el acceso.

"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0

while attempt < MAX_ATTEMPTS:
    
    user_input = input ("ingresa tu PIN: ")

    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break
    else:
        attempt+=1
        reamining_attemps= MAX_ATTEMPTS -attempt
        if reamining_attemps > 0:
            print("Ingresa un pin no valido")
            print(f"Te quedan {reamining_attemps} intentos")
        else:
            print("cuenta bloqueada.")





















