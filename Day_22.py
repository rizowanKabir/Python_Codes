# 1️⃣ Seconds ↔ Minutes Converter
def time_converter(value, unit):
    if unit == "sec_to_min":
        return value / 60
    elif unit == "min_to_sec":
        return value * 60
    else:
        return "Invalid Unit"

while True:
    try:
        choice = input("1. Sec→Min  2. Min→Sec  (q to quit): ")
        if choice.lower() == "q":
            break
        value = float(input("Enter value: "))
        if choice == "1":
            print(time_converter(value, "sec_to_min"), "Minutes")
        elif choice == "2":
            print(time_converter(value, "min_to_sec"), "Seconds")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number!")

# 2️⃣ Celsius ↔ Fahrenheit Converter
def temp_converter(value, unit):
    if unit == "c_to_f":
        return (value * 9/5) + 32
    elif unit == "f_to_c":
        return (value - 32) * 5/9

while True:
    try:
        choice = input("1. C→F 2. F→C (q to quit): ")
        if choice.lower() == "q":
            break
        temp = float(input("Enter temperature: "))
        if choice == "1":
            print(temp_converter(temp, "c_to_f"), "F")
        else:
            print(temp_converter(temp, "f_to_c"), "C")
    except ValueError:
        print("Invalid input! Enter a number.")

# 3️⃣ Meter ↔ Kilometer Converter
def length_converter(value, unit):
    if unit == "m_to_km":
        return value / 1000
    elif unit == "km_to_m":
        return value * 1000

while True:
    try:
        choice = input("1. M→KM 2. KM→M (q to quit): ")
        if choice.lower() == "q":
            break
        val = float(input("Enter value: "))
        if choice == "1":
            print(length_converter(val,"m_to_km"),"KM")
        else:
            print(length_converter(val,"km_to_m"),"M")
    except ValueError:
        print("Enter a valid number!")

# 4️⃣ Simple Calculator (+,-,*,/)
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b

while True:
    try:
        a = float(input("Enter first number (q to quit): "))
        b = float(input("Enter second number: "))
        op = input("Operator (+,-,*,/): ")
        print("Result:", calculator(a, b, op))
    except ValueError:
        print("Please enter numbers only!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

# 5️⃣ Area Calculator (Square & Circle)
def area(value, shape):
    if shape == "square":
        return value ** 2
    elif shape == "circle":
        return 3.1416 * value ** 2

while True:
    try:
        shape = input("square/circle (q to quit): ").lower()
        if shape == "q":
            break
        val = float(input("Enter value: "))
        print("Area:", area(val, shape))
    except ValueError:
        print("Invalid input!")
