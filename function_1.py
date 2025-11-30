# 1. Inventory Price Calculator
# Real-world use: Used in e-commerce dashboards for price summaries.
# Write a function calculate_inventory_summary (prices) that:
#  receives a list of product prices
#  returns total_cost and average_cost
# Input: [120, 250, 399, 150]
# Output: (919, 229.75)

def calculate_inventory_summary(prices):
    total_cost = 0
    for price in prices:
        total_cost += price
    average_cost = total_cost / len(prices)
    return total_cost, average_cost
# -------Take input from user-------
prices = []
n = int(input("Enter how many items do you have?: "))
for i in range(n):
    price = float(input(f"Enter the price of item {i + 1}: "))
    prices.append(price)
# Calculate Summary
total, avg = calculate_inventory_summary(prices)
print("\n----Inventory Management System-------")
print("Total Cost:",total)
print("Average Cost:", avg)

# 2. Unique Visitor Tracker
# Real-world use: Website analytics tools calculating daily active users.
# Write a function count_unique_visitors(visitor_list) that:
#  takes a list of visitor IDs
#  returns the number of unique visitors
# Input: [101, 205, 101, 310, 205, 550]
# Output: 4 (The unique IDs are 101, 205, 310, 550)

def count_unique_visitors(visitor_list):
    unique_visitors = set(visitor_list)
    return len(unique_visitors)

# ---User Input----
n = int(input("Enter the how many visitors you have in list: "))
visitors = []
for i in range(n):
    name = input(f"Enter the name here SI-{i + 1}: ")
    visitors.append(name)
# Unique Visitors List
print("Total unique Visitors: ", count_unique_visitors(visitors))

# 3. Product Category Counter
# Real-world use: Inventory/category-based analytics.
# Write a function count_categories(products) that:
#  takes a list of product names
#  returns a dictionary counting each product type.
# Input: ["Laptop", "Smartphone", "Monitor", "Laptop", "Smartphone", "Headphones", "Laptop"]
# Output: {"Laptop": 3, "Smartphone": 2, "Monitor": 1, "Headphones": 1}

def count_categories(products):
    category_count = {}
    for item in products:
        if item in category_count:
            category_count[item] += 1
        else:
            category_count[item] = 1
    return category_count
# ---Take User input---
n = int(input("Enter the how many products: "))
products = []
for i in range(n):
    product = input(f"Enter the product{i + 1} category: ")
    products.append(product)
print("Category Count", count_categories(products))

# 4. Temperature Analytics
# Real-world use: Health tech temperature screening systems.
# Write a function analyze_temperatures(temp_list) that:
#  separates high (> 38°C) and normal temps
#  returns two lists: (high_list, normal_list)
# Input: [36.5, 38.0, 39.1, 37.2, 40.5, 38.0, 37.9]
# High List (>38°C): [39.1, 40.5]
# Normal List (<38°C): [36.5, 38.0, 37.2, 38.0, 37.9]
# Full Output Tuple: ([39.1, 40.5], [36.5, 38.0, 37.2, 38.0, 37.9])

def analyze_temperature(temp_list):
    high = []
    normal = []
    for temp in temp_list:
        if temp > 38:
            high.append(temp)
        else:
            normal.append(temp)
    return high, normal
# Take Input From User
n = int(input("How many temperature: "))
temps = []
for i in range(n):
    temp = float(input(f"Enter the temp {i + 1}: "))
    temps.append(temp)
high_temp, normal_temp = analyze_temperature(temps)
print("The high_temperature: ", high_temp)
print("The low_temperature: ", normal_temp)

# 5. Menu Price Lookup
# Real-world use: Restaurant ordering apps.
# Write a function get_price(menu, item) that:
#  receives a dictionary menu and an item

def get_price(menu, item):
    return menu.get(item, "Item not found")

# Take input from user
menu = {}
n = int(input("How many Item do you have?: "))
for i in range(n):
    name = input(f"Enter the item SI-{i + 1} name: ")
    price = float(input(f"Enter the price of {name}: "))
    menu[name] = price
item = input("Enter the item name to check price: ")
print(get_price(menu,item))

# 6. Student Grading System
# Real-world use: School result automation.
# Write a function calculate_grade(score) that:
#  returns "A+", "A", "A-", "F" based on numeric marks
# Write another function grade_students(student_dict) to:
#  take a dictionary of student:score
#  return student:grade dictionary
# Input (Scores Dictionary): {"Alice": 85, "Bob": 78, "Charlie": 32, "David": 69}
# Output (Grades Dictionary): {"Alice": "A+", "Bob": "A", "Charlie": "F", "David": "A-"}

def calculate_grade(score):
    if score >= 80:
        return "A+"
    elif score >= 60:
        return "A"
    elif score >= 40:
        return 'A-'
    else:
        return "F"
def grade_student(student_dict):
    grades = {}
    for student, marks in student_dict.items():
        grades[student] = calculate_grade(marks)
    return grades

# Take user input
students = {}
n = int(input("How many students here: "))
for i in range(n):
    name = input(f"Enter the student SI-{i + 1} name: ")
    marks = float(input(f"Enter the mark for {name}: "))
    students[name] = marks
print("Grades: ",grade_student(students))

# 7. Discount Calculator
# Real-world use: Online store discount engine.
# Write a function apply_discounts(products) where:
#  products is a list of tuples: (name, price, discount)
#  return a list of updated prices after discount
# Input (List of Tuples): [("Keyboard", 80.00, 20), ("Mouse", 25.00, 10), ("Monitor", 300.00, 5)]
# Output (List of Prices): [64.00, 22.50, 285.00]

def apply_discounts(products):
    discounted_prices = []
    for name,price,discount in products:
        discounted_price = price - (price * discount / 100)
        discounted_prices.append((name,price,discounted_price))
    return discounted_prices
# Take input from user
n = int(input("Enter the how many products: "))
products = []
for i in range(n):
    name = input(f"Enter the product {i + 1} name: ")
    price = float(input(f"Enter the product price for {name}: "))
    discount = float(input("Enter the discount %: "))
    products.append((name,price,discount))
print("Discounted_prices: ",apply_discounts(products))

# 8. Hashtag Generator
# Real-world use: Social media automation tools.
# Write a function generate_hashtags(sentence) that:
#  converts every word into a hashtag
#  returns a list of hashtags
# Input: "AI Data Science"
# Output: ["#ai", "#data", "#science"]

def generate_hashtags(sentence):
    words = sentence.split()
    hashtags = []
    for word in words:
        hashtags.append("#" + word.lower())
    return hashtags
# Take input from user
sentence = input("Enter the sentence: ")
print("Hashtags: ", generate_hashtags(sentence))

# 9. User Authentication Mock
# Real-world use: Login systems (basic level).
# Write a function login(username, password) that:
#  checks if username exists
#  checks if password matches
#  returns "Login Successful" or "Invalid Credentials"

def login(users,username,password):
    if username in users and users[username] == password:
        return "Login Successful"
    else:
        return "Invalid Credential"
# Take input from user

users ={}
n = int(input("Enter how many users account?: "))
for i in range(n):
    user = input(f"Enter the username {i + 1}: ")
    pwd = input("Enter the password please: ")
    users[user] = pwd
username = input("Enter login username: ")
password = input("Enter login password: ")
print(login(users,username,password))

# 10. Shopping Cart Bill Calculator
def calculate_total(cart, prices):
    total = 0
    for item in cart:
        total += prices.get(item, 0)
    return total


# --- User Enters Price List ---
prices = {}
n = int(input("How many items in price list? "))

for i in range(n):
    item = input(f"Enter item {i+1} name: ")
    price = float(input("Enter price: "))
    prices[item] = price

# --- User Enters Cart Items ---
cart = []
m = int(input("\nHow many items in cart? "))

for i in range(m):
    c = input(f"Enter cart item {i+1}: ")
    cart.append(c)

































