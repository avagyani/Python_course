"""Create a function that takes a string and 
returns the number (count) of vowels contained within it.
Examples
'Celebration' ➞ 5
'Palm' ➞ 1
'Prediction' ➞ 4
Notes
a, e, i, o, u are considered vowels (not y)."""



string = input("Type some word ->")

count_a = string.count("a")
count_A = string.count("A")
count_e = string.count("e")
count_E = string.count("E")
count_i = string.count("i")
count_I = string.count("I")
count_o = string.count("o")
count_O = string.count("O")
count_u = string.count("u")
count_U = string.count("U")

result = count_a + count_A + count_e + count_E + count_i + count_I + count_o + count_O + count_u + count_U

print(result)
