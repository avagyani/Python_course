"""Write a function that takes a string name and a number num (either 0 or 1) 
and return 'Hello' + name if num is 1, otherwise return 'Bye' + name.
Examples
say_hello_bye('alon', 1) ➞ 'Hello Alon'
say_hello_bye('Tomi', 0) ➞ 'Bye Tomi'
say_hello_bye('jose', 0) ➞ 'Bye Jose'"""



# version_1
# say_hello_bye = ('jose', 0)

# name = say_hello_bye[0].capitalize()

# if (say_hello_bye[1] == 1) or (say_hello_bye[1] == 0):
                                          
#     if say_hello_bye[1]:
#         print("Hello" + " " + name)
#     else:
#         print("Bye" + " " + name)
# else:
#     print("Number is incorrect")



# version_2
# input_tuple = ("alon", 1)

# name, logic = input_tuple

# if logic:
#     result = f'Hello {name.capitalize()}'
# else:
#     result = f'Bye {name.capitalize()}'

# print(result)



# version_3
def say_hello_bye(name, logic):
    if logic == 1:
        result = f"Hello {name.capitalize()}"
    elif logic == 0:
        result = f"Bye {name.capitalize()}"
    else:
        result = "Number is incorrect"

    return result

print(say_hello_bye("jose", 1))
