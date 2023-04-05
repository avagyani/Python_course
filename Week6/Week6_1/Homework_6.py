"""Create a function that takes a string s and returns a list of two-paired 
characters. If the string has an odd number of characters, add an asterisk * 
in the final pair.
See the below examples for a better understanding:
Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
string_pairs("edabit") ➞ ["ed", "ab", "it"]
string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty."""



s = input("Enter a string -> ")

if len(s) % 2 != 0:
    s = s + "*"

result = list(s[i:i+2] for i in range(0, len(s), 2))

print(result)