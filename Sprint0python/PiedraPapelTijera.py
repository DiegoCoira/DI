import random
posibilidades = ["piedra", "papel", "tijera"]

print("Bienvenid@ al juego de piedra papel tijera :)")
nombre = input("Cual es tu nombre:")
jugadas = 0
partidasGanadas = 0

while jugadas < 5:
    JugadaJugador = input("Elige tu jugada(piedra, papel o tijera): ")
    while JugadaJugador != "piedra" and JugadaJugador != "papel" and JugadaJugador != "tijera":
        print("Porfavor eligue bien.")
        JugadaJugador = input("Elige tu jugada(piedra, papel o tijera): ")

    JugadaMaquina = random.choice(posibilidades)
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
if partidasGanadas >= 3:
    print("Enhorabuena "+ nombre + ", has ganado. En total ganaste " + str(partidasGanadas) + " rondas de 5")
else:
    print("Lo siento " + nombre + ", has perdido. En total ganaste " + str(partidasGanadas) + " rondas de 5")