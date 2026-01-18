# 1. Palindrome Checker
# Write a function that checks if a string is a palindrome, ignoring spaces and capitalization.
def is_palindrome(s):
    is_clean = "".join(s.lower().split())
    return is_clean == is_clean[::-1]
result = is_palindrome("Go hang a salami I m a lasagna hog")
print("This is palindrome or not then tell me True or False: ",result)

# 2. Anagram Checker
# Write a function that takes two strings and returns True if they are anagrams.
def an_anargrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
result = an_anargrams("Listen", "silent")
print(result)

# Problem 1: Hello World & Basic Output
# Problem: Write a program that prints your name, age, and favorite hobby on separate lines.
print("Name: Rizowan Kabir")
print("Age:",25)
print("Favorite hobby: Programming")

# Problem 2: Basic Input and Output
# Problem: Take user's name and age as input, then print a greeting message.
name = input("Enter the name please:")
age = int(input("Enter the age:"))
print(f"Hello {name}, Now you are {age} years old")

# Problem 3: Data Types Identification
# Problem: Create variables of different data types and print their types.
num = 42
print(f"{num} is of type {type(num)}")

pi = 3.1416
print(f"{pi} is of type {type(pi)}")

name = "Python"
print(f"{name} is of type {type(name)}")
is_valid = True
print(f"{is_valid} is of type {type(is_valid)}")

List = ["apple", "banana"]
print(f"{list} is of type {type(List)}")

Tuple = ("hello", "How", )
print(f"{Tuple} is of type {type(Tuple)}")

# Problem 4: Comments Practice
# Problem: Write a program with single-line and multi-line comments explaining what the code does.

length = float(input("Enter the number of length:"))
width = float(input("Enter the number of width:"))

area = length * width
print(f"The area of rectangle is {area} cm")

# Problem 5: String Concatenation and Formatting
# Problem: Take first name and last name as input, then display full name using different methods.

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

#method 1
full_name_1 = first_name+" "+last_name
print(full_name_1)
#method 2
full_name_2 = f"{first_name} {last_name}"
print(full_name_2)

full_name_3 = "{} {}".format(first_name, last_name)
print(full_name_3)

#method 4
full_name_4 = " ".join([first_name, last_name])
print(full_name_4)

# Problem 6: Type Conversion - String to Number
# Problem: Take two numbers as string input, convert them to integers, and find their sum.

first_number = input("Enter the number: ")
second_number = input("Enter the number: ")

f_num = int(first_number)
s_num = int(second_number)
total = f_num + s_num
print(f"The type of number {total} & {type(total)}")

# Problem 7: Type Conversion - Multiple Types
# Problem: Demonstrate conversion between int, float, and string.
num_int = 10
num_float = float(num_int)
print(f"Integer: {num_int} & Float: {num_float}")
num_float = 99.33
num_int = int(num_float)
print(f"Float: {num_float} & Integer: {num_int}")

num_int = 25
num_str = str(num_int)
print(f"Integer: {num_int} & string: {num_str} {type(num_str)}")

height_str = "5.9"
height_float = float(height_str)
print(f"string {height_str} & float{height_float} {type(height_float)}")

is_active = True
active_int = int(is_active)
print(f"active {is_active} & active int {active_int} {type(active_int)}")

# Problem 8: Implicit vs Explicit Type Conversion
# Problem: Show the difference between implicit and explicit type conversion.
# Implicit type conversion (automatic)
num_int = 10
num_float = 5.5

# Python automatically converts int to float
result = num_int + num_float
print(f"Implicit: {num_int} + {num_float} = {result} (type: {type(result)})")
decimal = 100
print(f"Decimal: {decimal}")

# Binary (base 2) - prefix 0b
binary = 0b1010  # equals 10 in decimal
print(f"Binary 0b1010: {binary}")

# Octal (base 8) - prefix 0o
octal = 0o17  # equals 15 in decimal
print(f"Octal 0o17: {octal}")

# Hexadecimal (base 16) - prefix 0x
hexadecimal = 0xFF  # equals 255 in decimal
print(f"Hexadecimal 0xFF: {hexadecimal}")

# Float with exponential notation
scientific = 1.5e3  # equals 1500.0
print(f"Scientific 1.5e3: {scientific}")

# Complex numbers
complex_num = 3 + 4j
print(f"Complex: {complex_num}")

# Problem 10: String Literals and Escape Sequences
# Problem: Demonstrate various string literals and escape sequences.
str_1 = 'Hello World'
print(str_1)
str_2 = "Python is implicit language"
print(str_2)

#Escape sequence
print("line 1\nline 2")
print("column1\tcolumn2")

# Problem 11: Arithmetic Operators
# Problem: Create a basic calculator using all arithmetic operators.
num_1 = float(input("Enter the number please: "))
num_2 = float(input("Enter the number please: "))

print(f"f\nArithmetic operations on {num_1} & {num_2}")
print(f"Addition: {num_1} + {num_2} = {num_1 + num_2}")
print(f"Subtraction: {num_1} - {num_2} = {num_1 - num_2}")
print(f"Multiplication: {num_1} * {num_2} = {num_1 * num_2}")
print(f"Division: {num_1} / {num_2} = {num_1 / num_2}")
print(f"floor division: {num_1} // {num_2} = {num_1 // num_2}")
print(f"Module: {num_1} % {num_2} = {num_1 % num_2}")
print(f"Exponential: {num_1} ** {num_2} = {num_1 ** num_2}")

# Problem 12: Comparison Operators
# Problem: Compare two numbers and display all comparison results.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Comparison between two number {a} & {b}")
print(f"{a} == {b} : {a == b}") # Equal to
print(f"{a} != {b} : {a != b}") # Not equal to
print(f"{a} > {b} : {a > b}") # Greater than
print(f"{a} < {b} : {a < b}") # Less than
print(f"{a} >= {b} : {a >= b}") # Greater than equal
print(f"{a} <= {b} : {a <= b}") # Less than equal

# Problem 13: Logical Operators
# Problem: Check if a number is within a range using logical operators.
number = int(input("Enter the number: "))
lower_bound = 10
upper_bound = 50

is_range = number >= lower_bound and number <= upper_bound
print(f"{number} between lower bound & upper bound: {is_range}")
is_boundary = number == lower_bound or number == upper_bound
print(f"{number} boundary is: {is_boundary}")

valid = (number > 0) and (number < 100) and (number % 2 == 0)
print(f"{number} is even & positive")

# Problem 14: Assignment Operators
# Problem: Demonstrate all assignment operators.
x = 10
print(f"Initial Value: X = {x}")
x += 5
print(f"After X = {x}")
x -= 10
print(x)
x *= 5
print(x)
x /= 10
print(x)
x %= 5
print(x)
x //= 20
print(x)

# Problem 15: Operator Precedence
# Problem: Demonstrate operator precedence with examples.
result1 = 10 + 5 * 2
print(f"10 + 5 * 2 = {result1}")  # Multiplication first

# Expression 2: Using parentheses
result2 = (10 + 5) * 2
print(f"(10 + 5) * 2 = {result2}")  # Parentheses first

# Expression 3: Complex expression
result3 = 2 + 3 * 4 ** 2 / 2 - 1
print(f"2 + 3 * 4 ** 2 / 2 - 1 = {result3}")
# Order: 4**2 = 16, 3*16 = 48, 48/2 = 24, 2+24 = 26, 26-1 = 25

# Expression 4: Comparison and logical
a, b, c = 5, 10, 15
result4 = a < b and b < c
print(f"{a} < {b} and {b} < {c} = {result4}")

# Expression 5: Mixed operators
x = 10
result5 = x + 5 > 12 and x * 2 < 25
print(f"x + 5 > 12 and x * 2 < 25 (where x={x}) = {result5}")




















