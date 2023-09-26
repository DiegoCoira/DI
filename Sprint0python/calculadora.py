from operaciones import suma, division, multiplicacion, resta

print("Bienvenido a calculadora.py")
# Inicializo seguir = "s" para que poida entrar no while
seguir = "s"
nombre = input("Cual es tu nombre:")
while seguir == "s":
    # Pidolle os numeros que queira utilizar
    print("Para poder continuar, necesito que me des dos numeros para hacer las operaciones.")
    a = input("El primer número:")
    b = input("El segundo número:")
    # Gardo a operacion que queira facer
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

    # Dou o resultado da operacion
    print("El resultado es " + str(resultado))
    # Preguntolle ao usuario se quere seguir utilizando a calculadora
    seguir = input("Quieres seguir jugando " + nombre + "?(s/n)")
    # Comprobo a resposta, se quere seguir xogando volvera o principio
    while seguir != "n" and seguir != "s":
        # Entrara en este while si o usuario pon algo que non sexa n ou s, e estara aqui hasta que o poña
        print("Mal input, vuelve a elegir s o n")
        seguir = input("Quieres seguir jugando " + nombre + "?(s/n)")

