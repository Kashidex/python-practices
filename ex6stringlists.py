# EXERCISE 6: STRING LISTS

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

###

a = input("Give me a string to be checked if it's whether a palindrome or not: ")
if a == a[::-1]:
    print("Your string is a palindrome.")
else:
    print("Your string is not a palindrome.")


# a = "hello my name is sonic the hedgehog i like chili dogs"
# lenght = len(a) - 1
# print(a[lenght:0:-1])length       