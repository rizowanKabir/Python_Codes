# Basic logic: Taking input, converting it to an integer, and adding them.

# Take input to user
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
# Result
result = num_1 + num_2
print(f"The result of them is: {result}")

# 2. Area of Rectangle
# Converting a mathematical formula into code.
length = float(input("Enter the length please: "))
width = float(input("Enter the width please: "))
area = length * width
print(f"The Area Of Rectangle: {area} Cm")
# 3. Calculate Age
# Logic: Subtracting the birth year from the current year.
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter the birth year: "))
age = current_year - birth_year
print(f"Your current age is: {age} Years")

# 4. Calculate Average
# Logic: Summing multiple numbers and dividing by the count.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
average = (a + b + c) / 3
print("The average is:", average)

# 5. Swap Variables (Using Temp)
# Logic: Swapping contents of two variables using a third temporary variable.
a = 10
b = 20
temp = a
a = b
b = temp
print("The value of a is:",a)
print("The value of b is:",b)

# 6. Quotient and Remainder
# Understanding Floor Division (//) and Modulus (%). This is crucial for logic building.
number = int(input("Enter the number: "))
divisor = int(input("Enter the divisor:" ))
quotient = number // divisor # Gives the integer result
remainder = number % divisor # Gives what is left over
print("The Quotient is: ", quotient)
print("The Remainder is: ", remainder)

# 7. Find the Last Digit
# Logic Trick: Any number modulo 10 (% 10) gives the last digit of that number.
number = int(input("Enter the any large number: "))
last_digit = number % 10
print("The last digit of number is: ",last_digit)

# 8. Celsius to Fahrenheit
# Applying a standard conversion formula.
celsius = int(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in fahrenheit is: ",fahrenheit , "°F")

# 9. Convert Days to Seconds
# Multiplication logic.
day = int(input("Enter the day please: "))
# 24 * 60 * 60
seconds = day * 24 * 60 * 60
print(f"The day-{day} equal to seconds is: {seconds} S")

# 10. Shopping Bill Calculator
# Simple arithmetic logic.
price = float(input("Enter the price per item: "))
quantity = int(input("Enter the quantity how many item you have?: "))
total_bill = price * quantity
print("The total bill is: ",total_bill,"TK")

# 11. Check if Number is Even (True/False)
# Using comparison operators without if-else.
number = int(input("Enter the number: "))
if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")

# 12. Swap Without Third Variable
# Advanced Logic: Using math to swap values.
x = 5
y = 10
x = x + y
y = x - y
x = x - y
print("x:",x ,"y:", y)
# 13. Circumference of a Circle
# Using float variables and constants.(2 * pi * r)
radius = float(input("Enter the radius: "))
pi = 3.1416
circumference = 2 * pi * radius
print(f"The Circumference of a circle is: {circumference:.2f}")
# 14. Using Power operators

base = int(input("Enter base number: "))
power = int(input("Enter power: "))

result = base ** power

print("Result:", result)

#15. Convert Seconds to Hours, Minutes, Seconds
# Best for Logic Building: Converting a raw number into a readable format using division and modulus.
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600            # 3600 seconds in 1 hour
remaining_seconds = total_seconds % 3600 # What's left after taking out hours
minutes = remaining_seconds // 60        # 60 seconds in 1 minute
seconds = remaining_seconds % 60         # Remaining seconds

print(f"Time: {hours} Hours, {minutes} Minutes, {seconds} Seconds")































