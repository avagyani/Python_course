"""Create a function that takes a list of numbers lst, 
a string s and return a list of numbers as per the following rules:
'Asc' returns a sorted list in ascending order.
'Des' returns a sorted list in descending order.
'None' returns a list without any modification.
Examples
[4, 3, 2, 1], 'Asc'  ➞ [1, 2, 3, 4]
[7, 8, 11, 66], 'Des' ➞ [66, 11, 8, 7]
[1, 2, 3, 4], 'None' ➞ [1, 2, 3, 4]"""



my_list = [4, 5, 7, 1, 2, 9, 10]
s = input("Type 'Asc' or 'Des' or 'None' ->  ")
result = sorted(my_list, reverse = s == "Des")
y = my_list * (s == "None")
print(y or result)
