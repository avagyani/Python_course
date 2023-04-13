"""Imajine you have three numbers: a, b, and c. c is equal to either a or b, 
but you don't know which one. Your task is to create a function that returns 
whatever number c isn't, out of a and b. So, if c is equal to a, return b, 
and if c is equal to b, return a. Here's what make this challenge difficult:
you cannot use any if statements.

Examples:

swap(1, 0, 0) -> 1
a = 1. b = 0. c = 0
return a

swap(1, 3, 1) -> 3
a = 1. b = 3. c = 1
return b

swap(27, 31, 31) -> 27
a = 27. b = 31. c = 31
return a

Notes:
* To prevent cheating, you also can't call any functions.
* c will always be equal to either a or b.
* a will never equal b.
* a, b, and c will always be integers.
"""



def swap(a, b, c):
    result  =  (a == c) * b + (b == c) * a
    return result

print(swap(27, 31, 31))
