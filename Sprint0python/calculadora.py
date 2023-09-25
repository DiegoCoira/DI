from operaciones import suma, division, multiplicacion, resta

print("Bienvenido a calculadora.py")
seguir = "s"
nombre = input("Cual es tu nombre:")
while seguir == "s":
    print("Para poder continuar, necesito que me des dos numeros para hacer las operaciones.")
    a = input("El primer número:")
    b = input("El segundo número:")
    operacion = input("Que operación deseas realizar?(suma, resta, division, multiplicacion):")
    if operacion == "suma":
        resultado = suma(a,b)
    elif operacion == "resta":
        resultado = resta(a,b)
    elif operacion == "division":
        resultado = division(a,b)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(a,b)

    else:
        print("La operacion que quieres realizar no esta disponible.")
    
    print("El resultado es " + str(resultado))
    seguir = input("Quieres seguir jugando " + nombre + "?(s/n)")
    while seguir != "n" and seguir != "s":
        print("Mal input, vuelve a elegir s o n")
        seguir = input("Quieres seguir jugando " + nombre + "?(s/n)")

