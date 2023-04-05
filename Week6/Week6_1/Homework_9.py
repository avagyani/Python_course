"""Check if the given string consists of only letters and spaces and if 
every letter is in lower case.
Examples
letters_only("PYTHON") ➞ False
letters_only("python") ➞ True
letters_only("12321313") ➞ False
letters_only("i have spaces") ➞ True
letters_only("i have numbers(1-10)") ➞ False
letters_only("") ➞ False
Notes
Empty arguments will always return False.
Input values will be mixed (symbols, letters, numbers)."""



my_letters = input("Enter a string -> ")
my_lst = my_letters.split()
letters = "".join(my_lst)

if letters.isalpha():
    if letters == letters.lower():
        result = True
    else:
        result = False
else:
    result = False

print(result)
