# EXERCISE 8: ROCK PAPER SCISSORS

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

###

import random

cpuChoices = ["rock", "paper", "scissors"]

outcomes = {
"rockrock": "Draw", "rockpaper": "Lose", "rockscissors": "Win",
"paperrock": "Win", "paperpaper": "Draw", "paperscissors": "Lose",
"scissorsrock": "Lose", "scissorspaper": "Win", "scissorsscissors": "Draw"}

outcomeMessages =  {"Win": "Congrats!", "Draw": "Try Again!", "Lose": "Better luck next time!"}

print("Rock, Paper, Scissors Game\n")

while True:
    userTurn = input("Type your decision (rock paper or scissors): ").lower()
    cpuTurn = cpuChoices[random.randint(0, 2)]

    finalOutcome = outcomes.get(userTurn + cpuTurn)
    if finalOutcome == None:
        print("Please enter a valid decision.")
    else:
        print(f"Your choice: {userTurn} // CPU's choice: {cpuTurn} // Result: {finalOutcome}!\n{outcomeMessages.get(finalOutcome)}")
        repeatAsk = input("Do you want to play again? (y/n): ").lower()
        if repeatAsk == "y" or repeatAsk == "yes":
            pass
        else:
            break