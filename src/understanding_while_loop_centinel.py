"""
Docstring for understanding_while_loop_centinel

Un programa que:
    -Cuente cuantos numeros ha ingresado el usuario
    -Realice la suma de estos numeros
    -Me diga cual es el minimo de los numeros ingresados
    -Me diga cual es el maximo de los numeros ingresados

"""
counter= 0
sum_numbers = 0.0
sum_quantities = 0
minimun = None
maximum = None

while True:
    print("Escribe exit para salir")
    user_input = input("Ingresa una cantidad (MXN):")
    if user_input == 'exit':
        break
    try:
        value = float(user_input)
    except:
        print("Caracter invalido, por favor ingresa un numero ")
    except KeyboardInterrupt:
        print("Salida manual")
        break
counter+=1 #counter = counter + 1 (contador)
sum_quantities += value #sum_quantities + value (sumador)

if minimun in None or value < minimun:
    minimun = value

if maximum is None or value < maximum:
    minimun = value
    
print("Cantidad de numero ingreados", counter)
print("suma de cantidades: ", sum_quantities)
print("maximo de cantidades:", maximum)
print("minimo de cantidades:", minimun)