"""Create a function that takes a number as its argument and returns a list 
of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving 
a remainder. The second example is a factor of 12, because 12 / 2 = 6, 
with remainder 0."""



num = int(input("Enter a number, please -> "))
factorize = []

while num < 0:
    num = int(input("Enter a positive number, please -> "))
    continue

for i in range(1, num + 1):
    if num % i == 0:
        factorize.append(i)

print(factorize)