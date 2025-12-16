# --------------🟢 Level 1: Easy (4 Problems)----------------

# 1. Area of a Circle
# Logic: Using float input, Literals (pi), and Exponent operator.

radius = float(input("Enter the radius please: "))
pi = 3.1416 # literals
area = pi * (radius ** 2)
print(f"The area of circle is: {area:.2f}")
# 2. Simple Interest Calculator
# Logic: Basic arithmetic formula

principle = float(input("Enter the principle here: "))
rate = float(input("Enter the interest rate(in %): "))
time = int(input("Enter the time (in years): "))
interest = (principle * rate * time) / 100
total_balance = interest + principle
print("The interest is: ", interest, "TK")
print("The total balance is: ", total_balance)
# 3. Convert Days to Hours and Minutes
# Logic: Multiplication.
day = int(input("Enter the day: "))

hours = day * 24
minutes = hours * 60
print("The hours is",hours, "and minutes is",minutes)

# 4. The Greeter (String Concatenation)
# Logic: Combining strings.
first_name = input("Please enter your name: ")
last_name = input("Enter the last name: ")

full_name = first_name +" " +last_name
print("Welcome to the new journey",full_name)

# -------------------🟡 Level 2: Medium (3 Problems)------------------

# 5. Convert Minutes to Hours and Minutes
# Logic: Using Floor Division (//) for hours and Modulo (%) for remaining minutes.
total_minutes = int(input("Enter the total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60
print(f"Hours: {hours} & minutes: {minutes}")

# 6. Temperature Converter (Fahrenheit to Celsius)
# Logic: Operator precedence (Brackets are important).
fahrenheit = int(input("Enter the temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"The temperature in celsius:{celsius:.2f}°C")
# 7. Swapping Variables (Arithmetic Method)
# Logic: Swapping without a temporary variable or python shortcut.
a = int(input("Enter the number of A: ")) # 12
b = int(input("enter the number of B: ")) # 21

a = a + b 
b = a - b
a = a - b
print(f"After Swapping A: {a} & B: {b}")

# -----------------🔴 Level 3: Hard (3 Problems)---------------
# 8. Sum of Digits (3-Digit Number)
# Logic: Extracting digits using Math. Input 123 -> Output 6.
num = int(input("Enter the number: "))
digit_3 = num % 10   #Last digit of any number
digit_2 = (num // 10) % 10  #Middle digit of any number
digit_1 = num // 100  #First number of any number
total_number = digit_3 + digit_2 + digit_1
print("The sum of digit is:",total_number)

# 9. Coordinate Geometry (Distance Formula)
x1 = int(input("Enter the X1: "))
x2 = int(input("Enter the X2: "))
y1 = int(input("Enter the Y1: "))
y2 = int(input("Enter the Y2: "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"The Distance is:{distance:.2f} cm")

# 10. ATM Currency Logic
# Logic: Breaking an amount into 500, 100, and 50 notes.
amount = int(input("Enter the amount please: "))

notes_500 = amount // 500
amount = amount % 500
notes_100 = amount // 100
amount = amount % 100
notes_50 = amount // 50
remaining_balance = amount % 50

print(f"Notes_500: {notes_500} TK Notes_100: {notes_100} TK Notes_50: {notes_50} TK & Left Balance: {remaining_balance} TK")

# 🔹 Part 2: Nested If-Else
# Topics: Conditional logic where one if is inside another if.

# ------------------------🟢 Level 1: Easy (4 Problems)------------------
# 1. Positive, Negative, or Zero (Nested)
# Logic: Check if not zero, then check if positive/negative.

num = int(input("Enter the number please: "))
if num != 0:
    if num > 0:
        print("This is Positive number")
    else:
        print("This is Negative number")
else:
    print("This is Zero")
# 2. Voting Eligibility (with ID check)
# Logic: Age > 18? -> If yes, Do you have ID?
name = input("Enter Your Name Please: ")
age = int(input("Enter Your Age: "))
has_id = input("Do You Have ID (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("You can vote")
    else:
        print("You need an ID to vote")
else:
    print("You are too young. You can't vote")

# 3. Exam Result (Pass/Fail/Distinction)
# Logic: Pass? -> If yes, is it Distinction?
mark = int(input("Enter the marks please: "))
if mark >= 40:
    if mark >= 80:
        print("You passed with letter marks")
    else:
        print("You just passed")
else:
    print("You are Failed")

# 4. Smallest of Three Numbers
# Logic: Nested comparison.
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
if a < b:
    if a < c:
        print("a is smallest number")
    else:
        print("c is smallest number")
else:
    if b < c:
        print("b is smallest number")
    else:
        print("C is smallest number")

# -------------🟡 Level 2: Medium (3 Problems)----------
# 5. Login System
# Logic: Check Username -> If correct, Check Password.

db_user = "admin12"
db_password = "12345"

user = input("Enter the username please: ")
password = input("Enter the password: ")

if user == db_user:
    if password == db_password:
        print("Login Successful !!!")
    else:
        print("Incorrect Password.Please give right password")
else:
    print("Invalid User. User not found")

# 6. Leap Year Checker (Nested Logic)
# Logic: Divisible by 4? -> Yes -> Divisible by 100? -> Yes -> Divisible by 400?
year = int(input("Enter the Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not Leap Year")
# 7. Job Eligibility Check
# Logic: Degree? -> Experience? -> Skills?
has_degree = input("Do You have any degree(yes/no): ").lower()

if has_degree == "yes":
    experience = int(input("Enter the year of experience: "))
    if experience >= 2:
        print("You are hired")
    else:
        print("You need more experience")
else:
    print("Degree is mandatory")

# ------------------🔴 Level 3: Hard (3 Problems)-------------------
# 8. Triangle Type Checker
# Logic: Is it a valid triangle? -> If yes, checks types (Equilateral/Isosceles/Scalene).
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if (a + b > c) and (a + b > b) and (a + b > a):
    if a == b and b == c:
        print("Equilateral Triangle")
    else:
        if a == b or b == c or c == a:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
else:
    print("Not a valid Triangle")

# 9. Bank Loan Approval System
# Logic: Income check -> Credit Score check -> Outstanding Debt check.
income = float(input("Enter the income please: "))
credit_score = int(input("Enter the credit score: "))

if income >= 30000:
    if credit_score > 700:
        has_debt = input("Do You have debt(yes/no): ")
        if has_debt == "no":
            print("Loan Approved !!")
        else:
            print("Your Loan is Denied")
    else:
        print("You have not enough credit_score")
else:
    print("Your Income is less then 30000")
# 10. Rock, Paper, Scissors Logic
# Logic: Player 1 Choice -> Nested check against Player 2 Choice.

p1 = input("Player 1 (rock/paper/scissors): ")
p2 = input("Player 2 (rock/paper/scissors: )")

if p1 == p2:
    print("Match Tie!!!")
else:
    if p1 == "rock":
        if p2 == "scissors":
            print("Player 1 is win !!!")
        else:
            print("Player 2 is win !!")
    elif p1 == "paper":
        if p2 == "rock":
            print("Player 1 win !!!")
        else:
            print("Player 2 is win !!")
    elif p1 == "scissors":
        if p2 == "paper":
            print("Player 1  win!!!")
        else:
            print("Player 2 win!! ")




















