# Aggregation has a relationship
# one class owns another class
"""class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_info(self):
        print(f"Name: {self.name},Gender:{self.gender},Address: {self.address.city},{self.address.pin},{self.address.state}")
class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state
adds = Address("Dhaka",1230,"Bangladesh")
cus = Customer("Jahid","Male",adds)
cus.print_info()"""

# 1. Sum of Natural Numbers (The Gauss Formula)
# Logic: How to find the sum of numbers from 1 to N (e.g., 1+2+3...+100) without a loop?
"""num = int(input("Enter the number: "))
sum_n = (num * (num + 1)) // num
print("The sum of number from 1 to",num, "is",sum_n)"""

# 2. Bytes to Kilobytes and Megabytes
# Logic: Data conversion logic. 1 KB = 1024 Bytes.
"""bytes_input = int(input("Enter the number in bytes: "))
kilobytes = bytes_input / 2024
megabytes = kilobytes / 1024

print("Size in KB",kilobytes, "KB")
print("Size in MB", megabytes, "MB")"""

# 3. Diagonal of a Rectangle
"""length = float(input("Enter the length: "))
width = float(input("Enter the width here: "))

diagonal = (length **2 + width ** 2) ** 2
print("The Diagonal Length: ",diagonal)"""

# 4. Extracting the First Digit (Using String Casting)
# Logic: Instead of math, convert the number to text strings to grab the first character.
"""num = int(input("Enter the number: "))
num_txt = str(num)
first_digit = int(num_txt[0])
print("The first digit is: ",first_digit)"""
# 5. Calculate Force (Physics)
mass = float(input("Mass (kg): "))
acceleration = float(input("Acceleration (m/s^2): "))

force = mass * acceleration

print("Force applied:", force, "Newtons")


































