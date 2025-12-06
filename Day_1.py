

# Collection of class object in oop
class person:
    def __init__(self,name,country):
        self.name = name
        self.country = country
obj1 = person("Rizowan","Bangladesh")
obj2 = person("Shagor","Dhaka")
obj3 = person("Shakil", "Saudiarabia")
l = [obj1, obj2, obj3]
for i in l:
    print(i.name, i.country)

# 1. Distance Between Two Points (Geometry)
# Concept: Exponent (**) for square root, Parentheses for precedence.

# Take input from user
x1 = float(input("Enter the number of x1: "))
x2 = float(input("Enter the number of x2: "))
y1 = float(input("Enter the number of y1: "))
y2 = float(input("Enter the number of y2: "))

x_diff = (x2 - x1) ** 2
y_diff = (y2 - y1) ** 2

distance = (x_diff + y_diff) ** 0.5
print(f"The distance between two point: {distance:.2f} Meters")

# 2. Student Marks Percentage
# Concept: Arithmetic Operators, Type Conversion.

math = float(input("Enter the number of math: "))
physics = float(input("Enter the number of physics: "))
english = float(input("Enter the number of english: "))

total_mark = 300
obtained_mark = math + physics + english
percentages = (total_mark / obtained_mark) * 100
print("Total marks is:", obtained_mark)
print("percentage of your mark: ",percentages, "%")

# 3. Speed Calculator
# Concept: Float Division (/), Variables.
# logic:speed = Distance / time
distance = float(input("Enter the distance(km): "))
time = int(input("Enter the time in(hours): "))
speed = distance / time
print("The total speed is: ",speed, "kmh")

# 4. Area of a Trapezoid
# Concept: Mathematical Formula translation.

a_side = float(input("Enter the number side of a: "))
b_side = float(input("Enter the number side of b: "))
height = float(input("Enter the height please: "))
# Calculate the area of trapezoid
area = ((a_side + b_side) / 2) * height
print("The Area of a trapezoid is: ", area)

# 5. Net Salary Calculator (Deductions)
# Concept: Percentage Logic, Subtraction.
# Logic: Gross Salary - Tax = Net Salary.
gross_salary = float(input("Enter the gross salary here: "))
tax_rate = 0.10
tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount
print("The salary of deduction: ",tax_amount,"TK")
print("The net salary in your hand: ",net_salary, "TK")

# 6. Tile Calculator (Floor Coverage)
# Concept: Area Calculation, Division
floor_len = float(input("Enter the floor length(fit): "))
floor_wid = float(input("Enter the floor width(fit): "))

tiles_len = float(input("Enter the tiles length(fit): "))
tiles_wid = float(input("Enter the tiles width(fit): "))
area_of_floor = floor_len * floor_wid
area_of_tiles = tiles_len * tiles_wid
number_of_tiles = area_of_floor / area_of_tiles
print("The total tiles needed: ",number_of_tiles,"pieces")

# 7. Logical Pass/Fail Check
# Concept: Comparison Operator (>=), Boolean Output.
marks = int(input("Enter the marks please: "))
passing_mark = 33
is_pass = passing_mark <= marks
print("Did student pass or fail??: ",is_pass)

# 8. Temperature Conversion (Kelvin to Celsius)
# Concept: Constant Subtraction.
kelvin = float(input("Enter the temperature in kelvin: "))
constant = 273.15 # literals
celsius = kelvin - constant
print("The temperature in celsius is: ",celsius)
# 10. Car Fuel Mileage
# Concept: Division, Float input.

start_km = float(input("Odometer at start: "))
end_km = float(input("Odometer at end: "))
fuel_used = float(input("Fuel consumed (liters): "))

distance_traveled = end_km - start_km
mileage = distance_traveled / fuel_used

print("Your car mileage is:", mileage, "km per liter")

# 1. Reverse a 3-Digit Number (Pure Math Logic)
# Logic: How to turn 123 into 321 using only math?
num = int(input("Enter the three digit numbers:(e.g.s 123): "))
digit_3 = num % 10
digit_2 = (num // 10) % 10
digit_1 = num // 100
reversed_number = (digit_3 * 100) + (digit_2 * 10) + digit_1
print("Reversed numbers: ",reversed_number)

# 2. Kinetic Energy Calculator (Physics Logic)
# Concept: Exponent Operator (**), Float.
mass = float(input("Enter the mass please(km): "))
velocity = float(input("Enter the velocity(m/s): "))

kinetic_energy = 0.5 * mass * velocity
print("The Kinetic Energy: ",kinetic_energy,"Joules")

# 3. Calculating Remainder without % Operator
# Logic: How does the modulus operator actually work?
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

quotient = dividend // divisor
remainder = dividend - (divisor * quotient)
print("Calculated Remainder: ",remainder)

# 4. Quadratic Equation Discriminant
# Concept: Order of operations.

a = float(input("Enter the number of A: "))
b = float(input("Enter the number of B: "))
c = float(input("Enter the number of C: "))

discriminant = (b ** 2) - (4 * a * c)
print("Discriminant is: ", discriminant)

# 5. Slope of a Line
# Concept: Parentheses for grouping logic.
x1 = float(input("Enter the number of x1: "))
x2 = float(input("Enter the number of x2: "))
y1 = float(input("Enter the number of y1: "))
y2 = float(input("Enter the number of y2: "))

slope_of_line = (y2 - y1) / (x2 - x1)
print("The slope is: ",slope_of_line)

# 6. Boolean Range Check (Is it a teenager?)
# Concept: Chained Comparison Operators.
# Logic: Checking if a number is between 13 and 19 (inclusive) without if.
age = int(input("Enter the age please: "))
is_teenager = 13 <=age<=20
print("is he/she teenager: ",is_teenager)

# 7. Minutes to Hours and Minutes
# Concept: Floor Division (//) vs Modulo (%).
# Logic: 130 minutes = 2 hours and 10 minutes.

total_minutes = int(input("Enter the total minutes: "))
minutes = total_minutes % 60
hours = total_minutes // 60
print(total_minutes,"minutes", hours, "Hours", minutes, "minutes")

# 8. Username Generator (String Concatenation)
# Concept: String manipulation, Casting.
# Logic: Combine Name + First 3 letters of city + Birth Year.
name = input("Enter the name first three letters: ")
city = input("Enter the name first two letters: ")
birth_year = input("Enter the birth_year: ")
username = name+""+city+""+birth_year
print("Username is: ",username)
# 9. Average Speed Calculation
# Concept: Total / Total logic.
distance_1 = int(input("Enter the distance_1(km): "))
time_1 = float(input("Enter the time_1(hours): "))

distance_2 = int(input("Enter the distance_2(km): "))
time_2 = float(input("Enter the time_2(hours): "))
avg_speed = (distance_1 + distance_2) / (time_1 + time_2)
print("The average speed is: ",avg_speed,"km/h")
# 10. Salary Annual Increment Prediction
# Concept: Compound Assignment (+=).
# Logic: Calculate what the salary will be next year with a 15% raise.
current_salary = float(input("Current Monthly Salary: "))

# Logic: 15% raise means multiplying by 0.15 and adding to original
raise_amount = current_salary * 0.15

# Using Compound Assignment to update the variable
current_salary += raise_amount

print("Next year your salary will be:", current_salary)








































