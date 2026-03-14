# EXERCISE 9: GUESSING GAME ONE

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

## Extras 1: Keep the game going until the user types “exit”
## Extras 2: Keep track of how many guesses the user has taken, and when the game ends, print this out.

###

import random
gameRun = True

print("Number Guessing Game")

while gameRun == True:
    randomNumber = random.randint(1,9)
    guessAttempts = 0
    guessed = False
    while guessed == False:
        try:
            userGuess = int(input("Guess a number between 1 and 9 (including 1 and 9): " ))
        except ValueError:
            print("Please enter a valid number.")
        if userGuess == randomNumber:
            print(f"You guessed correct! It took {guessAttempts + 1} attempt(s) for you to guess the number.")
            if input("Type 'exit' if you want to quit. Press enter if you want to play again. ") == "exit":
                gameRun = False
                break
            else:
                guessed = True
        elif userGuess > randomNumber:
            print("Your guess is higher.")
            guessAttempts = guessAttempts + 1
        else:
            print("Your guess is lower.")
            guessAttempts = guessAttempts + 1