# EXERCISE 4: DIVISORS

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

###

num = int(input("Can you give me a number?: "))
divisorNums = [1]

for i in range(2, num):
    if num % i == 0:
        divisorNums.append(i)

divisorNums.append(num)
print(f"The divisors of {num} is: {divisorNums}.")