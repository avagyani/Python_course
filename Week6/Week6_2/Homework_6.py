"""Write a function that takes a string, breaks it up and returns it with 
vowels first, consonants second. For any character that's not a vowel 
(like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation).
"""



my_str = input("Enter a string -> ")
my_str_1 = ""
my_str_2 = ""
is_vowel = "aeiou"

for i in my_str:
    if i in is_vowel:
        my_str_1 += i
    else:
        my_str_2 += i  
    
result = my_str_1 + my_str_2

print(result)
