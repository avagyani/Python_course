"""Create a function that returns a list of strings sorted by 
length in ascending order.
Examples
sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
sort_by_length([]) ➞ []
Notes
Strings will have unique lengths, so don't worry about comparing 
two strings with identical length.
Return an empty array if the input array is empty"""



lst = ["apple", "pie", "shortcake"]
print(sorted(lst, key = len))