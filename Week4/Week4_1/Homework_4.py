"""Luke Skywalker has family and friends. Help him remind them who is who. 
Given a string with a name, return the relation of that person to Luke.
Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid
Examples
'Darth Vader' ➞ 'Luke, I am your father.'
'Leia' ➞ 'Luke, I am your sister.'
'Han' ➞ 'Luke, I am your brother in law.'"""



name = input("Enter your name, please -> ")

a = name == "Darth Vader"
b = name == "Leia"
c = name == "Han"
d = not (name.isalpha() or " " in name)

result_1 = a * "Luke, I am your father."
result_2 = b * "Luke, I am your sister."
result_3 = c * "Luke, I am your brother in law."
result_4 = d * "droid"

print(result_1, result_2, result_3, result_4, sep = "")
