# EXERCISE 3: LIST LESS THAN TEN

# Take a list, say for example this one:
a = [1, 6, 7, 13, 15, 16, 21, 34, 45, 46, 49, 54]
# and write a program that prints out all the elements of the list that are less than 5.

## Extras 1: Instead of printing the elements one by one,
## make a new list that has all the elements less than 5 from this list in it and print out this new list.
## Extras 2: Ask the user for a number and return a list that contains only
## elements from the original list a that are smaller than that number given by the user.

###

lessThanNumber = int(input("Give me a number to check for the elements less than it: "))
lessThanList = []

for i in a:
    if i < lessThanNumber:
        lessThanList.append(i)

print(f"Numbers that are less than {lessThanNumber} is: {lessThanList}.")