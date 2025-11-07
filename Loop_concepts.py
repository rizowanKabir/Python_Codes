# Loops are here
#while loop

i = 0
while i <= 10:
    print("Kabir")
    i += 1
print("Thank you")

#Multiplication Table using while loop

number = int(input("Enter the number:"))
i = 1
while i <=10:
    print(f"{i} x {number} = {i * number}")
    i += 1
print("This is multiplication table")

#Guessing Game

import random

secret_number = random.randint(1, 100)
counter = 1

while True:
    guess_number = input("Enter the guessing number (you can type 'quit' to exit): ").lower()

    if guess_number == "quit":
        break

    guess_number = int(guess_number)

    if guess_number == secret_number:
        print(f"Oh! Your guess was right. You win in {counter} attempts!! 🎉")
        break
    elif guess_number > secret_number:
        print("Wrong, please try a lower number.")
    else:
        print("Wrong, please try a bigger number.")

    counter += 1

print("------- Game Over --------")

# For loop & nested loop

for i in range(1,5):
    for j in range(1,5):
        print("Kabir",i,"sohag",j)

# for loop triangle print

row = int(input("Enter the row number: "))

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")

row = int(input("Enter number of rows: "))

for i in range(row):
    print("*" * (i + 1))




