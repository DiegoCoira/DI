import random

# Cheks if user input is valid, if it is returns a boolean with true
def CheckInput(input):
    isRight = True
    if len(input) > 1 or input.isdigit() == True:
        print("Wrong input, pls try again")
        isRight = False
        
    for character in CharactersUsed:
        if character == userCharacter:
            print("Word already used")
            isRight = False
            
    return isRight

# Function with drawings based on the attempts left
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

# Reading the File and the lines with content
archive = "palabras.txt"
with open(archive, 'r', encoding='utf-8') as file:
    palabras = [line.strip() for line in file]
    LineasNonVacias = [linea for linea in palabras if linea.strip()]
    cantidadLineas = len(LineasNonVacias)

# Initialize the dificulties and other variable
Facil = []
Normal = []
Dificil = []
i = 0
counter = 0

# We fill the lists with the words based on the amount of character a word has
while i < cantidadLineas :
    if palabras[i] != "Fácil" and palabras[i] != "Normal" and palabras[i] != "Dificil": 
        if len(palabras[i]) >= 3 and len(palabras[i]) <= 5:
            Facil.append(palabras[i])
        elif len(palabras[i]) >= 6 and len(palabras[i]) <9:
            Normal.append(palabras[i])
        elif len(palabras[i]) >= 9:
            Dificil.append(palabras[i])

    i += 1

anotherGame = True
while anotherGame == True:
# Asking for a difficulty and generating the secret word.
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
    # Calculate the amoun of characters the word has.
    secretWordLength = len(secretWord)
    HiddenWord = ['_'] * secretWordLength
    CharactersUsed = []

    print("You got " + str(attempts) + " attempts left.")
    print("")
    isRight = False
    gameEnd = False
    isEqual = False
    j = 0

    # Check when the game ends
    while gameEnd == False:
        # Asking for a character and checking if its valid
        while isRight == False:
            userCharacter = input("Give me a character: ")
            isRight = CheckInput(userCharacter)

        charNumber = 0
        # Checking if the secret word has the character that the user input
        for character in secretWord:
            if character == userCharacter:
                HiddenWord[charNumber] = userCharacter
                isEqual = True
            charNumber += 1

        # If it doesnt, minus 1 attemp
        if isEqual == False:
            attempts -= 1
            print("Sorry, there is no " + "'" + str(userCharacter) + "'" + " in the secret word.")
                
            if attempts > 0:
                print("You still got " + "'" + str(attempts) + "'" +" attempts left.")
        else:
            print("There is a " + "'" + str(userCharacter)+ "'" + " in the secret word.")
            print("You still got " + "'" + str(attempts) + "'" + " attempts left.")
        
        # Saving the characters already used by the user.
        CharactersUsed.append(userCharacter)
        lastHiddenWord = HiddenWord
        drawing(attempts)
        print(HiddenWord)
        print("Letras ya utilizadas: ")
        print(CharactersUsed)
        # Converts hiddenword into a string.
        resultado = "".join([lista[0] for lista in HiddenWord])
        isRight = False
        isEqual = False
        # if user has 0 attempts game ends
        if attempts == 0:
            print("Game Over")
            print("The word was " + secretWord + " unlucky.")
            gameEnd = True
        # Cheks if the string is equal to the secret word, if it is the game ends
        elif resultado == secretWord:
            print("You won, congratulations")
            gameEnd = True
    another = input("Quierres jugar otra partida?(s/n)")
    while another != "s" and another != "n":
        print("Please, write s or n")
        another = input("Quierres jugar otra partida?(s/n)")
    
    if another == "n":
        anotherGame = False

    






