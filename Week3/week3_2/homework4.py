"""Extra Knowledge 
Create a function that takes two strings as arguments and return either 
True or False depending on whether the total number of characters in 
the first string is equal to the total number of characters in the second string.
Examples
"AB", "CD" ➞ True
"ABC", "DE" ➞ False
"hello", "edabit" ➞ False"""



a = input("Please type something -> ")
b = input("Please type something else -> ")

result = len(a) == len(b)

print(result)