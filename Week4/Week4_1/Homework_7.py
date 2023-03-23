"""Create a function that replaces all the vowels in a string 
with a specified character.
Examples
'the aardvark', '#' ➞ 'th# ##rdv#rk'
'minnie mouse', '?' ➞ 'm?nn?? m??s?'
'shakespeare', '*' ➞ 'sh*k*sp**r*'"""


# string = input("Type some word -> ")
# specified_char = input("Enter pecified character -> ")
# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# for char in vowels:
#     string = string.replace(char, specified_char)

# print(string)


# string = input("Type some word -> ")
# specified_char = input("Enter pecified character -> ")
# vowels = "aeiouAEIOU"
# len_vowels = len(vowels)

# while len_vowels > 0:
#     letter = vowels[len_vowels-  1]
#     len_vowels -= 1
#     string = string.replace(letter, specified_char)

# print(string)


string = input("Type some word -> ")
specified_char = input("Enter pecified character -> ")

string = string.replace("a", specified_char)
string = string.replace("e", specified_char)
string = string.replace("i", specified_char)
string = string.replace("o", specified_char)
string = string.replace("u", specified_char)
string = string.replace("A", specified_char)
string = string.replace("E", specified_char)
string = string.replace("I", specified_char)
string = string.replace("O", specified_char)
string = string.replace("U", specified_char)

print(string)
