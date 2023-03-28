"""Write a function that converts a dictionary into a list of 
keys-values tuples.
Examples
dict_to_list({
  'D': 1,
  'B': 2,
  'C': 3
}) ➞ [('B', 2), ('C', 3), ('D', 1)]
dict_to_list({
  'likes': 2,
  'dislikes': 3,
  'followers': 10
}) ➞ [('dislikes', 3), ('followers', 10), ('likes', 2)]
"""



dict_to_list = {
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}

result = dict_to_list.items()
print(sorted(result))