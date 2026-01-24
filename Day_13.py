class Robot:
    def __init__(self,robot_number):
        self.robot_number = robot_number
    def movement(self):
        print(f"Robot for movement {self.robot_number}")

    def fire_detect(self):
        print(f"Robot for movement {self.robot_number}")
    def wheel_control(self):
        print(f"Robot for movement {self.robot_number}")

robot1 = Robot(robot_number=1)
robot1.movement()
robot1.fire_detect()

# Create a Student class with name and age. Create an object and print details.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj1 = Student("Rizowan",25)
print(obj1.name, obj1.age)

# Create a Car class with brand and a method start().
class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        return (f"Car is starting {self.brand}")
b1 = Car("Toyota")
print(b1.start())

# Problem 1: Create a Dog class with name, breed, and age
# Task: Create objects and make the dog bark

print("      Problem 1: Dog class")
print("-" * 50)

class Dog:
    def __init__(self,name,breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} sys waaf"
    def info(self):
        return f"{self.name} is a {self.age} year old {self.breed}"
dog1 = Dog("Buddy", 3, "golden barbi")
dog2 = Dog("Max", 5, "Helio")

print(dog1.bark())
print(dog1.info())
print(dog2.info())

# Problem 2: Library Management - Book class
# Task: Track books with title, author, ISBN, and availability
print("      Problem-2 Class Book")
print("=" * 50)

class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} is book has been borrowed"
        return f"{self.title} is not available"
    def return_book(self):
        self.is_available = True
        return f"{self.title} has been returned"

    def display(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

book1 = Book("python course","Rizowan","017731554678")
print(book1.borrow())
print(book1.return_book())
print(book1.is_available)

# Problem 3: Calculator class
# Task: Create a calculator with basic operations
print("\n" + "="*50)
print("Problem 3: Calculator Class")
print("-" * 50)

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,a,b):
        self.result = a + b
        return self.result
    def subtract(self,a,b):
        self.result = a - b
        return self.result
    def multiplication(self,a,b):
        self.result = a * b
        return self.result
    def divide(self,a,b):
        if b == 0:
            return "Error: Division by zero"
        self.result = a / b
        return self.result
    def get_result(self):
        return  self.result
calu = Calculator()
print(f"10 + 5 = {calu.add(10,5)}")
print(f"10 - 5= {calu.subtract(10, 5)}")




































