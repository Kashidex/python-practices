# EXERCISE 2: ODD OR EVEN

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

## Extras 1: If the number is a multiple of 4, print out a different message.
## Extras 2: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
## If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

###

check = int(input("Can you give me a number?: "))
num = int(input("Give me a number to divide by: "))

if check % 2 == 0:
    if check % 4 == 0:
        print(f"{check} is even and is a multiple of 4.")
    else:
        print(f"{check} is an even number.")
else:
    print(f"{check} is an odd number.")

if num == 0:
    print("You can't divide by zero.")
elif check % num == 0:
    print(f"{check} divides evenly by {num}.")
else:
    print(f"{check} does not divide evenly by {num}.")
