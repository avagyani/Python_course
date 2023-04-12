"""Create a function that returns the number of palindrome numbers in a 
specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. 
Between 1550 and 1552 there is exactly one palindrome: 1551.
Examples
count_palindromes(1, 10) ➞ 9
count_palindromes(555, 556) ➞ 1
count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are 
reversed. For example, 2552 reversed is still 2552. The reflectional 
symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers."""



#version_1
# a = int(input("Enter the first number -> "))
# b = int(input("Enter the second number -> "))
# palindrome = []

# for i in range(a, b + 1):
#     if str(i) == str(i)[::-1]:
#         palindrome.append(i)

# palindrome_count = len(palindrome)

# print(palindrome_count)



#version_2
# a = int(input("Enter the first number -> "))
# b = int(input("Enter the second number -> "))

# count = 0

# for i in range(a, b + 1):
#     current = str(i)
#     odd = 0
    
#     if len(current) % 2 != 0:
#         odd = 1
#     start = current[:len(current) // 2]
#     end = current[len(current) // 2 + odd:][::-1]
    
#     if start == end:
#         count += 1

# print(count)



#version_3
def count_palindromes(a: int, b: int):
    count = 0
    for i in range(a, b + 1):
        current = str(i)
        odd = 0
        if len(current) % 2 != 0:
            odd = 1
        start = current[:len(current) // 2]
        end = current[len(current) // 2 + odd:][::-1]
        if start == end:
            count += 1
    return count

print(count_palindromes(878, 898))
