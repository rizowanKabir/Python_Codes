# Billing Invoice

def display_invoice(name,amount,due_date):
    print(f"Hello {name}")
    print(f"Your bill is {amount:.2f} TK and your due date is {due_date}")
display_invoice("Nabil Hasan",4500,"10-11-2025")

# Name Creation
def create_name(first,last):
    first_name = first.capitalize()
    last_name = last.capitalize()
    return first_name + " " + last_name
full_name = create_name("Nabil", "Fucker")
print(full_name)

# Python banking program

def show_balance():
    print(f"Your balance is {balance:.2f} Tk")

def deposit():
    amount = float(input("Enter the deposit amount: "))
    if amount < 0:
        print("That's not valid amount")
        return 0
    else:
        return  amount

def withdraw():
    amount = float(input("Enter the withdraw amount: "))
    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than Zero")
        return 0
    else:
        print("Transaction Successful")
        return amount


balance = 0
is_running = True
while is_running:
    print("Welcome to the Bank")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter the choice (1-4): ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")

print("Thank you. Have a nice day !!!")
