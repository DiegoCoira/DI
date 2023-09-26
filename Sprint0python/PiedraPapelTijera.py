import random
# Gardo as posibilidades nunha lista
posibilidades = ["piedra", "papel", "tijera"]

print("Bienvenid@ al juego de piedra papel tijera :)")
nombre = input("Cual es tu nombre:")
# Inicializo jugadas e partidasGanadas
jugadas = 0
partidasGanadas = 0

while jugadas < 5:
    # Pidolle o xogador que escriba a sua xogada
    JugadaJugador = input("Elige tu jugada(piedra, papel o tijera): ")
    # Comprobo se o xogador eliguei a sua xogada e senon entrara nun while infinito hasta que responda
    while JugadaJugador != "piedra" and JugadaJugador != "papel" and JugadaJugador != "tijera":
        print("Porfavor eligue bien.")
        JugadaJugador = input("Elige tu jugada(piedra, papel o tijera): ")

    # Eligo a xogada da maquina con un random.choice
    JugadaMaquina = random.choice(posibilidades)
    # Comprobo todas as posibilidades e sinon é un empate sumolle 1 a jugadas e se gana sumolle a partidasGanadas
    if JugadaMaquina == JugadaJugador:
        print("- Empate, no se cuenta la jugada")

    elif JugadaMaquina == "piedra" and JugadaJugador == "tijera":
        print("- Has perdido, piedra gana a tijera")
        jugadas = jugadas + 1

    elif JugadaMaquina == "piedra" and JugadaJugador == "papel":
        print("- Has ganado, papel gana a piedra")
        jugadas = jugadas + 1

        partidasGanadas = partidasGanadas + 1
    elif JugadaMaquina == "tijera" and JugadaJugador == "piedra":
        print("- Has ganado, piedra gana a tijera")
        jugadas = jugadas + 1
        partidasGanadas = partidasGanadas + 1

    elif JugadaMaquina == "tijera" and JugadaJugador == "papel":
        print("- Has perdido, tijera gana a papel")
        jugadas = jugadas + 1
    
    elif JugadaMaquina == "papel" and JugadaJugador == "piedra":
        print("- Has perdido, papel gana a piedra")
        jugadas = jugadas + 1

    elif JugadaMaquina == "papel" and JugadaJugador == "tijera":
        print("- Has ganado, tijera gana a papel")
        jugadas = jugadas + 1
        partidasGanadas = partidasGanadas + 1

print("El juego ha acabado.")
# Comprobo que si as partidas ganadas son 3 ou mais dou unha respuesta e se son menos dou outra
if partidasGanadas >= 3:
    print("Enhorabuena "+ nombre + ", has ganado. En total ganaste " + str(partidasGanadas) + " rondas de 5")
else:
    print("Lo siento " + nombre + ", has perdido. En total ganaste " + str(partidasGanadas) + " rondas de 5")