"""Write a function that takes a string name and a number num (either 0 or 1) 
and return 'Hello' + name if num is 1, otherwise return 'Bye' + name.
Examples
say_hello_bye('alon', 1) ➞ 'Hello Alon'
say_hello_bye('Tomi', 0) ➞ 'Bye Tomi'
say_hello_bye('jose', 0) ➞ 'Bye Jose'"""



say_hello_bye = ('jose', 0)

name = say_hello_bye[0].capitalize()

if (say_hello_bye[1] == 1) or (say_hello_bye[1] == 0):
                                          
    if say_hello_bye[1]:
        print("Hello" + " " + name)
    else:
        print("Bye" + " " + name)
else:
    print("Number is incorrect")
