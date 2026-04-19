# split & join Exercise

csv = 'sohag,shakil,shagor,sobuj,sadhin'
print(','.join(csv.split(',')))
print(type(csv))
friend_list = ['Exercise: file with me']
print(friend_list)

# Tuple faster than list but it can't change
friend = ['shakil','sohag','shagor','munna','sobuj']
friend_tuple = ('shakil','sohag','shagor','munna','sobuj')

print(friend[1:4])
print(friend_tuple[1:4])

# sets
friend = ['shakil','sohag','shagor','munna','sobuj']
friend_tuple = ('shakil','sohag','shagor','munna','sobuj')
friend_sets = {'shakil','sohag','shagor','munna','sobuj','shakil'}
friends_new = {'shakil','rizowan','shagor','ovey','sobuj','shakil'}
print(friend_sets.intersection(friends_new))
print(friend_sets.difference(friends_new))
print(friend_sets.union(friends_new))

# Function
print("Hello Function & Return")

def value_added_tax(amount):
    tax = amount * 0.25
    return tax
result = value_added_tax(100)
print(result + 10)

# if\else\elif\condition
mode = input("Enter operation (+, -, *, /) or f for Celsius→Fahrenheit: ").lower()

if mode == "f":
    num_1 = float(input("Enter Celsius value: "))
    fahrenheit = (num_1 * 9 / 5) + 32
    print(f"{num_1}°C = {fahrenheit}°F")

elif mode in ["+", "-", "*", "/"]:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))

    if mode == "+":
        print(f"Answer: {num_1 + num_2}")
    elif mode == "-":
        print(f"Answer: {num_1 - num_2}")
    elif mode == "*":
        print(f"Answer: {num_1 * num_2}")
    elif mode == "/":
        if num_2 == 0:
            print("Error: Division by zero")
        else:
            print(f"Answer: {num_1 / num_2}")

else:
    print("Invalid input ")

# while loops
# guessing Game

print("========Guessing Game=========")

num = 76
guess_limit = 4
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("Enter your guess (1-100): "))
    guess_count += 1

    if guess == num:
        print(f"{guess} You win! 🎉")
        break
    elif guess > num:
        print("Too high ❌")
    else:
        print("Too low ❌")

else:
    print(f"Sorry, you lose 😢. The number was {num}")

# For loops
for letter in 'Noregain blue':
    print(letter)
print("For loop done")

names = ['john','CLEEse','Eric IDLE','michale']
names_1 = ['Graham Chapman','TERRY','Terry jones']
msg = 'You are invited to the party on saturday'

names.extend(names_1)
for _ in range(2):
    names.append(input("Enter a new names: "))
for name in names:
    msg1 = f"{name.title()} ! {msg}"
    print(msg1)
    
# Access Controller scan system

revoked_badges = ["X123","B789","Z999"]

approved = []
denied = []

while True:
    name = input("Enter a person name or ( type done to finish): ")
    if name.lower() == "done":
        break
    badges = input("Enter the badges number: ").strip().upper()

    if badges in revoked_badges:
        denied.append(name)
        print(f"[Access Denied] {name} - Revoked Badges")
    else:
        approved.append(name)
        print(f"[ACCESS Granted] {name}")

print("========Access Summary========")

print("Approved Visitors:!!")
for person in sorted(approved):
    print(f" - {person}")

print("Denied Visitors:!!")
for person in sorted(denied):
    print(f"- {person}")

print(f"Total approved: {len(approved)}")
print(f"Total Denied: {len(denied)}")

# Loyalty Point Engine Challenge

purchases = [23.0,233,455]

def earn_points(price):
    whole_dollar = int(price)
    return whole_dollar * 3

def tier_labels(points):
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"

total_spent = 0.0
total_points = 0

for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)

final_tiers = tier_labels(total_points)

print("======loyalty Summary=========")
print(f"Total spent: BDT {total_spent:.2f}")
print(f"Total Points: {total_points}")
print(f"Tier achieved: {final_tiers}")

# Dictionary

movie = {
    'title':'prince',
    'year':2026,
    'cast': ['shakib khan','jutirmoy','fahrin']
}
for key,value in movie.items():
    print(key,value)

# 































