name = "hello WORLD"
print(name.capitalize())

name = "HELLO WORLD"
print(name.lower())

print(name.upper())
na = "python"
print(na.center(10,'*'))
print(name.count('L'))
print(name.index('o'))

num = ['name',10,20,30]
hello = set(num)
print(hello)
print(type(hello))
# Thi is first one
a = {'x':1,'y':2}
b = a.copy()
b['x'] = 5
print(a['x'])

# This is second one
arr = [2,4,6,8]
result = 0
for i in arr:
    result += i
print(result)
# this is third one
result = "" or 0 or "hello"
print(result)

# this is fourth one
x = [10,20,30]
y = x[:2]
y.append(40)
print(x)
print(y)

# this is fifth one
t = (1,2,3)
try:
    t[1] == 100
except:
    print("error")
# this is six
s = "mississippi"
result = s.count("s") > s.count("p")
print(result)
# Problem 1: Find all even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = []
for num in numbers:
    if num % 2 == 0:
        even_number.append(num)
print(even_number)
# Problem 2: Create a list of squares from 1 to(List comprehension )
square = [x ** 2 for x in range(1,11)]
print(square)
# Problem: Remove duplicates from [1, 2, 2, 3, 4, 4, 5]
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_number = []
for num in numbers:
    if num not in unique_number:
        unique_number.append(num)
print(unique_number)
# Problem: Merge two lists and sort them
list_1 = [1,3,5,7]
list_2 = [2,4,6,8]
merged = list_1 + list_2
merged.sort()
print(merged)
# Problem: Flatten [[1, 2], [3, 4], [5, 6]]
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)
# Problem 6: Tuple unpacking
a = 10
b = 20
a,b = b,a
print(f"a={a} & b={b}")
# Problem: Find max and min from tuple
numbers = (45, 12, 78, 34, 89, 23)
max_number = max(numbers)
min_number = min(numbers)
print(f"Max_number = {max_number} & min_number = {min_number}")
# use for loop

numbers = (45, 12, 78, 34, 89, 23)
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print("Max_number =", max_number)
min_number = numbers[0]
for num in numbers:
    if num < min_number:
        min_number = num
print(f"Min_number = {min_number}")

# Problem 8: Tuple count ও index method
tuple_data = (1, 2, 3, 2, 4, 2, 5)
count_tuple = tuple_data.count(2)
index_find = tuple_data.index(3)
print(f"Count_tuple = {count_tuple} & find_index = {index_find}")

# Problem 9: Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)

#  Problem: Get student marks
student = {
    'name': 'Rahim',
    'age': 20,
    'marks': {'math': 85, 'english': 78, 'science': 92}
}
result = f"Name: {student['name']}'s & Marks: {student['marks']['english']}"
print(result)
# Problem: Add new subject
marks = {'science':88,'english':99}
marks['math'] = 90
marks['bangla'] = 100
print(marks)

# Problem 12: Dictionary loop
person = {'name': 'Karim', 'age': 25, 'city': 'Dhaka'}
for key,value in person.items():
    print(f"{key}: {value}")
# Problem: Find student with highest marks

students = {'Rahim': 85, 'Karim': 92, 'Salma': 78, 'Nila': 95}

top_student = max(students, key=students.get)
print(f"Top student: {top_student} with {students[top_student]} marks")
# Problem: Merge two dictionaries '
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged)
# Problem 15: Set operations - union, intersection, difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print(f"Union: {union}") 
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")

from colorama import Fore
print(Fore.YELLOW + "Hello")









