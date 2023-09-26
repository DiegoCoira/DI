import random
# Lista cos numeros 1,2,3
numeros = list(range(1,4))

print("Bienvenido jugador!")
nombre = input("Como te llamas?:")
print("Este juego de adivinanza constara de 3 adivinanzas y se te dara una puntuacion de 0-3.")
juega = input("Quieres jugar a las adivinanzas jugador/jugadora " + nombre + "?(si/no)")

# Un if para saber si el jugador a elegido jugar o no
if juega == "si" or juega == "sí" or juega == "Si" or juega == "Sí":

    # Collo dous valores aleatorios da lista de 3 numeros
    muestra = random.sample(numeros, 2)
    
    # Inicializo o resultado
    resultado = 0

    # Si muestra conten o valor 1 en calquera das duas posicións, este entrara na primeira adivinanza
    if muestra[0] == 1 or muestra[1] == 1:
        print("Adivinanza: Que es verde por fuera, pero rojo por dentro?")
        print("A: Carlos.")
        print("B: Sandia (Esta es la correcta).")
        print("C: Melon (Es lo que eres si eligues la opción A o C.)")
        # Almaceno o input en respuesta
        respuesta = input("Eligue la opcion correcta.").lower()
        # Comprobo a resposta do usuario
        if respuesta == "a":
            print("Incorrecto. Creo que ya se lo que eres.")
        elif respuesta == "b":
            print("Correcto, era facil verdad?!")
            resultado = resultado + 1
        elif respuesta == "c":
            print("Incorrecto. Has leido las respuesta?")
        else:
            print("Si das un valor diferente a A,B o C. Obviamente no esperes un buen resultado.")

    # Si muestra conten o valor 2 en calquera das duas posicións, este entrara na segunda adivinanza
    if muestra[0] == 2 or muestra[1] == 2:
        print("Adivinanza:En la noche vuela sin ser ave, en el día descansa en su enclave. Siempre presente en todo rincón, silencioso, invisible, sin distorsión.  ")
        print("A: Soy el Sueño.")
        print("B: La brisa.")
        print("C: Un suspiro.")
        # Almaceno o input en respuesta
        respuesta = input("Eligue la opcion correcta.").lower()
        # Comprobo a resposta do usuario
        if respuesta == "a":
            print("Correcto. Este era mas dificil verdad jijijijijiji ;).")
            resultado = resultado + 1
        elif respuesta == "b":
            print("Incorrecto jijijijijiji.")
        elif respuesta == "c":
            print("Incorrecto jijijijijiji")
        else:
            print("Has dado un valor no valido, asique incorrecto jijijijijiji.")

    # Si muestra conten o valor 3 en calquera das duas posicións, este entrara na terceira adivinanza
    if muestra[0] == 3 or muestra[1] == 3: 
        print("Adivinanza:En el universo, soy infinito, sin forma, sin masa, sin ruido.Ni comienzo, ni fin, ni existencia,un enigma más allá de la conciencia. ¿Qué soy?")
        print("A: La oscuridad.")
        print("B: La nada o vacío.")
        print("C: El infinito.")
        # Almaceno o input en respuesta
        respuesta = input("Eligue la opcion correcta.").lower()
        # Comprobo a resposta do usuario
        if respuesta == "a":
            print("Incorrecto jijijijijiji.")
        elif respuesta == "b":
            print("Correcto :(.")
            resultado = resultado + 1
        elif respuesta == "c":
            print("Incorrecto jijijijijiji")
        else:
            print("Has dado un valor no valido, asique incorrecto jijijijijiji.")

    # Controla cantas adivinanzas fallastes e da unha respuesta dependendo do resultado
    if resultado == 0:
        print("Oh has fallado todas las adivinanzas " + nombre + " :(.")
    elif resultado == 1 :
        print("Solo has acertado una. Toma esto como regalo")
        print("*Has recibido un nuevo tema de escritura*")
    elif resultado == 2:
        print("Enhorabuena, as acertado 2/2. Toma este regalo")
        print("*Has recibido un aspecto mítico de personaje")
        print("*Has recibido un aspecto legendario de arma*")
    else:
        print("Como llegaste aqui, no se vale utilizar exploits :(. Toma esto.")
        print("*Has recibido un baneo*")
    
# Elif para comprobar si o xogador quere seguir xogando
elif juega == "no" or juega == "No":
    print("Tu te lo pierdes " + nombre)
else:
    print("No has escrito ni si ni no, asique no podras jugar :). Lo siento " + nombre)