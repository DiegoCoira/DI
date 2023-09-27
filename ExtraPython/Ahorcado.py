
import random


def CheckInput(input):
    isRight = True
    if len(input) > 1 or input.isdigit() == True:
        print("Wrong input, pls try again")
        isRight = False
        
    for character in WordsUsed:
        if character == userCharacter:
            print("Word already used")
            isRight = False
            
    return isRight


def drawing(attempts):
    if attempts == 6:
        print("  ________       ")
        print(" |       |       ")
        print(" |               ")
        print(" |               ")
        print(" |               ")
        print(" |               ")
        print("===============  ")
    elif attempts == 5:
        print("  ________       ")
        print(" |       |       ")
        print(" |       O       ")
        print(" |               ")
        print(" |               ")
        print(" |               ")
        print("===============  ")
    elif attempts == 4:
        print("  ________       ")
        print(" |       |       ")
        print(" |       O       ")
        print(" |       |       ")
        print(" |               ")
        print(" |               ")
        print("===============  ")
    elif attempts == 3:
        print("  ________       ")
        print(" |       |       ")
        print(" |       O       ")
        print(" |      /|       ")
        print(" |               ")
        print(" |               ")
        print("===============  ")
    elif attempts == 2:
        print("  ________       ")
        print(" |       |       ")
        print(" |       O       ")
        print(" |      /|\      ")
        print(" |               ")
        print(" |               ")
        print("===============  ")
    elif attempts == 1:
        print("  ________       ")
        print(" |       |       ")
        print(" |       O       ")
        print(" |      /|\      ")
        print(" |      /        ")
        print(" |               ")
        print("===============  ")
    else:
        print("  ________       ")
        print(" |       |       ")
        print(" |       O       ")
        print(" |      /|\      ")
        print(" |      / \      ")
        print(" |               ")
        print("===============  ")

archive = "palabras.txt"
with open(archive, 'r', encoding='utf-8') as file:
    palabras = [line.strip() for line in file]
    LineasNonVacias = [linea for linea in palabras if linea.strip()]
    cantidadLineas = len(LineasNonVacias)

Facil = []
Normal = []
Dificil = []
i = 0
counter = 0
while i < cantidadLineas :
    if palabras[i] != "Fácil" and palabras[i] != "Normal" and palabras[i] != "Dificil": 
        if len(palabras[i]) >= 3 and len(palabras[i]) <= 5:
            Facil.append(palabras[i])
        elif len(palabras[i]) >= 6 and len(palabras[i]) <9:
            Normal.append(palabras[i])
        elif len(palabras[i]) >= 9:
            Dificil.append(palabras[i])

    i += 1


rightInput = False
while rightInput == False:
    selection = input("Chose a difficulty (Fácil, Normal, Dificil): ")
    if selection == "Fácil":
        secretWord = random.choice(Facil)
        print("You selected the Fácil difficulty")
        rightInput = True
    elif selection == "Normal":
        secretWord = random.choice(Normal)
        print("You selected the Normal difficulty")
        rightInput = True
    elif selection == "Dificil":
        secretWord = random.choice(Dificil)
        print("You selected the Dificil difficulty")
        rightInput = True
    else:
        print("Wrong input, write your difficulty as it is intended to.")

print("You got six attempts, if you miss more than 6 times you lose the ahorcado game.")
attempts = 6
secretWordLength = len(secretWord)
HiddenWord = ['_'] * secretWordLength
WordsUsed = []

print("You got " + str(attempts) + " attempts left.")
print("")
isRight = False
gameEnd = False
isEqual = False
j = 0
while gameEnd == False:
    while isRight == False:
        userCharacter = input("Give me a word: ")
        isRight = CheckInput(userCharacter)

    charNumber = 0
    for character in secretWord:
        if character == userCharacter:
            HiddenWord[charNumber] = userCharacter
            isEqual = True
        charNumber += 1

    if isEqual == False:
        attempts -= 1
        print("Sorry, there is no " + "'" + str(userCharacter) + "'" + " in the secret word.")
            
        if attempts > 0:
            print("You still got " + "'" + str(attempts) + "'" +" attempts left.")
    else:
        print("There is a " + "'" + str(userCharacter)+ "'" + " in the secret word.")
        print("You still got " + "'" + str(attempts) + "'" + " attempts left.")
        
    WordsUsed.append(userCharacter)
    lastHiddenWord = HiddenWord

    drawing(attempts)
    print(HiddenWord)
    print("Letras ya utilizadas: ")
    print(WordsUsed)
    resultado = "".join([lista[0] for lista in HiddenWord])
    isRight = False
    isEqual = False
    if attempts == 0:
        print("Game Over")
        print("The word was " + secretWord + " unlucky.")
        gameEnd = True
    elif resultado == secretWord:
        print("You won, congratulations")
        gameEnd = True
            
    
    






