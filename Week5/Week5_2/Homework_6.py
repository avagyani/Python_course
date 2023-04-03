"""A number is said to be Harshad if it's exactly divisible 
by the sum of its digits. Create a function that determines 
whether a number is a Harshad or not.
Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True
is_harshad(89) ➞ False
is_harshad(516) ➞ True
is_harshad(200) ➞ True"""



# version_1
# x = int(input("Enter a number"))
# result = 0
# while x > 9:
#     rem = x % 10
#     x = x // 10
#     result += rem

# final_res = result + x
# print(x % final_res == 0)


# version_2
x = int(input("Enter a number"))   #int մուտքագրեցի, հետո փոխեցի str, որ տրված պայմանից չշեղվեմ

str = str(x)
lst = [int(char) for char in str]

summary = sum(lst)

print(x % summary == 0)
