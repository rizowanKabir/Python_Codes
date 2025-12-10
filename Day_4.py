
# 1. The Bio-data Generator (String Concatenation)
# Logic: Taking string inputs and combining them into a sentence.
"""name = input("Enter the name please: ")
age = int(input("Enter the age: "))
print("Hi mr",name,"Welcome to our world & you are",age,"years old now")"""

# 2. The Remainder Finder (Modulo Operator)
# Logic: If you have 50 apples and 3 friends, how many are left after dividing equally?
"""total_apple = 50
friends = 3

remaining_apple = total_apple % friends
print("The left apple over:",remaining_apple)"""

# 3. Perimeter of a Rectangle (Formula)
# Logic: Applying the math formula 2 * (length + width)
"""length = float(input("Enter the number of length: "))
width = float(input("Enter the number of width: "))

perimeter = 2 * (length + width)
print("The perimeter of a Rectangle is: ",perimeter)"""

# 4. String vs Integer Addition (Type Conversion)
# Logic: Understanding the difference between text 10 and number 10.
"""num_1 = input("Enter the number is: ")
num_2 = input("Enter the number is: ")
print("Result is string: ",num_1 + num_2)
print("The result in integer: ",int(num_1) + int(num_2))"""

# 5. Cube Calculator (Exponent Operator)
# Logic: Finding the power of a number.
"""side = int(input("Enter the number of side: "))
cube = side ** 3
print("The cube calculater is: ",cube)"""

# -----------------🟡 Level 2: Medium (3 Problems)--------------
# Focus: Logic using multiple operators and steps.
# 6. Seconds to Minutes Converter
# Logic: Converting total seconds into "Minutes" and "Remaining Seconds" using // and %.
"""total_second = int(input("Enter the second: "))
minutes = total_second // 60  # Total minutes
remaining_second = total_second % 60 # Remaining Second
print("The",minutes,"Minutes and",remaining_second,"seconds")"""

# 7. Variable Swapping (The Python Way)
# Logic: Swapping values between two variables without a third variable.
"""a = int(input("Enter the number:"))
b = int(input("Enter the number: "))
print(f"Before a={a} and b={b}")
# build a logic
a, b = b, a
print(f"After a={a} and b={b}")"""
# 8. Average Speed Calculator
# Logic: Speed=Distance/Time
"""distance = int(input("Enter the distance: "))
time_hr = int(input("Enter the time: "))
speed = distance / time_hr
print("Average speed is: ",speed,"km/h")"""
# ------------🔴 Level 3: Hard (2 Problems)--------------

# Focus: Mathematical algorithms and pure logic building.
# 9. Sum of Digits (3-Digit Number)
# Logic: If input is 456, calculate 4+5+6 = 15 using math only.
"""number = int(input("Enter the three digit number: "))

digit_3 = number % 10
temp = number // 10
digit_2 = temp % 10
digit_1 = temp //10
total_sum = digit_1 + digit_2 + digit_3
print("The total sum: ",total_sum)"""

# 10. ATM Cash Breakdown (Currency Logic)
# Logic: Calculate how many 1000, 500, and 100 notes make up a total amount.
"""amount = int(input("Enter amount to withdraw (e.g., 2600): "))

# How many 1000 notes?
note_1000 = amount // 1000
remaining = amount % 1000 # Balance remaining

# How many 500 notes from the remaining?
note_500 = remaining // 500
remaining = remaining % 500 # Balance remaining

# How many 100 notes from the remaining?
note_100 = remaining // 100
remaining = remaining % 100 # Change left

print("1000 Notes:", note_1000)
print("500 Notes:", note_500)
print("100 Notes:", note_100)
print("Change left:", remaining)"""

#-------------🟢 Level 1: Easy (5 Problems)-----------------

#Focus: Basic if and else with simple comparison operators.
#1. Odd or Even Number
#Logic: A number is even if it is divisible by 2 (Remainder is 0).
"""number = int(input("Enter the number: "))
if number == 0:
    print("This number is not right input")
elif number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")"""

# 2. Positive, Negative, or Zero
# Logic: Using elif to handle three possible states of a number.
"""number = int(input("Enter the number: "))

if number > 0:
    print("This is positive number")
elif number < 0:
    print("This is Negative number")
else:
    print("This is Zero")"""

# 3. Voting Eligibility
# Logic: Simple age comparison.
"""age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are too young to vote.")"""

# 4. Minimum of Two Numbers
# Logic: Comparing two values to find the smaller one.
"""num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 < num2:
    print("Smallest number is:", num1)
else:
    print("Smallest number is:", num2)"""
# 5. Divisibility Check
# Logic: Check if a number is divisible by both 5 AND 11.
"""num = int(input("Enter the number: "))
if num % 5 == 0 and num % 11 == 0:
    print("divisible by both 5 & 11")
else:
    print("Not divisible by both 5 & 11")"""

# -------------------🟡 Level 2: Medium (3 Problems)---------------------

# Focus: Multiple conditions (elif), Logical Operators (and, or), and Ranges.
# 6. Student Grading System
# Logic: Checking ranges of numbers to assign a grade.
"""student_name = input("Enter the student name: ")
marks = int(input("Enter the marks between(0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"
print(f"{student_name} you got {grade}")"""
# 7. Greatest of Three Numbers
# Logic: Finding the maximum among three numbers using and.
"""num_1 = int(input("Enter the number first number: "))
num_2 = int(input("Enter the number second number: "))
num_3 = int(input("Enter the number third number: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"num_1:{num_1} is the largest number")
elif num_2 > num_1 and num_2 > num_3:
    print(f"num_2: {num_2}is the largest number")
else:
    print(f"num_3: {num_3} is the largest number")"""
# 8. Vowel or Consonant Checker
# Logic: Checking if a character exists in a list of vowels.
"""char = input("Enter a letter: ").lower()

if len(char) == 1:
    if char in "aeiou":
        print("This is vowel")
    else:
        print("This is consonant")
else:
    print("Please enter only one letter")"""

# -----------------------------🔴 Level 3: Hard (2 Problems)----------------------

# Focus: Complex logic, Nested conditions, and Algorithm building.
# 9. Leap Year Calculator (The Full Logic)

"""year = int(input("Enter the year please: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"this is leap year")
else:
    print(year," is not leap year")"""
# 10. Electricity Bill Calculator (Tiered Logic)
# Logic: Calculating bill based on slabs.
# First 100 units: $5 per unit
# Next 100 units (101-200): $10 per unit
# Above 200 units: $15 per unit

"""units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    # First 100 units * 5 + Remaining units * 10
    bill = (100 * 5) + ((units - 100) * 10)
else:
    # First 100 * 5 + Next 100 * 10 + Remaining * 15
    bill = (100 * 5) + (100 * 10) + ((units - 200) * 15)

print("Total Electricity Bill: $", bill)"""

"""unit = int(input("Enter the units consumed: "))
bill = 0
if unit <= 100:
    bill = unit * 5
elif unit <= 200:
    bill = unit * 5 + ((unit - 100) * 10)
else:
    bill = unit * 5 + unit * 10 + ((unit - 200) * 15)
print("Total Electricity bill is: ",bill)"""


































