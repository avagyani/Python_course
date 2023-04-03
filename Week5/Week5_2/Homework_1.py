"""EXTRA Knowledge
Given three lists of integers: lst1, lst2, lst3, 
return the sum of integers which are common in all three lists.
Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.
sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
// 2, 2 & 3 are common in all 3 lists.
sum_common([1], [1], [2]) ➞ 0
"""


# version_1
lst_1 = [1, 2, 2, 3]
lst_2 = [5, 3, 2, 2]
lst_3 = [7, 3, 2, 2]

result = []

for i in lst_1:
    if i in lst_2 and i in lst_3:
        result.append(i)
        
print(sum(result))


# version_2
lst1 = [1, 2, 2, 3]
lst2 = [5, 3, 2, 2]
lst3 = [7, 3, 2, 2]

result = 0

for i in lst1:
    if i in lst2 and i in lst3:
        result += i

print(result)