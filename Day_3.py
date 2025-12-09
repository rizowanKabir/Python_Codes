# 6. Age in Days (Approximate)
# Logic: Converting years into days.
age_years = int(input("Enter the age years: "))
age_days = age_years * 365
print("You have lived in approximately: ",age_days, "Days")

# 7. Per Person Cost (Pizza Party)
# Logic: Total Cost divided by Number of People.
pizza_cost = float(input("Enter the pizza cost please: "))
drink_cost = float(input("Enter the drink cost please: "))
people = int(input("Enter the total people: "))

total_cost = pizza_cost + drink_cost
per_person_cost = total_cost / people
print("per person have to pays: ",per_person_cost,"TK")
# 8. Final Price with Tax AND Discount
# Logic: Step-by-step arithmetic.

price = float(input("Enter the principle price please: "))
tax_rate = float(input("Enter the tax rate: ")) # 10%
discount = float(input("Enter the discount pleas: ")) # 5 %

price_with_tax = price + (price * tax_rate)
final_price = price_with_tax - (price_with_tax * discount)
print(f"The price {price} & final price is: {final_price} TK")
# 9. Boolean "Is it divisible?" Check
# Logic: Using modulo % and comparison == to get True/False.
num = int(input("Enter a number: "))

# Logic: If remainder is 0, it is divisible by 5
is_divisible_by_5 = (num % 5 == 0)

print("Is the number divisible by 5?:", is_divisible_by_5)

# 10. Volume of a Cube
# Logic: side**3
side = int(input("Enter the number of length: "))
volume = side ** 3
print("The volume of cube is: ",volume,"meters")

# -----------If/Elif?else statement condition------------
# 11. Positive or Negative?
# Logic: If number is greater than 0, it's positive.
number = int(input("Enter the number here: "))
if number > 0:
    print(f"{number} is positive number")
elif number == 0:
    print("Try to give less or greater than Zero")
else:
    print(f"{number} is Negative number")
# 12. Odd or Even Checker
# Logic: If a number divided by 2 leaves 0 remainder, it is Even.

num = int(input("Enter the number to check even or odd: "))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# 13. Voting Eligibility
# Logic: Check if age is 18 or above.
name = input("Enter the name please: ")
age = int(input("Enter the age t0 check vote eligibility: "))

if age > 18:
    print("You are age enough to pay vote")
elif age == 18:
    print("You are in process")
else:
    print("You are not age enough to pay vote")

# 14. Maximum of Two Numbers
# Logic: Compare two variables to see which is bigger.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater:", a)
else:
    print("Second number is greater or equal:", b)
# 15. Password Checker
# Logic: Compare input string with stored string.

password = input("Enter the password: ")
if password == "admin@123":
    print("Password was matched. Access Granted")
else:
    print("Wrong Password Please try to give right password")

# 16. Pass or Fail
# Logic: Check if marks satisfy the passing criteria.
marks = int(input("Enter marks: "))

if marks >= 33:
    print("Result: PASSED")
else:
    print("Result: FAILED")
# 17. Square or Rectangle?
# Logic: If length equals width, it's a square.

length = int(input("Enter the length here: "))
width = int(input("Enter the width here: "))

if length == width:
    print("This is a Square")
else:
    print("This is a rectangle")

# 18. Discount Eligibility
# Logic: Give discount only if bill amount is high (e.g., > 1000).
bill_amount = float(input("Enter the Bill amount: "))

if bill_amount >= 1000:
    print("Congratulations !! You get  a discount 10%")
    total_bill = bill_amount * 0.90
    print("New Bill amount is: ",total_bill,"TK")
else:
    print("The bill amount is: ", bill_amount, "TK")
# 19. Divisibility Check (Leap Year Logic Basis)
# Logic: Check if a year is divisible by 4 (Basic Leap Year Logic).
year = int(input("Enter the years: "))

if year % 4 == 0:
    print("This year might be a leap year")
else:
    print("This is year not a leap year")
# 20. Water State Checker (Physics Logic)
# Logic: Check freezing point.

temp = float(input("Enter water temperature (Celsius): "))

if temp <= 0:
    print("Water is Frozen (Ice).")
else:
    print("Water is Liquid.")




























