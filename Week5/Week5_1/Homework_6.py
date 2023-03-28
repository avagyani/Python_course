"""Create a function that takes a dictionary of student names 
and returns a list of student names in alphabetical order.
Examples
{
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
} ➞ ["Becky", "John", "Steve"]
"""



students = {"Sutend 1": "Steve", "Sutend 2": "Becky", "Sutend 3": "John"}
print(sorted(students.values()))