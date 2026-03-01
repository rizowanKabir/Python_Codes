#  MATHEMATICAL PROBLEMS
# Check if a number is prime
def is_prime(n):
    if n < 2:
        return  False
    for i in range(2,n):
        if n % i == 0:
            return False
    return  True
result = is_prime(11)
print(result)

# Currency Converter
def currency_converter(amount, rate):
    return round(amount * rate, 2)

if __name__ == "__main__":
    print("Currency Converter")

    print("1. USD->EUR")
    print("2. USD->GBP")
    print("3. USD->JPY")
    choice = input("Enter the choice(1-3): ")
    amount = float(input("Enter the amount: "))

    if choice == "1":
        rate = 0.92
        target = "EUR"
    elif choice == "2":
        rate = 0.81
        target = "GBP"
    elif choice == "3":
        rate = 134.50
        target = "JPY"
    else:
        print("Invalid Choice.")
        exit()
    print(f"Converted amount: {currency_converter(amount,rate)} {target}")

# time converter using function
def time_converter(value,unit):
    if unit == "sec_to_min":
        return value / 60
    elif unit == "min_to_sec":
        return value * 60
    elif unit == "min_to_hr":
        return value / 60
    elif unit == "hr_to_min":
        return value * 60
    else:
        return "Invalid Choice"

if __name__ == "__main__":
    print("Conversion Options")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Minutes to Hours")
    print("4. Hours to Minutes")

    choice = input("Chose Options(1-4): ")
    value = float(input("Enter the time value: "))

    if choice == "1":
        unit = "sec_to_min"
        target = "Minutes"
    elif choice == "2":
        unit = "min_to_sec"
        target = "Seconds"
    elif choice == "3":
        unit = "min_to_hr"
        target = "Hours"
    elif choice == "4":
        unit = "hr_to_min"
        target = "Minutes"
    else:
        print("Invalid Choice")
        exit()

    print(f"Converted time: {time_converter(value,unit)} {target}")

# University Course Enrollment System

LOW_ENROLLMENT_THRESHOLD = 10
course_catalog = [
    ("CS101","Introduction to computer Science", 3),
    ("MATH201","Linear Algebra", 4),
    ("ENG150", "Academic Writing", 2)
]

courses = {
    "CS101": {
        "enrolled": 45,
        "Instructor": "Dr. Sharma",
        "room": "Block A - 101"},
    "MATH201": {
        "enrolled": 8,
        "Instructor": "Dr. Chayan",
        "room": "Block B 201"},
    "ENG150": {
        "enrolled": 12,
        "Instructor":"Dr.Rana",
        "room": "Block C 301"},
}

new_course = ("PHY120", "Physics for Engineers", 3)
course_catalog.append(new_course)
courses["PHY120"] = {
    "enrolled": 12,
    "Instructor": "Dr. Hasbi",
    "room": "Block D 401"
}
courses["CS101"]["enrolled"] -= 3

low_enrollment_courses = [
    code for code, info in courses.items()
    if info["enrolled"] < LOW_ENROLLMENT_THRESHOLD
]
print("Low Enrollment Courses: ", low_enrollment_courses)





