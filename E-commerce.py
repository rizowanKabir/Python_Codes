import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QSpinBox, QMessageBox, QInputDialog, QLineEdit, QSlider, QTabWidget, QFileDialog, QFrame
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from reportlab.pdfgen import canvas
import os  # <-- Important for path handling

# Product data with images (filename only)
products = {
    "Electronics": {
        "Laptop": {"price": 70000, "image": "laptop.png"},
        "Phone": {"price": 30000, "image": "phone.png"},
        "Monitor": {"price": 12000, "image": "monitor.png"},
        "Printer": {"price": 7000, "image": "printer.png"}
    },
    "Accessories": {
        "Keyboard": {"price": 1500, "image": "keyboard.png"},
        "Mouse": {"price": 800, "image": "mouse.png"},
        "USB Cable": {"price": 300, "image": "usb.png"},
        "Power Bank": {"price": 1500, "image": "powerbank.png"}
    },
    "Gadgets": {
        "Headphones": {"price": 2000, "image": "headphones.png"},
        "WebCam": {"price": 3500, "image": "webcam.png"},
        "Microphone": {"price": 2500, "image": "mic.png"},
        "Speakers": {"price": 4000, "image": "speakers.png"}
    }
}

cart = {}
loyalty_points = 0


class ProfessionalECommerce(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 Professional E-Commerce App")
        self.setGeometry(50, 50, 1200, 700)
        self.setStyleSheet("background-color:#1e1e2f; color:#f0f0f0;")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Left: Tabs for categories
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {border: 1px solid #444;}
            QTabBar::tab {background: red; color: black; padding: 10px; border-top-left-radius:5px; border-top-right-radius:5px;}
            QTabBar::tab:selected {background: darkred; color: white;}
        """)
        self.tab_widgets = {}
        for category in products:
            tab = QWidget()
            tab.layout = QVBoxLayout()
            tab.setLayout(tab.layout)
            self.tab_widgets[category] = tab
            self.tabs.addTab(tab, category)
        self.layout.addWidget(self.tabs, 70)

        # Right: Cart Summary Panel
        self.cart_panel = QFrame()
        self.cart_panel.setStyleSheet("background-color:#2c3e50; border-radius:10px;")
        self.cart_layout = QVBoxLayout()
        self.cart_panel.setLayout(self.cart_layout)
        self.layout.addWidget(self.cart_panel, 30)

        self.cart_label = QLabel("🛍️ Cart Summary")
        self.cart_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.cart_layout.addWidget(self.cart_label)

        self.cart_table = QTableWidget()
        self.cart_table.setColumnCount(3)
        self.cart_table.setHorizontalHeaderLabels(["Item", "Qty", "Remove"])
        self.cart_layout.addWidget(self.cart_table)

        # Discount Slider
        self.discount_slider = QSlider(Qt.Horizontal)
        self.discount_slider.setRange(0, 25)
        self.discount_slider.valueChanged.connect(self.update_summary)
        self.cart_layout.addWidget(QLabel("Discount (%)"))
        self.cart_layout.addWidget(self.discount_slider)

        # Summary
        self.summary_label = QLabel()
        self.summary_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.cart_layout.addWidget(self.summary_label)

        # Checkout Button
        self.checkout_btn = QPushButton("💳 Checkout")
        self.checkout_btn.clicked.connect(self.checkout)
        self.checkout_btn.setStyleSheet("""
            QPushButton{background-color:#c0392b;color:white;font-weight:bold;padding:10px;border-radius:5px;}
            QPushButton:hover{background-color:#e74c3c;}
        """)
        self.cart_layout.addWidget(self.checkout_btn)

        # Populate Products in Tabs
        self.load_products_tabs()
        self.update_summary(animated=True)

    def load_products_tabs(self):
        # Current directory
        img_folder = os.path.join(os.getcwd(), "images")

        for category, tab in self.tab_widgets.items():
            tab.layout.addStretch()
            for name, info in products[category].items():
                h_layout = QHBoxLayout()

                # Image label
                img_label = QLabel()
                img_path = os.path.join(img_folder, info["image"])
                if os.path.exists(img_path):
                    pix = QPixmap(img_path).scaled(60, 60, Qt.KeepAspectRatio)
                else:
                    pix = QPixmap(60, 60)
                    pix.fill(Qt.gray)  # fallback gray box if image missing
                img_label.setPixmap(pix)
                h_layout.addWidget(img_label)

                # Product Name + Price
                label = QLabel(f"{name} - {info['price']} Tk")
                label.setFont(QFont("Arial", 12))
                h_layout.addWidget(label)

                # Quantity SpinBox
                qty_spin = QSpinBox()
                qty_spin.setRange(1, 100)
                h_layout.addWidget(qty_spin)

                # Add Button
                add_btn = QPushButton("➕ Add")
                add_btn.clicked.connect(lambda _, n=name, q=qty_spin: self.add_to_cart(n, q.value(), info["price"]))
                add_btn.setStyleSheet("background-color:#27ae60;color:white;")
                h_layout.addWidget(add_btn)

                tab.layout.addLayout(h_layout)

    def add_to_cart(self, name, qty, price):
        global cart
        if name in cart:
            cart[name]["qty"] += qty
        else:
            cart[name] = {"qty": qty, "price": price}
        self.refresh_cart_table()
        self.update_summary(animated=True)

    def refresh_cart_table(self):
        self.cart_table.setRowCount(len(cart))
        for row, (item, data) in enumerate(cart.items()):
            self.cart_table.setItem(row, 0, QTableWidgetItem(item))
            self.cart_table.setItem(row, 1, QTableWidgetItem(str(data["qty"])))
            remove_btn = QPushButton("🗑")
            remove_btn.clicked.connect(lambda _, i=item: self.remove_item(i))
            self.cart_table.setCellWidget(row, 2, remove_btn)
        self.cart_table.resizeColumnsToContents()

    def remove_item(self, item):
        global cart
        if item in cart: del cart[item]
        self.refresh_cart_table()
        self.update_summary(animated=True)

    def update_summary(self, animated=False):
        global loyalty_points
        subtotal = sum(d["price"] * d["qty"] for d in cart.values())
        discount_percent = self.discount_slider.value()
        discount = subtotal * discount_percent / 100
        tax = 0.05 * (subtotal - discount)
        total = subtotal - discount + tax
        points_earned = int(total // 1000) * 10
        if animated:
            self.animate_value(0, total, points_earned)
        else:
            self.summary_label.setText(
                f"Subtotal:{subtotal} | Discount:{discount:.2f} | Tax:{tax:.2f} | Total:{total:.2f} | Points:{points_earned} | Loyalty:{loyalty_points}")

    def animate_value(self, start, end, points):
        steps = 50
        step_value = (end - start) / steps
        self.current_value = start

        def update_label():
            self.current_value += step_value
            if self.current_value >= end:
                self.current_value = end
                self.summary_label.setText(f"Total: {self.current_value:.2f} | Points:{points}")
                timer.stop()
            else:
                self.summary_label.setText(f"Total: {self.current_value:.2f} | Points:{points}")

        timer = QTimer()
        timer.timeout.connect(update_label)
        timer.start(10)

    def checkout(self):
        global cart, loyalty_points
        if not cart:
            QMessageBox.information(self, "Checkout", "Cart is empty!")
            return
        subtotal = sum(d["price"] * d["qty"] for d in cart.values())
        discount = subtotal * self.discount_slider.value() / 100
        tax = 0.05 * (subtotal - discount)
        total = subtotal - discount + tax
        points_earned = int(total // 1000) * 10
        loyalty_points += points_earned

        # PDF Receipt
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Receipt", "", "PDF Files (*.pdf)")
        if file_path:
            c = canvas.Canvas(file_path)
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, 800, "🛒 Professional Shopping Receipt")
            y = 770
            c.setFont("Helvetica", 12)
            for item, d in cart.items():
                c.drawString(50, y, f"{item} x {d['qty']} = {d['price'] * d['qty']} Tk")
                y -= 20
            c.drawString(50, y, f"Subtotal:{subtotal} Tk");
            y -= 20
            c.drawString(50, y, f"Discount:{discount:.2f} Tk");
            y -= 20
            c.drawString(50, y, f"Tax:{tax:.2f} Tk");
            y -= 20
            c.drawString(50, y, f"Total:{total:.2f} Tk");
            y -= 20
            c.drawString(50, y, f"Points Earned:{points_earned}");
            y -= 20
            c.drawString(50, y, f"Loyalty Points:{loyalty_points}");
            y -= 20
            c.save()
            QMessageBox.information(self, "Receipt Saved", f"Receipt saved to {file_path}")

        QMessageBox.information(self, "Checkout",
                                f"✅ Checkout Successful\nTotal:{total:.2f} | Points Earned:{points_earned}")
        cart.clear()
        self.refresh_cart_table()
        self.update_summary(animated=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfessionalECommerce()
    window.show()
    sys.exit(app.exec_())
