
 #             ----------------------------🔹 Part 4: Lists & Tuples---------------------------

# 1. Sum of List Elements
nums = [10,20,30,40,50]
total = 0
for i in nums:
    total += i
print("The sum is:",total)

# 2. Find Max Number
nums = [5, 12, 1, 99, 4]
max_val = nums[0]
for x in nums:
    if x > max_val:
        max_val = x
print("Max Value is: ",max_val)
# 3. Separate Odd and Even
nums = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for x in nums:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print("The Even numbers: ",even)
print("The odd numbers: ",odd)

# 4. Remove Duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
print("The unique numbers are:",unique)
# 5. Reverse a List
nums = [1,2,3,4,5,6]
reverse_num = nums[::-1]
print("Reverses_number is:",reverse_num)

# 6. Count Occurrences
nums = [1,1,1,2,3,4,5,5,5,6,7,8,8,8,9,10]
target = int(input("Enter the target number: "))
count = 0
for x in nums:
    if x == target:
        count += 1
print(f"{target} appears & count {count} times")

# 7. List Slicing Logic
data = [10, 20, 30, 40, 50, 60]
print("First 3:", data[:3])
print("Last 3:", data[-3:])

# 8. Merge Two Lists
l1 = [1,2,3,4]
l2 = [5,6,7,8,9,10]
merged = l1 + l2
print("Merged: ",merged)

# 9. Tuple Unpacking
nums = (10,20,30)
x,y,z = nums
print(f"X:{x} Y:{y} Z:{z}")"""
# 10. Check Element in Tuple
"""fruits = ("apple", "banana", "cherry")
if "apple" in fruits:
    print("Apple is found")

# 🔹-------------------------------- Part 1: Basic Python (Variables, Operators, Input) -------------------------

 # Topics: Data Types, Variables, Input, Casting, Literals, Operators (No if-else).
 # 🟢 Easy (4 Problems)

# 1. Area of a Rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print("The area of rectangle: ",area,"cm")

# 2. Full Name Generator
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
full_name = first_name+" "+last_name
print("Full Name:",full_name)

# 3. Next Number Predictor
num = int(input("Enter the number: "))
print("The next number is:",num + 1)
# 4. Remainder Calculator
divisor = int(input("Enter the divisor: "))
divider = int(input("Enter the divider: "))
remainder = divider % divisor
print("The remainder:",remainder)

# ---------------------------🟡 Medium (3 Problems)---------------------

# 5. Days to Years, Weeks, Days
days = int(input("Enter the days: "))

years = days // 365
week = (days % 365) // 7
remaining_day = (days % 365) % 7
print(f"Years {years} weeks {week} & remaining_day: {remaining_day}")

# 6. Swap Without Third Variable
a = int(input("Enter the number of A: ")) # 5
b = int(input("Enter the number of B: ")) # 7

a = a + b
b = a - b
a = a - b
print(f"After swapping a:{a} & b:{b}")

# 7. Celsius to Fahrenheit
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit temperature is: ",fahrenheit,"F")

# ----------------------🔴 Hard (3 Problems)---------------------------

# 8. Sum of Digits (3-Digit Number)
nums = int(input("Enter the number: "))

digit_3 = nums % 10
digit_2 = (nums // 10) % 10
digit_1 = nums // 100
sum_digit = digit_3 + digit_2 + digit_1
print("Sum of Digits:",sum_digit)

# 9. Distance Between Coordinates
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance:", dist)

# 10. Last Digit Removal
nums = int(input("Enter the number: "))
last_digit_remove = nums // 10
print("Last Digit Removal:",last_digit_remove)

# 🔹-------------------------------- Part 2: Nested If-Else-----------------------

# Topics: Conditional logic inside another condition.
# 🟢 Easy (4 Problems)
# 1. Positive/Negative/Zero
num = int(input("Enter the number: "))
if num != 0:
    if num > 0:
        print("This is positive number")
    else:
        print("This is negative number")
else:
    print("This is Zero")

# 2. Voting Check (Age + ID)
age = int(input("Enter the age: "))
if age >= 18:
    has_id = input("Do you have id??(yes/no): ")
    if has_id == "yes":
        print("You can Vote now")
    else:
        print("Get ID card first")
else:
    print("You are not enough aged")

# 3. Smallest of Three Numbers

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a < b:
    if a < c:
        print(" a is the smallest number")
    else:
        print("Smallest number C")
else:
    if b < c:
        print("Smallest number B")
    else:
        print("Smallest number C")

# 4. Pass/Fail/Distinction

student_name = input("Enter the name: ")
marks = int(input("Enter the mark: "))
if marks >= 40:
    if marks >= 80:
        print("Distinction")
    else:
        print("Passed")
else:
    print("Failed")

# -------------------🟡 Medium (3 Problems)---------------------

# 5. Login System
user_name = input("Enter the username: ")
password = input("Enter the password: ")
if user_name == "admin12":
    if password == "12345":
        print("Login Successful!!")
    else:
        print("Incorrect Password")
else:
    print("Username not found")

# Logic of leap Year

# --------------------------🔹 Part 3: Loops (For & While)-----------------

# Topics: Iteration, Range, Logic inside loops.
# 2. Sum of First N Numbers

num = int(input("Enter the number: "))

if num > 1:
    is_prime = True
    for i in range(2,num):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime number")
    else:
        print(f"{num} is NOT a prime number")
else:
    print(f"{num} is NOT a prime number")

#------------------
num = int(input("Enter the number: "))
sum_N = 0
for i in range(1,num + 1):
    sum_N += i
print("The Sum Of N:",sum_N)

# 3. Print Multiplication Table
num = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{i} x {num} = {i * num}")

# 4. Count Digits (While)
n = int(input("Enter the number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Digits:",count)

# ---------------------------🟡 Medium (3 Problems)---------------------

# 5. Factorial Calculation
num = int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact *= i
print("Factorials:",fact)

# 6. Reverse a Number
num = int(input("Enter the number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10
print("Reversed Number: ",reverse)

# -------------------------------🔴 Hard (3 Problems)----------------------

# 8. Fibonacci Series
num = int(input("Enter the number: "))
n1 , n2 = 0,1
fabi = 0
if num <= 0:
    print("Invalid input please enter the number greater than Zero")
else:
    for i in range(num):
        print(fabi,end=" ")
        n1 = n2
        n2 = fabi
        fabi = n1 + n2

# 9. Check Palindrome Number
num = int(input("Enter the number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10
if temp == rev:
    print("This is palindrome")
else:
    print("This is not palindrome")

# ------------------------------🔄 Nested Loop Special (5 Problems)-------------

# 11. Square Pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
# 12. Right Triangle Pattern
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

# 13. Inverted Triangle
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# 14. Number Pyramid
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 15. Prime Numbers between 1 to 50
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
