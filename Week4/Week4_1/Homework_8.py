"""Write a function that takes a credit card number and 
only displays the last four characters. 
The rest of the card number must be replaced by ************.
Examples
'1234123456785678' ➞ '************5678'
'8754456321113213' ➞ '************3213'
'35123413355523' ➞ '**********5523'
"""

card_number = input("Enter your credit card number")

len_mask = len(card_number) - 4
last_four = card_number[len_mask:]
result = "*" * len_mask + last_four

print(result)
