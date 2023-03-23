"""Write a function that returns the string 'something' joined with a space 
' ' and the given argument a.
Examples
'is better than nothing' ➞ 'something is better than nothing'
'Bob Jane" ➞ "something Bob Jane'
'something' ➞ 'something something'"""



argument = input("Enter your text here ->")

print("something" + " "+ argument, sep = " ")
