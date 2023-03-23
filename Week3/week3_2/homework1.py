"""Emmy has written a function that returns a greeting to users. 
However, she's in love with Mubashir, and would like to greet him 
slightly differently. She added a special case in her function, 
but she made a mistake.
Can you help her?
Examples
"Matt" ➞ "Hello, Matt!"
"Helen" ➞ "Hello, Helen!"
'Mubashir' ➞ 'Hello, my Love!'"""


name = input("Please type your name here -> ")
result = "Hello, " + ((name * (name != "Mubashir"))
                      or ("my Love" * (name == "Mubashir"))) + "!"
print(result)
