"""Given a list of numbers, return True if the sum of the values
in the list is less than 100; otherwise return False.
Examples
[5, 57] ➞ True
[77, 30] ➞ False
[0] ➞ True
"""



a = [5, 57]
b = [77, 30]

sum_a = sum(a)
sum_b = sum(b)

result_a = sum_a < 100
result_b = sum_b < 100

print(result_a)
print(result_b)
