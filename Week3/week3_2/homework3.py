"""Create a function that returns True if an integer is evenly divisible by 5, 
and False otherwise.
Examples
5 ➞ True
-55 ➞ True
37 ➞ False"""



a = int(input("Please, enter any number -> "))

result = a % 5 == 0
print(result)