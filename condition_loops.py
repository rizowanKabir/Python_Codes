# if / elif / else  statement condition
# Problem: Write a program that takes an integer as input and prints whether it's "Even" or "Odd."

number = int(input("Enter the number please: "))

if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")

# Problem: Get a number from the user and determine if it's positive, negative, or zero.
number = int(input("Enter the number: "))

if number > 0:
    print(f"{number} is Positive number")
elif number < 0:
    print(f"{number} is Negative number")
else:
    print(f"{number} is Zero")

# Problem: Take two numbers as input and print the larger one.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"This number is larger {num1}")
else:
    print(f"This is number is larger {num2}")

# Problem: Ask the user for a year and check if it's a leap year. (A leap year is divisible by 4, but not by 100 unless it's also divisible by 400).
year = int(input("Enter the year please: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# loops concepts
# Problem: Get an integer N from the user and calculate the sum of all numbers from 1 to N.
number = int(input("Enter the number: "))

total_sum = 0
for i in range(1,number+1):
    total_sum += i
print(f"The sum of all number 1 to {number} & the sum is: {total_sum}")

# Problem: Take a number from the user and print its multiplication table up to 10.

num = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{i} x {num} = {i * num}")

# Problem: Get a non-negative integer from the user and calculate its factorial. (Factorial of 0 is 1).

num = int(input("Enter the number please: "))

factorial = 1
if num < 0:
    print("Factorial is not defined for negative number")
elif num == 0:
    print("For factorial number 0 is 1(Please input given 1)")
else:
    for i in range(1,num+1):
        factorial *= i
    print(f"The factorial is: {factorial}")

# Problem: Ask the user for a number N and print a countdown from N to 1.

num = int(input("Enter the number: "))

while num >= 1:
    print(num)
    num -= 1 # This part is most important
# Problem: Ask the user for their name and then print a personalized greeting like "Hello, [Name]!"

name = input("Enter the name here: ")
print("Hello Mr",name ,"Bokachoda")

# Problem: Take two numbers and an operator (+, -, *, /) as input from the user and perform the calculation.

num1 = float(input("Enter the first number: "))
operator = input("Enter the operators (+,-,*,/): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    print(f"The result is: {num1 + num2}")
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 + num2)
else:
    print("Invalid operator")

# Problem: Get the length and width of a rectangle from the user and calculate its area.

length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

area = length * width
print(f"The area of the rectangle is: {area:.2f} cm")

# Problem: Ask the user for their age in years and estimate their age in days (assume 365 days/year).

age_years = int(input("Enter your age in years: "))
age = int(input("Enter your age: "))
age_days = age_years * 365

print("You are approximately", age_days, "days old.")

# Problem: Get temperature in Celsius from the user and convert it to Fahrenheit. (F = C * 9/5 + 32)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Problem: Ask the user for a word and print its length.

word = input("Enter the word please: ")
print(f"The length of word is: {len(word)}")

# Problem: Get two strings from the user and print them concatenated.
word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word: ")

print(f"The concatenation is: {word_1 + word_2}")

# Problem: Take a string as input and print its reverse.
# Problem: Get a string from the user and check if it's a palindrome (reads the same forwards and backwards).

text = input("Enter the word please: ")

if text == text[::-1]:
    print(f"{text} this is palindrome")
else:
    print(f"{text} this is not palindrome")

# Problem: Take a string as input and count the number of vowels (a, e, i, o, u) in it.
text = input("Enter the word please: ")
vowels = "aeiou"
counter = 0
for char in text:
    if char in vowels:
        counter += 1
print(f"Number of vowels is: {counter}")




