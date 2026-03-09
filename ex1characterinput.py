# EXERCISE 1: CHARACTER INPUT

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

###

from datetime import datetime

# fetching both variables in just one command
userName, userAge = input("Tell me your name and your age: ").split()

# turning year into an input to not be out of date
currentYear = datetime.now().year

# year calculation
hundredYearsOldDate = 100 - int(userAge) + currentYear

# formatted string in variable for further usage
message = f"{userName}, you will be 100 years old in approximately {hundredYearsOldDate}."

print(message)

## Extras 1: Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
## Extras 2: Print out that many copies of the previous message on separate lines.

# repeating the code enough times
# print('\n'.join(message * repeaterNumber))
print('\n'.join([message] * int(input(f"{userName}, can you give me another number?: "))))
