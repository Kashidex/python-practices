# EXERCISE 13: FIBONACCI

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

###


def getFibonacci(steps):
    lastTwoNumbers = []
    fibonacciList = []
    for i in range(steps):
        if len(lastTwoNumbers) != 2:
            lastTwoNumbers.append(1)
            fibonacciList.append(1)
        else:
            nextNum = sum(lastTwoNumbers)
            lastTwoNumbers.pop(0)
            lastTwoNumbers.append(nextNum)
            fibonacciList.append(nextNum)
    return fibonacciList

print(getFibonacci(int(input("Please enter how many numbers you want in the Fibonacci sequence: "))))