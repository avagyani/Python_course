"""Create a function that takes a number as its argument and returns a list 
of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving 
a remainder. The second example is a factor of 12, because 12 / 2 = 6, 
with remainder 0."""



#version_1
# num = int(input("Enter a number, please -> "))
# factorize = []

# while num < 0:
#     num = int(input("Enter a positive number, please -> "))

# for i in range(1, num + 1):
#     if num % i == 0:
#         factorize.append(i)

# print(factorize)



#version_2
# num = 12
# result = []

# for i in range(1, num//2 + 1):     #որպեսզի շատ թվերի համար էդքան շատ չաշխատի
#     if num % i == 0:
#         result.append(i)

# result.append(num)

# print(result)



#version_3
def factorize(num: int):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

print(factorize(12))
