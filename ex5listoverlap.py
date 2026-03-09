# EXERCISE 5: LIST OVERLAP

# Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

## Extras 1: Randomly generate two lists to test this

###

import random
import os

os.system('cls')

def findCommonElements(list1, list2):
    commonElements = set(list1) & set(list2)
    if len(commonElements) != 0:
        return set(commonElements)
    else:
        return "None"

def newRandomList():
    newList = []
    for i in range(random.randint(1, 20)):
        newList.append(random.randint(1, 100))
    return set(newList)

print(findCommonElements(a, b))

newList1 = newRandomList()
newList2 = newRandomList()

print(f"\nNew randomly generated lists:\n"
f"List 1: {newList1}\n"
f"List 2: {newList2}\n\n"
f"Common elements found in both new lists: {findCommonElements(newList1, newList2)}.")

## Extras 2: Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
## -- I mean, c'mon. I can't do that.