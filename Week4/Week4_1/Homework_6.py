"""EXTRA Knowledge
Create a function that returns True if a given inequality expression is correct
 and False otherwise.
Examples
"3 < 7 < 11" ➞ True
"13 > 44 > 33 > 1" ➞ False
"1 < 2 < 6 < 9 > 3" ➞ True"""



#print(3 < 7 < 11) Sa     - mer antsatsov
# print(3 < 7 and 7 < 11)




a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b <  c:                 #if-ov tarberak1
    print("True")
else:
    print("False")

# if (a < b and b < c):          if-ov tarberak2
#     print("True")
# else:
#     print("False")

