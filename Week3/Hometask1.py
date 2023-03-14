"""For this challenge, you are supposed to find the sum of the digits of a two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13
Need extra knowledge!! """



a = 45
b = 38
c = 67
result1 = a // 10 + a % 10
result2 = b //10 + b % 10
result3 = c //10 + c % 10
print(result1, result2, result3)