#Level 1: Basic Functions (Beginner)
#1. Simple Greeting
#Write a function greet() that prints "Welcome to Python Functions".

def greet():
    print("Welcome the to new function part")
greet()
greet()

# 2. Function with Parameters
# Write a function sum_numbers(a, b) that takes two numbers and prints their sum.
def total(a,b):
    sum = a + b
    print("The sum of two numbers:",sum)
total(10,20)

# 3. Return Value
# Write a function multiply(a, b) that returns the product of two numbers.
def multiply(a,b):
    return  a*b
result = multiply(10,20)
print("The multiply of two numbers:",result)

#
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # 3^2 = 9
print(power(3, 3)) # 3^3 = 27

# 5. Even or Odd
# Write a function is_even(n) that returns True if a number is even, and False otherwise.
def is_even(n):
    return n % 2 == 0
result = is_even(10)
print(result)

# 6. Find Maximum
# Write a function find_max(a, b, c) that returns the largest of three numbers
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 50, 30))
# 7. List Summation
# Write a function sum_list(numbers) that takes a list and returns the sum of all elements.
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_list([1, 2, 3, 4, 5]))






















