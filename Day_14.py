# Problem 1: Bank Account Class
# Create a BankAccount class with deposit, withdraw, and check balance method
"""class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit amount ${amount} & New balance ${self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        elif amount > 0:
            self.balance =- amount
            print(f"Withdraw amount ${amount} & current balance is ${self.balance}")
        else:
            print("Invalid withdraw balance")
    def check_balance(self):
        print(f"Account holder {self.account_holder} & check balance {self.balance}")
        return self.balance
account = BankAccount("Rizowan Kabir", 120000)
account.deposit(10000)
account.check_balance()"""

# Problem 2: Student Class with Grade Calculation
# Create a Student class that stores grades and calculates average
"""class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self,grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Grade {grade} added for {self.name}")
        else:
            print("Invalid input number must be between 0 & 100")
    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    def display_info(self):
        avg = self.calculate_average()
        print(f"student {self.name} & (ID:{self.student_id})")
        print(f"Grade {self.grades}")
        print(f"Average {avg:.2f}")
student = Student("Ovey","20303026")
student.add_grade(85)
student.add_grade(100)
student.add_grade(89)
student.display_info()
print()"""
# Problem 3: Rectangle Class with Area and Perimeter
# Create a Rectangle class with methods to calculate area and perimeter
"""class Rectangle:
    def __init__(self,length,width):
        self.length =  length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def display_info(self):
        print(f"Rectangle {self.length} X {self.width}")
        print(f"Area {self.area()}")
        print(f"Perimeter {self.perimeter()}")
rect = Rectangle(5,3)
rect.display_info()"""

# Problem 4: Car Class with Inheritance
# Create a base Vehicle class and a Car subclass
"""class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"Drove {miles} miles. Total mileage: {self.mileage}")

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}, Mileage: {self.mileage}")


# Test Problem 4
print("=== Problem 4: Car with Inheritance ===")
car = Car("Toyota", "Camry", 2022, 4)
car.display_info()
car.drive(150)
car.drive(75)
print()"""

# Problem 6: Employee Class with Salary Calculation
# Create an Employee class with different types of employees









































