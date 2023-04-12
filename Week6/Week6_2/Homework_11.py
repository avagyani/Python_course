"""Create a function to perform basic arithmetic operations that includes 
addition, subtraction, multiplication and division on a string number 
(e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 
2. For the challenge, we are going to have only two numbers between 1 valid 
operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals 
'0' return -1.
For example:
'15 // 0'  ➞ -1
Examples
arithmetic_operation('12 + 12') ➞ 24 // 12 + 12 = 24
arithmetic_operation('12 - 12') ➞ 24 // 12 - 12 = 0
arithmetic_operation('12 * 12') ➞ 144 // 12 * 12 = 144
arithmetic_operation('12 // 0') ➞ -1 // 12 / 0 = -1
Notes
All the inputs are only integers.
The operators are * - + and //.
Hint: Think about the single space that appears before and after the 
arithmetic operator."""



#version_1
# arithmetic_operation = ('12 // 0')
# lst_operator = arithmetic_operation.strip()
# lst_operator = lst_operator.split()

# if lst_operator[1] == "//" and lst_operator[2] == "0":
#     result = -1
# else:
#     if lst_operator[1] == "+":
#         result = int(lst_operator[0]) + int(lst_operator[2])
#     elif lst_operator[1] == "-":
#         result = int(lst_operator[0]) - int(lst_operator[2])
#     elif lst_operator[1] == "*":
#         result = int(lst_operator[0]) * int(lst_operator[2])
#     elif lst_operator[1] == "//":
#         result = int(lst_operator[0]) // int(lst_operator[2])
#     else:
#         result = "invalid operation"

# print(result)




#version_2
def arithmetic_operation(a: int, b: str, c: int):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/" or b == "//":
        if c == 0:
            return -1
        else:
            return a // c
    else:
        print("Invalid operation")



result = arithmetic_operation(12, "//", 2)

print(result)
