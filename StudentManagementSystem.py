from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QInputDialog
)
import sys


class Student:
    def __init__(self, name, roll, age, parent_mobile, address):
        self.name = name
        self.roll = roll
        self.age = age
        self.parent_mobile = parent_mobile
        self.address = address


class StudentManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎓 Student Management System")
        self.setGeometry(100, 50, 1200, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #EAF0F6;
            }
            QLabel {
                font-size: 15px;
                color: #333;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #aaa;
                border-radius: 8px;
                background: white;
            }
            QPushButton {
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #007BFF, stop:1 #00C6FF);
                color: white;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0056b3, stop:1 #00aaff);
            }
            QTableWidget {
                background: white;
                border-radius: 8px;
                font-size: 14px;
            }
        """)

        self.students = []
        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # ===== Header Section =====
        header = QLabel("🎓 Welcome to Student Management System")
        header.setAlignment(QtCore.Qt.AlignCenter)
        header.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: white;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #007BFF, stop:1 #00C6FF);
                padding: 20px;
                border-radius: 12px;
            }
        """)
        main_layout.addWidget(header)

        # ===== Input Form =====
        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.roll_input = QLineEdit()
        self.roll_input.setPlaceholderText("Roll Number")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")

        self.parent_mobile_input = QLineEdit()
        self.parent_mobile_input.setPlaceholderText("Parent Mobile Number")

        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Address")

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.roll_input)
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(self.parent_mobile_input)
        form_layout.addWidget(self.address_input)

        main_layout.addLayout(form_layout)

        # ===== Buttons =====
        button_layout = QHBoxLayout()

        add_btn = QPushButton("➕ Add Student")
        add_btn.clicked.connect(self.add_student)

        update_btn = QPushButton("✏️ Update Student")
        update_btn.clicked.connect(self.update_student)

        delete_btn = QPushButton("🗑️ Delete Student")
        delete_btn.clicked.connect(self.delete_student)

        search_btn = QPushButton("🔍 Search Student")
        search_btn.clicked.connect(self.search_student)

        view_btn = QPushButton("📋 View All Students")
        view_btn.clicked.connect(self.view_students)

        for btn in [add_btn, update_btn, delete_btn, search_btn, view_btn]:
            btn.setMinimumWidth(160)
            button_layout.addWidget(btn)

        main_layout.addLayout(button_layout)

        # ===== Table =====
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Roll", "Age", "Parent Mobile", "Address"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            QHeaderView::section {
                background-color: #007BFF;
                color: white;
                font-weight: bold;
                border: none;
                padding: 6px;
            }
            QTableWidget::item:selected {
                background-color: #CCE5FF;
            }
        """)
        main_layout.addWidget(self.table)

    # ---------- Core Logic ---------- #
    def add_student(self):
        name = self.name_input.text().strip()
        roll = self.roll_input.text().strip()
        age = self.age_input.text().strip()
        parent_mobile = self.parent_mobile_input.text().strip()
        address = self.address_input.text().strip()

        if not (name and roll and age and parent_mobile and address):
            QMessageBox.warning(self, "Input Error", "Please fill all fields!")
            return
        if not roll.isdigit() or not age.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Roll and Age must be numeric!")
            return
        if self.search_by_roll(roll):
            QMessageBox.warning(self, "Duplicate", f"Roll {roll} already exists!")
            return

        student = Student(name, roll, age, parent_mobile, address)
        self.students.append(student)
        QMessageBox.information(self, "Success", f"Student {name} added successfully!")
        self.clear_inputs()
        self.view_students()

    def view_students(self):
        self.table.setRowCount(len(self.students))
        for row, s in enumerate(self.students):
            self.table.setItem(row, 0, QTableWidgetItem(s.name))
            self.table.setItem(row, 1, QTableWidgetItem(s.roll))
            self.table.setItem(row, 2, QTableWidgetItem(s.age))
            self.table.setItem(row, 3, QTableWidgetItem(s.parent_mobile))
            self.table.setItem(row, 4, QTableWidgetItem(s.address))

    def search_by_roll(self, roll):
        for s in self.students:
            if s.roll == roll:
                return s
        return None

    def search_student(self):
        roll, ok = QInputDialog.getText(self, "Search Student", "Enter Roll Number:")
        if ok and roll:
            student = self.search_by_roll(roll)
            if student:
                QMessageBox.information(
                    self, "Student Found",
                    f"Name: {student.name}\nRoll: {student.roll}\nAge: {student.age}\n"
                    f"Parent Mobile: {student.parent_mobile}\nAddress: {student.address}"
                )
            else:
                QMessageBox.warning(self, "Not Found", "Student not found!")

    def delete_student(self):
        roll, ok = QInputDialog.getText(self, "Delete Student", "Enter Roll Number:")
        if ok and roll:
            student = self.search_by_roll(roll)
            if not student:
                QMessageBox.warning(self, "Not Found", "Student not found!")
                return
            confirm = QMessageBox.question(
                self, "Confirm Delete",
                f"Delete student with Roll {roll}?",
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                self.students.remove(student)
                QMessageBox.information(self, "Deleted", "Student deleted successfully!")
                self.view_students()

    def update_student(self):
        roll, ok = QInputDialog.getText(self, "Update Student", "Enter Roll Number:")
        if not ok or not roll:
            return
        student = self.search_by_roll(roll)
        if not student:
            QMessageBox.warning(self, "Not Found", "Student not found!")
            return

        name, _ = QInputDialog.getText(self, "Update Name", "Enter New Name:", text=student.name)
        age, _ = QInputDialog.getText(self, "Update Age", "Enter New Age:", text=student.age)
        parent_mobile, _ = QInputDialog.getText(self, "Update Mobile", "Enter New Mobile:", text=student.parent_mobile)
        address, _ = QInputDialog.getText(self, "Update Address", "Enter New Address:", text=student.address)

        student.name = name or student.name
        student.age = age or student.age
        student.parent_mobile = parent_mobile or student.parent_mobile
        student.address = address or student.address

        QMessageBox.information(self, "Updated", f"Student (Roll {roll}) updated successfully!")
        self.view_students()

    def clear_inputs(self):
        self.name_input.clear()
        self.roll_input.clear()
        self.age_input.clear()
        self.parent_mobile_input.clear()
        self.address_input.clear()


def main():
    app = QApplication(sys.argv)
    window = StudentManagementSystem()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
