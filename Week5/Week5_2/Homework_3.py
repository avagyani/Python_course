"""Create a function that takes a dictionary of objects like 
{ "name": "John", "notes": [3, 5, 4] } and returns a dictionary 
of objects like { "name": "John", "top_note": 5 }.
Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ 
{ "name": "John", "top_note": 5 }
top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ 
{ "name": "Max", "top_note": 6 }
top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ 
{ "name": "Zygmund", "top_note": 3 }
"""



#version_1
# dct = { "name": "John", "notes": [3, 5, 4] }

# tpl_max = max(dct["notes"])

# new_dct = {"top_notes": tpl_max}

# dct.pop("notes")
# dct.update(new_dct)

# print(dct)


#version_2
# dct = { "name": "John", "notes": [3, 5, 4] }

# tpl_max = max(dct.get("notes"))

# dct.pop("notes")

# dct["top_notes"] = tpl_max

# print(dct)


#version_3
dct = { "name": "John", "notes": [3, 5, 4] }

tpl_max = max(dct.get("notes"))

dct.pop("notes")

dct.setdefault("top_notes", tpl_max)

print(dct)