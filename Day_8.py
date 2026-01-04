#🔹 ----------------------Section 1: Lists (Intermediate)--------------------------

#1. Grouping Elements (Chunking a List)
#Logic: Break a list into smaller sub-lists of size n.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3

chunks = []

for i in range(0, len(data), chunk_size):
    chunk = data[i:i + chunk_size]
    chunks.append(chunk)

print("Chunked:", chunks)

# 1. Sum and Average of a List
# Problem: Take a list of numbers and calculate the sum and the average of all elements without using the built-in sum() function.
numbers = [1,2,10,50,20,22,11]
total = 0

for num in numbers:
    total += num
average = total / len(numbers)
print("Sum of numbers is", total)
print("The numbers of average is", average)

# 2. Find Largest and Smallest Number
# Problem: Find the maximum and minimum numbers in a list without using max() or min().
nums = [15, 2, 45, 12, 89, 4]
largest = nums[0]
smallest = nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("The largest numbers is",largest)
print("The smallest numbers is",smallest)

# 3. Reverse a List
# Problem: Reverse a list using two methods: Slicing and the reverse() method.
lst = [1, 2, 3, 4, 5]
reversed_1st = lst[::-1] # use slicing
# using method
lst.reverse()
print("The reversed using method",lst)
print("The reversed using slicing",reversed_1st)

# 4. Remove Duplicates
# Problem: Remove duplicate elements from a list.
items = [1, 2, 2, 3, 4, 4, 4, 5]
unique_items = list(set(items))

#using logic building
result = []
for i in items:
    if i not in result:
        result.append(i)
print("Unique list using logic",result)        
print("unique items using method",unique_items)

# 5. Count Occurrences
# Problem: Count how many times a specific element appears in a list.
colors = ["red", "blue", "red", "green", "red", "blue"]
target = "red"
count = 0
for c in colors:
    if c == target:
        count += 1
print(f"{target} & appears {count} times")
# 6. List Comprehension (Filtering)
# Problem: Use list comprehension to create a new list containing only the squares of even numbers from an existing list.
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_even = [x**2 for x in original if x % 2==0]
print("The square of even numbers",square_even)

# 7. Find the Second Largest Number
# Problem: Find the second largest number in a list without sorting the entire list.
nums = [10, 20, 4, 45, 99, 99, 45]
nums = list(set(nums)) # Remove duplicate numbers from nums
largest = second_largest = float('-inf')
for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n
print("The second_largest number is",second_largest)

# 8. Check if List is Sorted
# Problem: Write a logic to check if a list is sorted in ascending order.
my_list = [10, 20, 30, 40, 50]
is_sorted = True
for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print("List is sorted")
else:
    print("List not sorted")

# 9. Merge and Sort Two Lists
# Problem: Take two lists, merge them, and sort the final list.
list1 = [1, 5, 9]
list2 = [2, 4, 8]

# Merging
merged = list1 + list2

# Sorting
merged.sort()

print("Merged and Sorted:", merged)

# 10. Rotate a List (Left Rotation)
# Problem: Rotate a list to the left by k positions. (Example: [1,2,3,4,5] rotated by 2 becomes [3,4,5,1,2]).
lst = [1, 2, 3, 4, 5]
k = 2

# Logic: Slicing
# Get elements from index k to end + elements from start to index k
rotated = lst[k:] + lst[:k]

print("Rotated List:", rotated)

# prime number check
num = int(input("Enter the number: "))
is_prime = True
if num <= 1:
    print("This is not a prime number.Please enter a number that is greater than 1")
else:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 1. Tuple Unpacking
# Problem: Create a tuple with 3 elements (Name, Age, City) and unpack them into three separate variables.
person = ("Rizowan",25,"Bangladesh")
name,age,country = person
print("Name:",name)
print("Age:",age)
print("Country:",country)

# 2. Find the Index of an Element
# Problem: Find the index position of the number 7 in the tuple (1, 3, 5, 7, 9, 7).
nums = (1, 3, 5, 7, 9, 7)
index_pos = nums.index(7)
print("The position of number 7 is",index_pos)

# 3. Count Occurrences
# Problem: Count how many times the word "Python" appears in a given tuple.
langs = ("Java", "Python", "C++", "Python", "JavaScript", "Python")
target = "Python"
count = 0
for c in langs:
    if c == target:
        count += 1
print(f"python appears {count} times")

langs = ("Java", "Python", "C++", "Python", "JavaScript", "Python")
count_py = langs.count("Python")
print(count_py)

# 4. Check if an Item Exists
# Problem: Check if a specific element (e.g., 50) exists in a tuple using an if statement.
my_tuple = (10,20,30,40,50)

if 50 in my_tuple:
    print("50 present in my tuple")
else:
    print("Not found")

# 5. Reverse a Tuple
# Problem: Reverse a tuple without using a loop.
original = (1,2,3,4,5,6,7)

reversed_tuple = original[::-1]
print("Reverses Tuple is",reversed_tuple)
print("Original is",original)
# 6. Convert Tuple to List (and vice-versa)
# Problem: Since tuples are immutable, you cannot add items. Change the tuple (10, 20, 30) to (10, 20, 30, 40) by converting it to a list first.
# Solution
tup = (10, 20, 30)

tup_list = list(tup)
tup_list.append(40)

tup = tuple(tup_list)
print(tup)

# 7. Find Min, Max, and Sum
# Problem: Find the maximum, minimum, and the sum of all numbers in a tuple.
numbers = (10,20,40,50,40,60,70)
print("Maximum",max(numbers))
print("Minimum",min(numbers))
print("Sum of numbers",sum(numbers))

# 8. Concatenate Two Tuples
# Problem: Create two tuples and join them into one single tuple.
# Solution
t1 = (1, 2, 3)
t2 = ("a", "b", "c")

combined = t1 + t2
print(combined)

# 9. Nested Tuple Access
# Problem: Access the value "Apple" from the following nested tuple: (1, [10, 20], ("Orange", "Apple", "Banana")).
nested = (1, [10, 20], ("Orange", "Apple", "Banana"))
fruit = nested[2][1]
print(fruit)

# 10. Check if All Elements are the Same
# Problem: Check if all elements in a tuple are identical (e.g., (10, 10, 10) should return True).
tup1 = (10, 10, 10, 10)
is_same = len(set(tup1)) == 1
print("All the elements are same",is_same)

# Fibonacci series
num = int(input("Enter the number: "))
n1,n2 = 0,1
sum = 0
if num <= 0:
    print("Please enter the number greater than Zero")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2

























