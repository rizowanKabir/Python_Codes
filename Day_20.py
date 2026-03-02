# ✅ Problem 10: Discount Calculator

def discount(price, percent):
    return price - (price * percent / 100)
price = float(input("Enter Price: "))
percent = float(input("Enter Discount%: "))
print(f"Final Price: {discount(price,percent)} TK")

# Convert number system
def number_system_converter(value,system):
    if system == "dec_to_bin":
        return bin(int(value))
    elif system == "dec_to_oct":
        return oct(int(value))
    elif system == "dec_to_hexa":
        return hex(int(value))
    elif system == "bin_to_dec":
        return int(value, 2)
    elif system == "oct_to_dec":
        return int(value,8)
    elif system == "hex_to_dec":
        return int(value,16)
    else:
        return "Invalid Choice"

if __name__ == "__main__":
    print("Conversion Options")
    print("1. Decimal -> Binary")
    print("2. Decimal -> Octal")
    print("3. Decimal -> Hexadecimal")
    print("4. Binary -> Decimal")
    print("5. Octal -> Decimal")
    print("6. Hexadecimal -> Decimal")

    choice = input("Choose options(1-6): ")
    value = input("Enter the value: ")

    if choice == "1":
        system = "dec_to_bin"
        target = "Binary"
    elif choice == "2":
        system = "dec_to_oct"
        target = "Octal"
    elif choice == "3":
        system = "dec_to_hex"
        target = "Hexadecimal"
    elif choice == "4":
        system = "bin_to_dec"
        target = "Decimal"
    elif choice == "5":
        system = "Oct_to_dec"
        target = "Decimal"
    elif choice == "6":
        system = "hex_to_dec"
        target = "Decimal"
    else:
        print("Invalid Choice")
        exit()
    print(f"Converted Value: {number_system_converter(value,system)} {target}")

# ✅ Problem 9: Password Length Checker
def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password"
pw = input("Enter the password: ")
print(check_password(pw))

# ✅ Problem 8: Age to Days Converter
def age_to_days(age):
    return  age * 365
age = int(input("Enter the age: "))
print(age_to_days(age))

# ✅ Problem 7: Student Grade System
def grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "D"
    else:
        return "Fail"
mark = int(input("Enter the mark please: "))
print("Grade: ",grade(mark))

# ✅ Problem 6: Even or Odd Checker
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number: "))
print(check_even_odd(num))

# ✅ Problem 6: Even or Odd Checker
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number: "))
print(check_even_odd(num))

# ✅ Problem 5: Weight Converter
def weight_converter(value, unit):
    if unit == "kg_to_g":
        return value * 1000
    elif unit == "g_to_kg":
        return value / 1000

choice = input("1.KG→G 2.G→KG: ")
value = float(input("Enter weight: "))

if choice == "1":
    print(weight_converter(value,"kg_to_g"),"Gram")
else:
    print(weight_converter(value,"g_to_kg"),"KG")

# ✅ Problem 4: Area Calculator
def area(value,shape):
    if shape == "square":
        return value * value
    elif shape == "circle":
        return 3.1416 * value * value
choice = input("square/circle: ")
value = float(input("Enter the value: "))
print("Area", area(value,choice),"CM")

# ✅ Problem 3: Simple Calculator
def calculator(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
op = input("Enter the operators(+,-,*,/): ")
print(calculator(x,y,op))

# ✅ Problem 2: Length Converter
def length_converter(value, unit):
    if unit == "m_to_km":
        return value / 1000
    elif unit == "km_to_m":
        return value * 1000

choice = input("1.M→KM 2.KM→M : ")
value = float(input("Enter length: "))

if choice == "1":
    print(length_converter(value,"m_to_km"),"KM")
else:
    print(length_converter(value,"km_to_m"),"Meter")

# ✅ Problem 1: Temperature Converter
def temperature_converter(value,unit):
    if unit == "c_to_f":
        return (value * 9/5) + 32
    elif unit == "f_to_c":
        return (value - 32) * 5/9
    else:
        return "Invalid Choice"
choice = input("1.C→F  2.F→C : ")
value = float(input("Enter temperature: "))

if choice == "1":
    print(temperature_converter(value, "c_to_f"), "F")
elif choice == "2":
    print(temperature_converter(value, "f_to_c"), "C")
