while True:
    try:
        number = int(input ("Ingrese un numero entre 10 y 20:"))
        if 10 <= number <= 20:
            print ("Numero dentro del rango , Felicitaciones!")
            break
        else:
            print("Numero fuera del rango, intentalo de nuevo.")
    except ValueError:
        print("Entrada invalida, por favor ingrese un numero entero.")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break
print("Saliste del while yupi")

