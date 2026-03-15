# EXERCISE 11: CHECK PRIMALITY FUNCTIONS

# Ask the user for a number and determine whether the number is prime or not.

###

def primeCheck(num):
    for i in range(2, num):
        if userNumber % i == 0:
            return False
        else:
            pass
    return True

userNumber = int(input("Give me a number: "))

if primeCheck(userNumber) == True:
    print("Your number is a prime number.")
else:
    print("Your number is not a prime number.") 