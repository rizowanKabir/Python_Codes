
students = {}

def add_student():
    name = input("Enter the student name: ").strip()
    mark = float(input("Enter the marks: "))
    students[name] = mark
    print("Student added successfully\n")

def search_student():
    name = input("Enter the student name to search: ").strip()
    if name in students:
        print(f"{name}'s marks: {students[name]}\n")
    else:
        print("student not found\n")

def update_student():
    name = input("Enter the student name: ")
    if name in students:
        marks = float(input("Enter the new marks: "))
        students[name] = marks
        print("Student updated successfully\n")
    else:
        print("Student not found\n")

def delete_student():
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")


def show_all_students():
    if students:
        print("\nAll Students:")
        for name, marks in students.items():
            print(f"Name: {name}, Marks: {marks}")
        print()
    else:
        print("No students found!\n")


print("===== STUDENT MANAGEMENT SYSTEM =====")

while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        show_all_students()
    elif choice == 6:
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice! Please choose between 1 to 6.\n")
