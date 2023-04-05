"""Create a function that changes all the elements in a list as follows:
Add 1 to all even integers, nothing to odd integers.
Concatenates '!' to all strings and make the first letter of the word 
a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(['a', 12, True]) ➞ ['A!', 13, False]
change_types([13, '13', '12', 'twelve']) ➞ [13, '13!', '12!', 'Twelve!']
change_types([False, 'False', 'true']) ➞ [True, 'False!', 'True!']
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and 
as readable as possible!
"""



my_lst = [False, 'False', 'true']
new_lst = []

for i in my_lst:
    if type(i) == int:
        if i % 2 == 0:
            new_lst.append(i + 1)
        else:
            new_lst.append(i)
    if type(i) == str:
        my_str = i.capitalize()
        smbl = "!"
        new_lst.append(f"{my_str}{smbl}")
    if type(i) == bool:
        if i == True:
            new_lst.append(False)
        else:
            new_lst.append(True)

print(new_lst)