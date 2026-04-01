# EXERCISE 14: REMOVE LIST DUPLICATES

# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.

## Extras 1: Write two different functions to do this - one using a loop and constructing a list, and another using sets.

###

testList = [4, 4, 2, 13, 14, 25, 25, 26, 37, "string1", "string2", "string2"]

def removeDuplicates1(a):
    return list(set(a))

def removeDuplicates2(a):
    newList = []
    addNewNum = bool
    for i in sorted(a, key=str):
        addNewNum = True
        for n in range(len(newList)):
            if newList[n] == i:
                addNewNum = False
                break
            else:
                pass
        if addNewNum == True:
            newList.append(i)
        else:
            pass
    return newList


print("Sort with set casting return:\n", removeDuplicates1(testList))
print("Sort with for loop return:\n", removeDuplicates2(testList))