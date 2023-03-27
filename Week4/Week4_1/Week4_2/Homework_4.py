"""Create a function that takes a list and returns 
the difference between the biggest and smallest numbers.
Examples
[10, 4, 1, 4, -10, -50, 32, 21] ➞ 82
# Smallest number is -50, biggest is 32.
[44, 32, 86, 19] ➞ 67
# Smallest number is 19, biggest is 86.
"""



my_list = [10, 4, 1, 4, -10, -50, 32, 21]
result = max(my_list) - min(my_list)
print(result)