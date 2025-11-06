# This is oop concept

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} {self.year}")
obj = Car("TATA","HondaXmotion",2025)
obj.display_info()

# Print numbers from 1 to 10
for i in range(1,11):
    print(i)

# Print numbers from 1 to 10 (while loop)

i = 1
while i <= 10:
    print(i)
    i += 1

# Print numbers from 1 to 10(using function)

def print_number():
    for i in range(1,11):
        print(i)
print_number()
# Print even numbers from 1 to 20
def print_number():
    for i in range(2,21,2):
        print(i)
print_number()

# Calculate the sum of numbers from 1 to N

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Rizowan Kabir"))  # Output: 5
