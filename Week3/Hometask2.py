"""A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
44 ➞ True
45 ➞ False
-44 ➞ False"""



a = 44
result1 = a // 10 == a % 10

b = 45
result2 = b // 10 == b % 10

c = -44
result3 = c // 10 == c % 10

print(result1, result2, result3)