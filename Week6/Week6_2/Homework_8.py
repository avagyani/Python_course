"""Create a function that takes an integer and returns it as an ordinal 
number. An Ordinal Number is a number that tells the position of something 
in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.
Examples
return_end_of_number(553) ➞ ՛553-RD՛
return_end_of_number(34) ➞ ՛34-TH՛
return_end_of_number(1231) ➞ ՛1231-ST՛
return_end_of_number(22) ➞ ՛22-ND՛
return_end_of_number(412) ➞ ՛412-TH՛"""



num = int(input("Enter a number -> "))
result = str(num)

if result[-2] != '1':
    if result[-1] == '1':
        result += "-ST"
    elif result[-1] == '2':
        result += "-ND"
    elif result[-1] == '3':
        result += "-RD"
    else:
        result += "-TH"
else:
    result += "-TH"

print(result)

