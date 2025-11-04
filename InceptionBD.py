# Write a program that takes the current temperature as input and prints

temperature = int(input("Enter the current temperature: "))

if temperature <= 10 :
  print("Its too cold!")
elif 10 < temperature < 25:
  print("Its too clod Outside!!")
elif temperature > 25:
  print("Its too hot outside!!!")
else:
  print("Invalid input.")

# Ask the user for their account balance and the amount they want to withdraw.
balance = 1000
print(f"Main balance is: {balance}")
withdraw = int(input("Enter the amount (you can check & withdraw): "))

if balance < withdraw:
  print("Insufficient Balance!!!")
elif balance >= withdraw:
  print("Transaction Successful !!")
else:
  print("Thank you")
# Student Grade Calculator (Input marks (0–100) and print grade based on)

Student = input("Enter the name please: ")
mark = int(input("Enter the mark please: "))

if 90 <= mark <= 100:
  grade = "A+"
elif 80 <= mark <=89:
  grade = "A"
elif 70 <= mark <= 79:
  grade = "B"
elif 60 <= mark <= 69:
  grade = "c"
else:
  grade = "Fail"
print(f"{Student} your result is: {grade} & your mark is: {mark}")

#Bus Ticket Discount(Ask the user for age and print ticket price)

passenger = input("Enter the name please: ")
age = int(input("Enter your age: "))

# Check the age and determine the ticket price
if age < 5:
    print("Ticket is Free!")
elif 5 <= age <= 18:
    print("You get a 50% Discount.")
elif age >= 60:
    print("You get a 30% Discount.")
else:
    print("You need to pay the Full Price.")

# Restaurant Bill with Discount
bill = float(input("Enter the bill please: "))

if bill > 100:
  discount = 0.10 * bill # 10 % Discount
else:
  discount = 0   # No discount
final_bill = bill - discount

print(f"Original bill is: {bill} TK")
print(f"The discount bill is: {discount} TK")
print(f"The final bill is: {final_bill} TK")

# Login Authentication

username = input("Enter the username please: ")
password = input("Enter the password please: ")

if username == "admin" and password == "12345":
  print("Login Successful !!")
else:
  print("Invalid Credentials !!!")

# Traffic Light System

color = input("Enter a color (Know traffic system): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready to go")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

# Leap Year Checker

year = int(input("Enter the year please: "))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
  print(f"This {year} is leap year")
else:
  print(f"This {year}  is not leap year")


# Job Eligibility Checker

age = int(input("Enter your age: "))
qualification = input("Enter your qualification: ").lower()

if age >= 18 and qualification == "graduate":
    print("Eligible for Job")
else:
    print("Not Eligible")

# Electricity Bill Calculator

units = int(input("Enter number of units consumed: "))

if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
else:
    rate = 10

# Calculate total bill
bill = units * rate

print(f"Total units: {units}")
print(f"Rate per unit: {rate} BDT")
print(f"Total Payable Amount: {bill} BDT")

























