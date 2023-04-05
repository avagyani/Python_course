"""EXTRA Knowledge
Given an input string, reverse the string word by word 
(reversed word also).
Examples
"the sky is blue" ➞ "eulb si yks eht"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
Try to solve this in linear time.
"""



my_str = input("Input string -> ")
my_str = my_str.strip()
words = my_str.split()

reversed_words = [word[::-1] for word in words]

reversed_words = reversed_words[::-1]
reversed_str = " ".join(reversed_words)

print(reversed_str)
