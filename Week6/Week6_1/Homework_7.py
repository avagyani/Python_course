"""Create a function that takes two parameters and, if both parameters are 
strings, add them as if they were integers or if the two parameters are 
integers, concatenate them.
Examples
stupid_addition(1, 2) ➞ '12'
stupid_addition('1', '2') ➞ 3
stupid_addition('1', 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers."""



a = "1"
b = 2

if type(a) != type(b):
    print(None)

elif type(a) == int:
    print(str(a) + str(b))

elif type(a) == str:
    print(int(a) + int(b))
