"""Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
1,3 ➞ 3780
2,0 ➞ 7200"""



hour1 = 1
minute1 = 3

hour2 = 2
minute2 = 0

hourInSeconds = 3600
minuteInSeconds = 60

result1 = hour1 * hourInSeconds + minute1 * minuteInSeconds
result2 = hour2 * hourInSeconds + minute2 * minuteInSeconds

print(result1, result2)