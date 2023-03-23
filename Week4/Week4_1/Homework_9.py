"""Create a function that takes a string 
(will be a person's first and last name) 
and returns a string with the first and last name swapped.
Examples
'Donald Trump' ➞ 'Trump Donald'
'Rosie O'Donnell' ➞ 'O"Donnell Rosie'
'Seymour Butts' ➞ 'Butts Seymour'"""



name = input("Enter your first and last name")

name = name.split()

name[0], name[1] = name[1], name[0]

name = " ".join(name)

print(name)
