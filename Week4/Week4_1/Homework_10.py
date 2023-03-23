"""An isogram is a word that has no duplicate letters. 
Create a function that takes a string and returns either 
True or False depending on whether or not it's an 'isogram'.
Examples
'Algorism' ➞ True
'PasSword' ➞ False
# Not case sensitive.
'Consecutive' ➞ False"""



word = input("type some word ->")

clean_word = word.lower()
letters = set(clean_word)

result = len(letters) == len(clean_word)

print(result)