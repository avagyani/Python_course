"""Write a function that takes a list and determines whether it's strictly 
increasing, strictly decreasing, or neither.
Examples
check([1, 2, 3]) ➞ "increasing"
check([3, 2, 1]) ➞ "decreasing"
check([1, 2, 1]) ➞ "neither"
check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 
is not strictly greater than the 0-indexed 1.
Input lists have a minimum length of 2."""



lst_for_check = [1, 1, 2]

if len(lst_for_check) >= 2:
    
    if lst_for_check == sorted(lst_for_check) and len(lst_for_check) == len(set(lst_for_check)):
        result = "increasing"
    
    elif lst_for_check == sorted(lst_for_check)[::-1] and len(lst_for_check) == len(set(lst_for_check)):
        result = "decreasing"
    
    else:
        result = "neither"
    
    print(result)

else:
    
    print("List must have a minimum length of 2")
