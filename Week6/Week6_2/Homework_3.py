"""Create a function that takes an array of hurdle heights and a jumper's 
jump height, and determine whether or not the hurdler can clear all the 
hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal 
to the hurdle height.
Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False
Notes
Return True for the edge case of an empty array of hurdles. 
(Zero hurdles means that any jump height can clear them)."""



# version_1
# hurdle_jump = ([5, 5, 3, 4, 5], 3)

# hurdle_heights = hurdle_jump[0]
# jump_height = hurdle_jump[1]

# if hurdle_heights == []:
#     result = True
# else:
#     result = max(hurdle_heights) <= jump_height

# print(result)



#version_2
# hurdle_jump = ([1, 2, 3, 4, 5], 5)

# hurdle, jump = hurdle_jump

# result = False

# if hurdle:
#     if max(hurdle) <= jump:
#         result = True
# else:
#     result = True

# print(result)



#version_3
def hurdle_jump(hundle: list, jump: int):
    result = False
    if hundle != []:
        if max(hundle) <= jump:
            result = True
    else:
        result = True
    return result

print(hurdle_jump([1, 2, 1], 1))
