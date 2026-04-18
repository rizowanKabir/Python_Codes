# print(Arithmetic operations)
"""a = 3
b = 6
print("addition:" ,a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division", a / b)
print("Floor Division:", a // b)
print("Module", a % b)
print("Exponential", a ** b)"""

# print(String Basic slicing)

"""message = " hello python welcome to the my world 101 "
print(message)
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())
print(message.swapcase())
print(message.find("hello"))
print(message.index("python"))
print(message.count("o"))
print(message.startswith("hello"))
print(message.endswith("101"))
print(message.strip()) # remove two side space
print(message.lstrip())
print(message.rstrip())
print(message.isdigit())
print(message.isalpha())
print(message.isnumeric())
print(message.isalnum())
print(len(message))

# slicing
print(message[1:10])
print(message[1:])
print(message[8:])"""

# Exercise

"""msg = "welcome to python 101: strings"
msg1 = msg[18]+' '+ msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1)
print(msg1[::-1].title())"""

# string quotation
"""msg = 'welcome to python 101: strings'
print(msg.find("python"))
print(msg.replace("python",'java'))
print("python" in msg)
print("python" not in msg)"""

# Racing analyser
"""total_race_time = float(input("Enter the total race time(in second): "))
num_pit_stop = float(input("Enter the number of pit stop: "))
avg_pit_duration = float(input("Enter the average pit stop duration (in second): "))
# calculation
total_pit_time = num_pit_stop * avg_pit_duration
pit_percentage = (total_pit_time / total_race_time) * 100
pit_percentage = round(pit_percentage,2)
# print the result
print("------Pit the summary-------")
print(f"Total pit time: {total_pit_time} seconds")
print(f"Percentage of race in pits: {pit_percentage} %")
# Optional feedback
if pit_percentage > 5:
    print("You need a new pit crew")"""

# List
friends = ["Atik","Ovey","Shawon","Shakil","Shagor"]
print(friends[0])
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
cars = [10,20,50,70,90,100]
print(min(cars))
print(max(cars))
print(sum(cars))
friends.append("Nabil")
print(friends)
friends.insert(0,"Sobuj")
print(friends)
friends.extend(cars)
print(friends)
friends.remove("Sobuj")
print(friends)
friends.pop(1)
print(friends)


























