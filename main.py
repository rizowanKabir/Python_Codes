#Tuple, Dictionary & Set
l = []
for i in range(1,11):
    l.append(i)
print(l)

#Tuple comprehensive

 print(tuple(i for i in range(1, 11)))

# Dictionary

d1 = {"name":"Alex","age":20, "Gender":"male"}
d1 ["name"] = "Shagor"
print(d1)

d1 = {"name":"Alex","age":20, "Gender":"male"}

for i in d1:
    print(f"{i}:{d1[i]}")

# Using if condition

products = {"phone":10, "laptop":12, "Charger":100, "Headphone":0}

{key:value for (key,value) in products.items() if value > 0}
print(products)

# Restaurant Management System

menu = {
    "Coffe": 200,
    "Pasta": 150,
    "Pizza": 400,
    "Burger": 300,
}

print("------WELCOME TO THE RIZOWAN RESTAURANT------")
print(
    """
    coffe: 200 tk
    Pasta: 150 tk
    Pizza: 400 tk
    Burger: 300 tk
    """
)

item1 = input("Enter the item what you want order: ")
total_price = 0
if item1 in menu:
    total_price += menu[item1]
    print(f"Your order is {item1} & your total bill is {total_price} TK")
else:
    print("Invalid Item. Please try order from our menu")

another_item = input("Do you want add another item?(Yes/No): ").lower()
if another_item == "yes":
    item2 = input("Enter the second order what you want: ")
    if item2 in menu:
        total_price += menu[item2]
        print(f"You ordered {item2} & your total ordered is {total_price} TK")
    else:
        print("Invalid Item. Please try to order from our menu")
print(f"Your total amount is {total_price} TK. Thank You")






