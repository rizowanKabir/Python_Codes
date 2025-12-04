# 1. The ID Card Generator
# Concepts: String concatenation, Type Conversion, Input.
# Logic: Combining string literals with user input to create a formatted string.
name = input("Enter the name here: ")
current_year = int(input("Enter the current years please: "))
birth_day_year = int(input("Enter the birth year please: "))
age = current_year - birth_day_year

print(f"ID CARD: {name} | Age: {age} ")

# 2. Currency Converter (USD to Local)
# Concepts: Float Literals, Arithmetic Operators, Variables.
# Logic: Multiplying input by a constant exchange rate.
exchange_rate = float(input("Enter the rate of exchange: "))
usd_amount = float(input("Enter the usd amount here: "))

local_currency = usd_amount * exchange_rate
print("The local Currency in BDT:",local_currency, "TK")

# 3. Area of a Triangle
# Concepts: Float data type, Arithmetic Operators, Literals.
# Logic: Using the formula
base = float(input("Enter the number: "))
height = float(input("Enter the height number: "))
area = 0.5 * base * height # 0.5 is literal here
print("The Area of Triangle: ",area)

# 4. Grocery Bill with Tax
# Concepts: Identifiers (variable naming), Type Conversion, Percentage Logic.
# Logic: Calculating tax percentage and adding it to the total.

price = float(input("Enter the price please: "))
tax_rate = 0.15   # this is literal values
tax_amount = price * tax_rate

final_price = price + tax_amount
print(f"The tax amount is: {tax_amount} TK")
print(f"The final price is: {final_price} TK")

# 5. String Multiplier (The "Echo" Effect)
# Concepts: String Operators (*), Input.
# Logic: In Python, you can multiply a string by an integer to repeat it.
word = input("Enter the input echo word: ")
time = int(input("Enter the time please: "))
# Logic building here
echo = word * time
print("Result is: ",echo)

# 6. Steps Counter (Compound Assignment)
# Concepts: Assignment Operators (+=), Integer Data Type.
# Logic: Updating a variable's value without creating a new variable.
steps = 0
morning_walk = int(input("Enter the morning walk steps: "))
steps += morning_walk
evening_walk = int(input("Enter the steps of evening walk: "))
steps += evening_walk
print("The total steps of both of them(morning & evening): ", steps,"meters")

# 7. Logical Comparison (Voting Eligibility)
# Concepts: Boolean Data Type, Comparison Operators (>=).
# Logic: Returning True or False based on a condition.
age = int(input("Enter the age please: "))
can_vote = age >= 18
print("Eligible for vote", can_vote)
# 8. Digits Extraction (Middle Digit)
# Concepts: Floor Division (//), Modulus (%).
# Logic: How to extract the middle digit of a 3-digit number (e.g., input 123 -> output 2).

number = int(input("Enter the 3 digit number: "))
first_two = number // 10
middle_digit = first_two % 10
print("The middle digit is: ",middle_digit)
# 9. Type Checker
# Concepts: type() function, Comments.
# Logic: Understanding how Python treats different inputs.
data_1 = input("Enter the input here: ")
data_2 = int(input("Enter the input here: "))
data_3 = float(input("Enter the input here: "))
# Type checker
print("The type of data data_1: ",type(data_1))
print("The type of data data_2: ",type(data_2))
print("The type of data data_3: ",type(data_3))

# 10. Complex Interest Logic (Exponent Operator)
# Concepts: Exponentiation Operator (**), Operator Precedence.
# Logic: Calculating Compound Interest Formula:
P = float(input("Principal Amount: "))
r = 0.05 # 5% Interest rate (Literal)
t = int(input("Time (years): "))

# Logic: ** is the Power operator
amount = P * (1 + r) ** t

print("Total Amount after", t, "years:", amount)

# Here are 10 unique Logic Building Codes in English, specifically designed using Data Types, Variables, Input, Type Conversion, Literals, and Operators.
# These examples focus on mathematical and boolean logic without using if-else or loops.
# 1. BMI Calculator (Body Mass Index)
# Concept: Exponent Operator (**), Float Conversion, Order of Operations.
weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in meters: "))
bmi = weight / (height ** 2)
print("The body mass if bmi is:",bmi)

# 2. Volume of a Cylinder
# Concept: Constants (Literals), Arithmetic Operators.
radius = float(input("Enter the radius here: "))
height = int(input("Enter the height here: "))
pi = 3.1416
base_area = pi * (radius ** 2)
volume = base_area * height
print("The Volume of a cylinder: ",volume)

# 3. Shopping Budget (Floor Division)
# Concept: Floor Division (//), Type Conversion.
# Logic: Calculate the maximum number of items one can buy with a fixed budget (ignoring decimal parts).
budget = float(input("Enter the budget here: "))
items_price = float(input("Enter the items price here: "))

total_item = budget // items_price
change_left = budget % items_price
print("You can buy",items_price, "item")
print("Change left is: ",change_left)
# 4. Simple Interest Calculator
# Concept: Percentage Logic, Operator Precedence.
principle = float(input("Enter the principle here please: "))
rate = float(input("Enter the annual interest here: "))
time = int(input("Enter the time (in years): "))

interest_calculate = (principle * rate * time) / 100
total_amount = principle + interest_calculate
print("The total annual interest is: ",interest_calculate)
print("The total amount you to pay: ",total_amount)

# 5. String Repeater (Design Pattern)
# Concept: String Operators (*), Literals.
# Logic: In Python, multiplying a string by an integer repeats it.

symbol = input("Enter these symbol(! @ # $ % & *): ")
count = int(input("How long should line be?: "))
line = symbol * count
print("Here is year pattern: ")
print(line)
# 6. Clock Math (Modulo Operator)
# Concept: Modulo (%), Addition.
# Logic: If it is 9 o'clock, what time will it be after 5 hours? (12-hour format).
current_time = int(input("Enter the current time here(1-12): "))
hours_later = int(input("Enter the hours (1-12): "))
future_time = ((current_time + hours_later - 1) % 12) + 1
print("-----Welcome to the Future Time-------")
print(future_time)

# 7. Logical "AND" Gate (Authentication)
# Concept: Boolean Data Type, Logical Operators (and), Comparison Operators (==).
# Logic: Verification succeeds only if both username and PIN are correct.
db_user = "admin12"
db_password = 12345

user = input("Enter the username please: ")
password = int(input("Enter the password please: "))

is_authenticated = (db_user == user) and (db_password == password)
print("Login Successful !!", is_authenticated)

# 8. Convert Feet to Inches and Centimeters
# Concept: Multiple arithmetic operations.
# Logic: 1 Foot = 12 Inches, 1 Inch = 2.54 cm.
feet = float(input("Enter length in Feet: "))

inches = feet * 12
centimeters = inches * 2.54

print(str(feet) + " feet is equal to:")
print(inches, "Inches")
print(centimeters, "Centimeters")

# 9. Profit or Loss Calculation
# Concept: Subtraction, Variables.
# Logic: Profit = Selling Price - Cost Price.
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

profit = selling_price - cost_price
print("The Net profit(positive) or loss(negative)", profit, "TK")






























