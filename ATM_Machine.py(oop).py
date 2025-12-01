class AtmMachine:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
            Hi, How Can I help you
            1. Press 1 to Create pin
            2. Press 2 to Change pin
            3. Press 3 to Check Balance 
            4. Press 4 to Withdraw balance
            5. Anything to Exit 
            Please Choice one Option to move forward: 
            """
        )

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw_balance()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter the PIN: ")
        self.pin = user_pin

        user_balance = float(input("Enter the Balance here: "))
        self.balance = user_balance
        print("Pin Created Successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter the old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter the new pin here: ")
            self.pin = new_pin
            print("Pin Changed Successfully")
        else:
            print("Incorrect Pin !!")
        self.menu()
    def check_balance(self):
        user_pin = input("Enter the pin here: ")
        if user_pin == self.pin:
            print("Your Balance is TK", self.balance)
        else:
            print("Incorrect Pin. Please try to give right pin !!")
        self.menu()
    def withdraw_balance(self):
        user_pin = input("Enter the pin here: ")
        if user_pin == self.pin:
            amount = float(input("Enter the withdraw amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have withdraw {amount} Tk. Your current Balance is {self.balance} TK")
            else:
                print("Insufficient Balance")
        else:
            print("Please try to give correct pin")

        self.menu()


atm = AtmMachine()