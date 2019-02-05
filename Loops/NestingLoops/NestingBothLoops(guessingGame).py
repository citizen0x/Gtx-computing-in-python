"""import random
numGames = int(input("How many games would you like to play?"))
# Repeats this the number of games the user chose
for i in range(0, numGames):
    print("Game start")
    # Get a random of number from 1 to 100
    hiddenNumber = random.randint(1, 100)
    # Create userGuess and give is a value that can't be correct
    userGuess = 0
    # Repeat until the guess is correct
    while userGuess != hiddenNumber:
        # Get the user's next guess as an integer
        userGuess = int(input("Guess a number: "))
        # check if the guess is too high
        if userGuess > hiddenNumber:
            print("Too high!")
        # check if the guess is too low
        elif userGuess < hiddenNumber:
            print("Too low")
        # The guess must be right!
        else:
            print("That's right!")
"""
################################################
# 2nd Solution
import random
keepPlaying = 'y'
# while keepPlaying is "y"
while keepPlaying == 'y':
    print("Game start")
    # Get a random of number from 1 to 100
    hiddenNumber = random.randint(1, 100)
    # Create userGuess and give is a value that can't be correct
    userGuess = 0
    # Repeat until the guess is correct
    while userGuess != hiddenNumber:
        # Get the user's next guess as an integer
        userGuess = int(input("Guess a number: "))
        # check if the guess is too high
        if userGuess > hiddenNumber:
            print("Too high!")
        # check if the guess is too low
        elif userGuess < hiddenNumber:
            print("Too low")
        # The guess must be right!
        else:
            print("That's right!")
    # Update keepPlaying
    keepPlaying = input("Play again (y for yes, n for no)?")