# Function
def check(num):
    return "Even" if num % 2 == 0 else "Odd"
print(check(2),check(3))
# tuple

t = (1,2,3,4)
a, *b, c= t
print(a,b,c)
# List

nums = [1,2,3,4,5]
print(nums[::-1][1])
# list

data = [1,2,3]
result = data
result.append(4)
if result == data:
    print("same")
else:
    print("Different")

# for loop
s = "banana"
count = 0
for ch in s:
    if ch == "a":
        count += 1
    if ch == 2:
        break
print(count)

#
word = "hello"
if "h" in word:
    if "e" in word:
        print("yes")
    else:
        print("Maybe")
else:
    print("No")

print(type(None))

love = input("Please enter the word: ")
if love == "real":
    print("please Welcome into my heart")
else:
    print("Stay away !! ")


x = ("uniathena",500, 'education') #  Tuple unpacking
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)

# 1️⃣ Reverse String
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))

# ✅ Method 2 (using Loop)
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
print(reverse_string("HELLO"))

class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
            self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(1000)
print(account.get_balance())

square = lambda x: x*x
print(square)

try:
    x = int("abc")
except ValueError:
    print("Invalid errors")
finally:
    print("Done")








































