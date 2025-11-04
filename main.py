# ATM Simulation

menu = input(""" 
Hi there!! Welcome to ATM Simulation
Please enter what option you want

1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdraw 
4. Enter 4 for Deposite 
5. Enter 5 for Exit
""")
print(menu)

if menu == "1":
  print("Please change your pin")
elif menu == "2":
  print("Here you can check your balance")
elif menu == "3":
  print("Here you can withdraw")
elif menu == "4":
  print("Here you can Deposit")
else:
  print("Exit")

# Find the minimum number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 < num2 and num1 < num3:
  print(f"Minimum number is: {num1}")
elif num2 < num1 and num2 < num3:
  print(f"Minimum number is: {num2}")
else:
  print(f"Minimum number is: {num3}")

#Login function
email = input("Enter the email here: ")
password = input("Enter the password here: ")

actual_email = "sohagrizowan@gmail.com"
actual_password = "kabir001"
if email == actual_email and password == actual_password:
  print("Login Successfull !!")
elif email == actual_email and password != actual_password:
  print("Please try again !!")
  password = input("Enter the password again: ")

  if password == actual_password:
    print("Login Succefull!!")
  else:
    print("Wrong!! Password")


else:
  print("Wrong Crdential. Try right one please!!")


