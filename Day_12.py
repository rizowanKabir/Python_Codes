# Problem 16: Simple If-Else
# Problem: Check if a number is positive or negative.
"""number = int(input("Enter the number: "))

if number > 0:
    print(f"{number} this is positive number")
elif number < 0:
    print(f"{number} this is negative number")
else:
    print(f"{number} this is Zero")"""

# Problem 17: Grade Calculator
# Problem: Calculate letter grade based on percentage.
"""percentage = float(input("Enter the percentage: "))
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Failed"
print(f"Your grade is {grade} &")
if grade in ['A+','A']:
    print("Excellent Work")
elif grade in ['B','C']:
    print("Good Job")
elif grade in ['D']:
    print("Passes. But need more improvement")
else:
    print("Failed.Try again later")"""

# Problem 18: Leap Year Checker
# Problem: Check if a given year is a leap year.
"""year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} this is leap year")
else:
    print(f"{year} this is not leap year")"""
# Problem 19: Even/Odd and Multiple Checker
# Problem: Check if a number is even/odd and if it's a multiple of 5.
"""number = int(input("Enter the number: "))
if number % 2 == 0:
    print(f"{number} this is even number")
else:
    print(f"{number} this is odd number")

if number % 5 == 0:
    print(f"{number} this is multiply by 5")
else:
    print(f"{number} this is not multiply by 5")
if number % 2 == 0 and number % 5 == 0:
    print(f"{number} this is divisible by both of 2 and 5")"""

# Problem 20: Largest of Three Numbers
# Problem: Find the largest among three numbers.
"""num1 = float(input("Enter the number_1: "))
num2 = float(input("Enter the number_2: "))
num3 = float(input("Enter the number_3: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")
print(f"The largest number is {max(num1,num2,num3)}")"""

# Problem 21: Print Numbers 1 to N
# Problem: Print all numbers from 1 to n using a for loop.
"""n = int(input("Enter the number: "))
print(f"Numbers from 1 to {n}")
for i in range(1, n+1):
    print(i, end=" ")
print()"""

# Problem 22: Sum of Natural Numbers
# Problem: Calculate the sum of first n natural numbers.
"""n = int(input("Enter the number: "))
total = 0
for i in range(1,n+1):
    total += i
print(f"The sum of frist {n} natural numbers {total}")

formula_result = n * (n + 1) // 2
print(f"The formula result is {formula_result}")"""

# Problem 23: Multiplication Table
# Problem: Print the multiplication table for a given number.
"""num = int(input("Enter the number: "))
print(f"\nMultiplication table for a given number {num}")
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")"""

# Problem 24: Factorial Calculator
# Problem: Calculate factorial of a number using for loop.
"""n = int(input("Enter the number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}")"""

# Problem 25: Pattern Printing
# Problem: Print various patterns using nested for loops.
# Pattern 1: Right-angled Triangle
"""n = int(input("Enter the row number: "))
for i in range(1, n+1):
    for j in range(i):
        print("*",end=" ")
    print()
print("Another One")
# Pattern 2: Inverted Triangle
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
print("Next Another One")
# Pattern 3: Number Pyramid
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()"""

# Problem 26: Count Digits in a Number
# Problem: Count the number of digits in a given number using while loop.
"""number = int(input("Enter the number: "))
original = number
count = 0
if number < 0:
    number = -number
if number == 0:
    count = 1
else:
    while number > 0:
        count += 1
        number = number // 10
print(f"Number of digit in {original} : {count}")"""

# Problem 27: Reverse a Number
# Problem: Reverse the digits of a number using while loop.
"""number = int(input("Enter the number: "))
original = number
reversed_num = 0
is_negative = number < 0
if is_negative:
    number = -number
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10
if is_negative:
    reversed_num = -reversed_num
print(f"original number: {original}")
print(f"reversed number: {reversed_num}")"""

# Problem 28: Sum of Digits
# Problem: Calculate the sum of digits of a number.
"""number = int(input("Enter the number: "))
original = number
digit_sum = 0

if number < 0:
    number = -number
while number > 0:
    digit = number % 10
    digit_sum += digit
    number = number //10
print(f"Sum of the digit of number {original}: {digit_sum}")"""

# Problem 29: Guess the Number Game
# Problem: Create a number guessing game using while loop.
"""import random

secret_number = random.randint(1,100)
attempts = 0
max_attempts = 7

print("Welcome to the number of guessing game")
print("I am thinking of a number between 1 to 100")
print(f"You have {max_attempts} attempts to guess it")

while attempts < max_attempts:
    guess = int(input("\nEnter the guessing number: "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations ! you guessed it {attempts} attempts")
        break
    elif guess < secret_number:
        print("Too low.Try bigger")
    else:
        print("Too high try lower")
    print(f"Attempts remaining {max_attempts - attempts}")
else:
    print(f"\nGame over & your secret number was {secret_number}")"""

# Problem 30: Fibonacci Series
# Problem: Generate Fibonacci series up to n terms using while loop.
"""n = int(input("Enter number of terms: "))

# First two terms
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print(f"Fibonacci series: {a}")
else:
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        # Update values
        a, b = b, a + b
        count += 1
    print()

# Alternative: Store in list
fib_list = []
a, b = 0, 1
count = 0
while count < n:
    fib_list.append(a)
    a, b = b, a + b
    count += 1
print(f"Fibonacci list: {fib_list}")"""

# Bonus Problem: Simple ATM System
# Problem: Create a simple ATM system combining all concepts learned.
"""print("=" * 40)
print("      Welcome to the python ATM")
print("=" * 40)

balance = 1000
pin = "12345"
attempts = 0
max_attempts = 4
while max_attempts > attempts:
    entered_pin = input("\nEnter your PIN: ")
    if entered_pin == pin:
        print("PIN verified successfully")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN {remaining} attempts remaining")
        else:
            print("Too many incorrect pin. card blocked")
            exit()
while True:
    print("\n" + "=" * 40)
    print("Python ATM")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Balance")
    print("3. Withdraw balance")
    print("4. Exit")
    choice = input("/Enter your choice between(1 - 4): ")
    if choice == "1":
        print(f"Your current balance is {balance:.2f}")
    elif choice == "2":
        amount = float(input("\nEnter the amount to deposit"))
        if amount > 0:
            print(f"{amount:.2f} amount added successfully")
            print(f"Your current balance is {balance:.2f} TK")
        else:
            print("Invalid Amount")
    elif choice == "3":
        amount = float(input("Enter the balance to withdraw" ))
        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"{amount:.2f} TK Balance withdraw successfully ")
            print(f"remaining Balance is {balance:.2f}")
    elif choice == "4":
        print("\nThank you for using Python ATM!")
        print("Have a great day!")
        break
    else:
        print("Invalid Choice.Try to give between 1 to 4")"""


# Prime Number Checker Programs
number = int(input("Enter the number: "))

if number <= 1:
    print(f"{number} is not a prime number")
elif number == 2:
    print(f"{number} is a prime number")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")




































