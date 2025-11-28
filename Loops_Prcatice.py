# 1. Email Validator (String Filtering + Loops)
# Real-world use: Used in signup forms or data cleaning tasks.
# Check if a given email is valid — must contain “@” and end with “.com” or “.org”.

email = input("Please enter your email: ")

count = 0
check_1 = False
check_2 = False

for i in email:
    count += 1
    if i == "@":
        break
if count > 1:
    check_1 = True
if email[-4:] == ".com" or email[-4:] == ".org":
    check_2 = True
if check_1 & check_2:
    print(f"{email} this is Valid Email")
else:
    print(f"{email} this is Invalid email")


# 2. Count Word Frequency in Customer Reviews
# Real-world use: Analyzing reviews or comments in text analytics.
# Given a review text, count how many times each word appears (ignore case).

text = input("Please enter the review: ").lower()

words = text.split()
frequency = {}
for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1
print(frequency)

# 3. Password Strength Checker
# Real-world use: Used in user authentication systems.
# Check if a password is strong — must have at least one uppercase, one lowercase, one digit, and one
# special character.
# Input: "Hello@123"
# Output: Strong Password

password = input("Please enter the password: ")
count_strength = 0
special_chars = "!@#$%^&*()_+-=<>?/.,"

for ch in password:
    if ch.isupper():
        count_strength += 1
        break
for ch in password:
    if ch.islower():
        count_strength += 1
        break
for ch in password:
    if ch.isdigit():
        count_strength += 1
        break
for ch in password:
    if ch in special_chars:
        count_strength += 1
        break
if count_strength == 4:
    print(f"{password} this is strong password")
else:
    print(f"{password} this is weak password !!")

# 4. Username Generator
# Real-world use: Automatically create usernames for users.
# Take user’s full name and generate a short username.
# Rules: first 3 letters of first name + last 3 letters of last name + random number (use loops only).
# Input: "Mamun Malitha"
# Output: mamitha57

import time

full_name = input("Enter Your Name: ")

full_name_lower = full_name.lower()
name_parts = full_name_lower.split(" ")

first_name = name_parts[0]
last_name = name_parts[-1]

username_part1 = ""
username_part2 = ""
random_part = ""

i = 0
while i < 3:
    if i < len(first_name):
        username_part1 = username_part1 + first_name[i]
    else:
        break
    i = i + 1

last_name_length = len(last_name)
start_index = last_name_length - 3

j = 0
while j < 3:
    current_index = start_index + j

    if current_index >= 0 and current_index < last_name_length:
        username_part2 = username_part2 + last_name[current_index]
    else:
        break
    j = j + 1

current_time = time.time()
time_str = str(current_time)
decimal_found = False
k = 0
digit_count = 0

while k < len(time_str) and digit_count < 2:
    if time_str[k] == '.':
        decimal_found = True
    elif decimal_found:
        random_part = random_part + time_str[k]
        digit_count = digit_count + 1
    k = k + 1

while len(random_part) < 2:
    random_part = random_part + "0"

final_username = username_part1 + username_part2 + random_part

print(final_username)

# 5. SMS Word Counter
# Real-world use: Used in messaging apps or social media post limit check.
# Count how many characters and words are in a message, and tell if it exceeds 160 characters (SMS limit).
# Input: "This is a demo message."
# Output: Words = 5, Characters = 23, Status = Within Limit

message = input("Please enter the message here: ")

words = message.split()
char = len(message)
if char <= 160:
    print("Status = ", "Message Within Limit")
else:
    print("Status = ", "Message Without Limit")
print(f"These words: {words} & length of words: {len(words)}")
print(f"The count of message: {char}")

# 6. Remove Duplicates from Contact List
# Real-world use: Data cleaning in CRM or user databases.
# Given a list of names (comma separated), remove duplicates.
# Input: "Rahim, Karim, Rahim, Sultana"
# Output: "Rahim, Karim, Sultana"

contacts = input("Enter the name separated by coma: ").split()

unique_list = []
for name in contacts:
    name = name.strip()
    if name not in unique_list:
        unique_list.append(name)
print("Unique Contacts: "," ," .join(unique_list) )

# 7. Detect Suspicious Words in Text (Moderation)
# Real-world use: Used in chat moderation or email filtering.
# If any “banned” words like ['spam', 'scam', 'fake'] are found in a text, print “Warning”.
# Input: "This is a scam offer"
# Output: Warning: Suspicious content detected

banned_word = ['spam', 'scam', 'fake']
text = input("Enter the text here please: ").lower()
warning = False
for word in banned_word:
    if word in text:
        warning = True
        break
if warning:
    print("Warning: Suspicious Content detected")
else:
    print("Text is  safe")

# 8. Invoice Code Formatter
#  Real-world use: Formatting IDs or codes in finance or ERP systems.
# Given an invoice number like 23, generate code in the format INV00023.
# Input: 23
# Output: INV00023

invoice_number = int(input("Enter the invoice number here: "))
formatted_code = "INV" + str(invoice_number).zfill(5)

print("Invoice Code is: ", formatted_code)

# 9. Count Hashtags and Mentions (Social Media Analytics)
#  Real-world use: Used in analyzing social media posts.
# Count how many hashtags (#) and mentions (@) appear in a post.
# Input: "Check out #AIWorkshop and follow @inceptionbd"
# Output: Hashtags = 1, Mentions = 1

post = input("Enter the social post here: ")
hashtags = 0
mention = 0

for ch in post:
    if ch == "#":
        hashtags += 1
    elif ch == "@":
        mention += 1
print(f"Total hashtags: {hashtags} & total mention: {mention}

# 10. Word Reversal for Data Encryption
# Real-world use: Simple text obfuscation or playful encoding.
# Reverse each word in a sentence while keeping word order the same.
# Input: "AI is fun"
# Output: "IA si nuf"

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = []

for word in words:
    reversed_word = ""
    for ch in word:
        reversed_word = ch + reversed_word
    reversed_words.append(reversed_word)

print("Encrypted Text:", " ".join(reversed_words))






















































