"""EXTRA Knowledge
Write a function that takes a list of numbers and returns a
 list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
[1, 2, 3, 4, 5, 6] ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
[-1, -2, -3, -4, -5, -6] ➞ [-12, -9]
[0, 0] ➞ [0, 0]
Notes
Count 0 as an even number."""



# version_1
# lst = [-1, -2, -3, -4, -5, -6]

# result = []
# even = []
# odd = []

# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# result.append(sum(even))
# result.append(sum(odd))
# print(result)


# version_2
lst = [-1, -2, -3, -4, -5, -6]

result = []
even = 0
odd = 0

for i in lst:
    if i % 2 == 0:
        even += i
    else:
        odd += i

result.append(even)
result.append(odd)
print(result)