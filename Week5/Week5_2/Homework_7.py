"""EXTRA Knowledge
Given an input string, reverse the string word by word.
Examples
"the sky is blue" ➞ "blue is sky the"
"  hello world!  " ➞ "world! hello"
"a good   example" ➞ "example good a"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. 
However, your reversed string should not contain leading or 
trailing spaces.
Try to solve this in linear time."""



my_str = input("Input string -> ")

words = my_str.strip().split()
reversed_words = ' '.join(words[::-1])

print(reversed_words)