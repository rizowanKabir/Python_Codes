# ----------------------------🟢 Level 1: Easy (4 Problems)---------------------

# Focus: Basic iteration, Syntax, and Accumulators.
# 1. Print Numbers 1 to N (While Loop)
# Logic: Basic structure of a while loop. Initialize, Condition, Increment.
num = int(input("Enter the number: "))
i = 1
while i <= num:
    print(i)
    i += 1

# 2. Sum of Natural Numbers (For Loop)
# Logic: Adding numbers cumulatively (1 + 2 + 3...).
num = int(input("Enter the number: "))
total = 0
for i in range(1,num + 1):
    total += i
print("The sum of ",num,"is",total)

# 3. Multiplication Table (For Loop)
# Logic: Iterating 10 times to multiply a number.
num = int(input("Enter the number: "))
print(f"Multiplication table of number {num}")
for i in range(1,11):
    result = num * i

    print(f"{num} x {i} = {result}")

# 4. Calculate Factorial (Loop Logic)

number = int(input("Enter the number: "))
factorial = 1
for i in range(1,number + 1):
    factorial *= i
    print("The factorial is: ",factorial)

# ------------🟡 Level 2: Medium (4 Problems)---------------

# Focus: Mathematical algorithms and Conditions inside loops.
# 5. Count Digits in a Number (While Loop)
# Logic: Keep dividing the number by 10 (// 10) until it becomes 0. Each division represents one digit removed.

num = int(input("Enter a large number: "))
count = 0

# If input is 0, it has 1 digit
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10  # Remove last digit
        count = count + 1

print("Total digits:", count)

# 6. Sum of Even Numbers Only (For + If)
# Logic: Iterate through a range and pick only even numbers to add.

limit = int(input("Enter the number please: "))
sum_even = 0
for i in range(1, limit + 1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers: ",sum_even)

# 7. Reverse a Number (While Loop - Classic Logic)
# Logic: Extract last digit -> Add to reversed variable multiplied by 10 -> Remove last digit.

num = int(input("Enter the number: "))
original_num = num
reversed_num = 0
while num > 0:
    last_digit = num % 10
    reversed_num = (reversed_num * 10) + last_digit
    num = num // 10
print("Original number: ",original_num)
print("Reversed number: ",reversed_num)

# 8. Check Prime Number (For Loop + Break)
# Logic: A prime number is only divisible by 1 and itself. We check if it is divisible by any number between 2 and (n-1).

num = int(input("Enter the number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("Its a prime number")
else:
    print("Its NOT a prime number")

# ------------------🔴 Level 3: Hard (2 Problems)----------------

# Focus: Nested Loops and Series Logic.
# 9. The Fibonacci Series
# Logic: A sequence where the next number is the sum of the previous two (0, 1, 1, 2, 3, 5, 8...).

num = int(input("Enter the any number: "))
a = 0
b = 1
count = 0
if num <= 0:
    print("Please enter the number greater than Zero")
else:
    for i in range(1,num):
        print(count,end=" ")
        a = b
        b = count
        count = a + b
print('Thank you')
# 10. Right-Angled Triangle Pattern (Nested For Loop)
# Logic: The outer loop controls the rows, the inner loop controls the columns (stars).
rows = int(input("Enter number of rows: "))

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for printing stars
    for j in range(i):
        print("*", end="")
    print()
























