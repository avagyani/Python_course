"""Create a function that converts Celsius to Fahrenheit and vice versa.
Examples
convert("35*C") ➞ "95*F"
convert("19*F") ➞ "-7*C"
convert("33") ➞ "Error"
Notes
Round to the nearest integer.
If the input is incorrect, return "Error".
For the formulae to convert back and forth, check the Resources tab."""



#version_1
# input_temp = input("Enter a temperature -> ")

# if input_temp[-2] != "*" or input_temp[-1] != "C" and input_temp[-1] != "F":
#     result = "Error"
# else:
#     temp = int(input_temp[0:-2])
#     c_to_f = round(32 + temp * (9/5))
#     f_to_c = round((temp- 32) * (5/9))
#     if input_temp[-1] == "C":
#         result = str(c_to_f) + "*F"
#     elif input_temp[-1] == "F":
#         result = str(f_to_c) + "*C"

# print(result)



#version_2
input_temp = input("Enter a temperature -> ")

def convert_temp():

    if input_temp[-2:] == "*C":
        temp = float(input_temp[:-2])
        c_to_f = round(32 + temp * (9/5))
        result = str(c_to_f) + "*F"
    elif input_temp[-2:] == "*F":
        temp = float(input_temp[:-2])
        f_to_c = round((temp- 32) * (5/9))
        result = str(f_to_c) + "*C"
    else:
        result = "Error"
    return result

print(convert_temp())
