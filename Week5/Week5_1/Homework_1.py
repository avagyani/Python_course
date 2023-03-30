"""Given a list, rotate the values clockwise by one 
(the last value is sent to the first position).
Check the examples for a better understanding.
Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]"""



# version_1
# lst = [20, 15, 26, 8, 4]
# lst_1= lst[:4]
# lst_2 = lst[4:]
# lst_2.extend(lst_1)
# print(lst_2)

lst = [20, 15, 26, 8, 4]
a = lst.pop(4)
lst.insert(0, a)
print(lst)