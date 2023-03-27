"""EXTRA Knowledge
Create a function that takes two numbers as arguments num, length and 
returns a list of multiples of num until the list length reaches length.
Examples
7, 5 ➞ [7, 14, 21, 28, 35]
12, 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
17, 6 ➞ [17, 34, 51, 68, 85, 102]"""



# version_1

# first_number = int(input("Enter first number"))
# length = int(input("Enter length"))
# last_number = first_number * length
# result = list(range(first_number, last_number + 1, first_number))
# print(result)


# version_2

# multiples = lambda num, length, i=1, lst=[]: (lst if len(lst) == length else multiples(num, length, i+1, lst + [num*i]))
# print(multiples(7, 5))

# version_3

def list_of_multiples(num, length):
    lst = [num] * length
    lst[0:] = [num * (i+1) for i in range(length)]
    return lst
print(list_of_multiples(17, 6))