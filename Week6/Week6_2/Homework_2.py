"""Create a function that takes a list (slot machine outcome) and returns 
True if all elements in the list are identical, and False otherwise. 
The list will contain 4 elements.
Examples
test_jackpot(['@', '@', '@', '@']) ➞ True
test_jackpot(['abc', 'abc', 'abc', 'abc']) ➞ True
test_jackpot(['SS', 'SS', 'SS', 'SS']) ➞ True
test_jackpot(['&&', '&', '&&&', '&&&&']) ➞ False
test_jackpot(['SS', 'SS', 'SS', 'Ss']) ➞ False"""



#version_1
# test_jackpot = ['SS', 'SS', 'SS', 'Ss']

# if len(test_jackpot) != 4:
#     print("The list will contain 4 elements")

# else:
#     if test_jackpot[0] == test_jackpot[1] == test_jackpot[2] == test_jackpot[3]:
#         print(True)
#     else:
#         print(False)



#version_2
# test_jackpot = ['SS', 'SS', 'SS', 'Ss']

# new_set = set(test_jackpot)
# result = False

# if len(new_set) == 1:
#     result = True
    
# print(result)



#version_3
def test_jackpot(a: list):
    return len(set(a)) == 1

print(test_jackpot(['SS', 'SS', 'SS', 'Ss']))
