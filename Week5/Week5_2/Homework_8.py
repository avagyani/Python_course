"""Create a function that builds a word from the scrambled letters 
contained in the first list. Use the second list to establish 
each position of the letters in the first list. 
Return a string from the unscrambled letters (that made-up the word).
Examples
word_builder(['g', 'e', 'o'], [1, 0, 2]) ➞ 'ego'
word_builder(['e', 't', 's', 't'], [3, 0, 2, 1]) ➞ 'test'
word_builder(['b', 'e', 't', 'i', 'd', 'a'], [1, 4, 5, 0, 3, 2]) ➞ 
'edabit'"""



scr_letters = ['e', 't', 's', 't']
positions = [3, 0, 2, 1]
unscrambled_word = ""

for pos in positions:
    unscrambled_word += scr_letters[pos]

print(unscrambled_word)
