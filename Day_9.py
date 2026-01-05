# Part 1: Python Dictionary (10 Problems)
# 1. Create and Access
# Create a dictionary representing a student with keys: name, age, and grade. Print only the grade.

student = {"name":"Shakil","age":20,"grade":"A+"}
print(student["grade"])

# 2. Merge Two Dictionaries
# Merge dict1 = {'a': 10, 'b': 20} and dict2 = {'c': 30, 'd': 40} into one.
dict1 = {"a":10,"b":20}
dict2 = {"c":30, "d":40}

dict1.update(dict2)
print(dict1)

#3. Character Frequency Counter
#Count the number of times each character appears in the string "banana".
word = "banana"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# 4. Check if Key Exists
# Check if the key "price" exists in the dictionary {'item': 'book', 'count': 5}.
data = {"item": "book", "count": 5}
if "price" in data:
    print("Exists")
else:
    print("Dose not exists")

# 5. Sum of All Values
# Find the total sum of all values in the dictionary {'math': 80, 'science': 90, 'english': 85}.
marks = {'math': 80, 'science': 90, 'english': 85}
total_sum = sum(marks.values())
print("The total sum of values:",total_sum)

# 6. Delete a Key
# Remove the key "city" from the dictionary {"name": "John", "city": "Dhaka", "job": "Dev"}.
person = {"name":"john", "city": "Dhaka", "Job":"Dev"}
person.pop("city")
print(person)

# 7. Dictionary Comprehension
# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 8. Map Two Lists into a Dictionary
# Convert keys = ['ID', 'Name'] and values = [101, 'Kabir'] into a dictionary.
key = ['ID', 'Name']
values = [101, 'kabir']
result = dict(zip(key,values))
print(result)

# 9. Sort Dictionary by Values
# Sort {'apple': 10, 'orange': 5, 'banana': 20} based on the values (ascending).
fruits = {'apple': 10, 'orange': 5, 'banana': 20}
sorted_fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
print(sorted_fruits)

# 10. Nested Dictionary Access
# Access the "Salary" of "Employee2" from the following data:
company = {
    "emp1": {"name": "Aziz", "salary": 50000},
    "emp2": {"name": "Bari", "salary": 60000}
}
print(company["emp2"]["salary"])

# Part 2: Python Sets (10 Problems)
# 1. Create and Add
# Create an empty set, add the numbers 10, 20, and 30 to it, and print the set.

s = set()
s.add(10)
s.add(10)
s.add(20)
s.add(30)
s.add(40)
print(s)
# 2. Remove Duplicates from a List
# Use a set to remove duplicates from [1, 2, 2, 3, 4, 4, 5].
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print(unique_lst)

# 3. Set Intersection (Common Elements)
# Find the common elements between {1, 2, 3, 4} and {3, 4, 5, 6}.
set1 = {1,2,3,4}
set2 = {3,4,5,6}

result = set1.intersection(set2)
print(result)

# 4. Set Union (Combine)
# Combine two sets {10, 20} and {20, 30} without duplicates.
set1 = {10, 20}
set2 = {20, 30}
print(set1.union(set2))

# 5. Set Difference
# Find elements that are in Set A but not in Set B: A = {1, 2, 3}, B = {3, 4, 5}.
A = {1, 2, 3}
B = {3, 4, 5}
print(A - B) # Output: {1, 2}

# 6. Symmetric Difference
# Find elements that are in either Set A or Set B, but not in both.
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B)) # Output: {1, 2, 4, 5}

# 7. Subset Check
# Check if {1, 2} is a subset of {1, 2, 3, 4, 5}.
small = {1, 2}
big = {1, 2, 3, 4, 5}
print(small.issubset(big))
# 8. Clear a Set
# Remove all elements from the set {10, 20, 30} at once.
my_set = {10, 20, 30}
my_set.clear()
print(my_set)
# 9. Max and Min in a Set
# Find the maximum and minimum values in the set {45, 12, 89, 3, 27}.

vals = {45, 12, 89, 3, 27}
print("Max:", max(vals))
print("Min:", min(vals))
# 10. Iterate through a Set
# Print each element of the set {"Python", "Java", "C++"} using a loop.
langs = {"Python", "Java", "C++"}
for l in langs:
    print(l)
























