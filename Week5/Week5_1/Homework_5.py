"""EXTRA Knowledge
Given two strings, create a function that returns the total number 
of unique characters from the combined string.
Examples
count_unique('apple', 'play') ➞ 5
# 'appleplay' has 5 unique characters:
# 'a', 'e', 'l', 'p', 'y'
'sore', 'zebra' ➞ 7
'a', 'soup' ➞ 5"""



str_1 = input()
str_2 = input()
letters = set(str_1 + str_2)
result = len(letters)
print(result)