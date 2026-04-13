# simple print, variables

failed_subjects = "3"
name = "john"
print("Dear Mrs Badgers")
print("your son " + name + " is falling " + failed_subjects + " subjects")
print(name + " will need to redo " + failed_subjects + " courses")
print(name + " is doing well in Geography")

# Datatypes & typecasting
print(type("hello"))
print(type(23))
print(type(2.50))
print(type(True))
print(type([23,34]))
print(type((2,34,4)))
print(type({"hello":"Python"}))
print(type({23,45}))

# Variables & datatype exercise
item_name = "Apple Mobile"
price = 25.5
inventory = "12"
print(f"The item name is {item_name}, this item price is {price} tk & this item stock is {inventory}")

# Arcade Day pass Tracker - challenge steps
customer_name = "kabir"
passes_bought = 3
token_per_pass = 30
pass_price = 15.00
token_per_game = 3

total_token = passes_bought * token_per_pass
total_cost = passes_bought * pass_price
games_available = total_token // token_per_game

print("======= Arcade Day Pass ========")
print("Customers: ", customer_name)
print("Passes: ", passes_bought)
print("Tokens: ", total_token)
print("Total Cost: $" + str(total_cost))
print("Games available " + str(games_available))

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("Enter the first name: ")
distance_km = float(input("Enter the distance in km: "))
distance_miles = distance_km / 1.609
print(f"Hi {name}! You entered {distance_km} km, which is approximately {round(distance_miles, 2)} miles.")







