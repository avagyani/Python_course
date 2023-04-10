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
my_lst_1 = []
my_lst_2 = []
is_vowel = ['a', 'e', 'i', 'o', 'u']

for i in my_str:
    if i in is_vowel:
        my_lst_1.append(i)
    else:
        my_lst_2.append(i)    
    
result = "".join(my_lst_1) + "".join(my_lst_2)

print(result)
