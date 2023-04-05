"""Create a function that takes damage and speed (attacks per second) 
and returns the amount of damage after a given time.
Examples
damage(40, 5, 'second') ➞ 200
damage(100, 1, 'minute') ➞ 6000
damage(2, 100, 'hour') ➞ 720000
Notes
Return 'invalid' if damage or speed is negative."""



damage = (2, 100, 'hour')
if damage[0] >= 0:
    if damage[2] == "second":
        print(damage[0] * damage[1] * 1)
    elif damage[2] == "minute":
        print(damage[0] * damage[1] * 60)
    elif damage[2] == "hour":
        print(damage[0] * damage[1] * 3600)
else:
    print("Invalid")