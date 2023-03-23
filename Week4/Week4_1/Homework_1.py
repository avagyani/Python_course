"""Create a function that takes a string and returns it as an integer.
Examples
'6' ➞ 6
'1000' ➞ 1000
Notes
All numbers will be whole.
All numbers will be positive."""


text = input("Please, enter any number -> ")


result = text.isalnum()



print((not result) * "Please, enter whole and positive number" or result * int(text))
