"""Create a function that converts a date formatted 
as MM/DD/YYYY to YYYYDDMM.
Examples
'11/12/2019' ➞ '20191211'
'12/31/2019' ➞ '20193112'
'01/15/2019' ➞ '20191501'"""



date = "01/15/2019"
list_of_date = date.split("/")
list_reversed = list_of_date[::-1]
result = list_reversed[0] + list_reversed[1] + list_reversed[2]
print(result)
