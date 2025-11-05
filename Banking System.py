import tkinter as tk
from tkinter import messagebox
import time

balance = 0.0
transactions = []

def update_balance_label():
    balance_label.config(text=f"Current Balance: {balance:.2f} Tk")


def deposit_money():
    global balance
    amount = amount_entry.get()
    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Invalid", "Amount must be greater than 0!")
            return
        balance += amount
        transactions.append((time.strftime("%Y-%m-%d %H:%M:%S"), "Deposit", amount))
        update_balance_label()
        messagebox.showinfo("Success", f"Deposited {amount:.2f} Tk successfully!")
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid", "Please enter a valid number!")


def withdraw_money():
    global balance
    amount = amount_entry.get()
    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Invalid", "Amount must be greater than 0!")
        elif amount > balance:
            messagebox.showerror("Error", "Insufficient Balance!")
        else:
            balance -= amount
            transactions.append((time.strftime("%Y-%m-%d %H:%M:%S"), "Withdraw", amount))
            update_balance_label()
            messagebox.showinfo("Success", f"Withdrawn {amount:.2f} Tk successfully!")
            amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid", "Please enter a valid number!")


def show_history():
    if not transactions:
        messagebox.showinfo("History", "No transactions yet.")
        return

    history_window = tk.Toplevel(root)
    history_window.title("Transaction History")
    history_window.geometry("500x400")
    tk.Label(history_window, text=" Transaction History", font=("Arial", 14, "bold")).pack(pady=10)

    text = tk.Text(history_window, wrap="none", font=("Consolas", 11))
    text.pack(fill=tk.BOTH, expand=True)

    for t in transactions:
        text.insert(tk.END, f"{t[0]} | {t[1]:<8} | {t[2]:.2f} Tk\n")

    text.config(state="disabled")


def show_summary():
    total_deposit = sum(t[2] for t in transactions if t[1] == "Deposit")
    total_withdraw = sum(t[2] for t in transactions if t[1] == "Withdraw")

    summary_msg = (
        f" Account Summary\n\n"
        f"Total Deposited: {total_deposit:.2f} Tk\n"
        f"Total Withdrawn: {total_withdraw:.2f} Tk\n"
        f"Current Balance: {balance:.2f} Tk"
    )

    messagebox.showinfo("Account Summary", summary_msg)


def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


# ---------- Main Window ----------
root = tk.Tk()
root.title("Python Banking System")
root.geometry("600x450")
root.configure(bg="#f0f0f0")

# ---------- UI Elements ----------
tk.Label(root, text="Welcome to Python Bank", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

balance_label = tk.Label(root, text=f"Current Balance: {balance:.2f} Tk", font=("Arial", 14), bg="#f0f0f0")
balance_label.pack(pady=10)

tk.Label(root, text="Enter Amount:", font=("Arial", 12), bg="#f0f0f0").pack()
amount_entry = tk.Entry(root, font=("Arial", 12), justify="center")
amount_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Deposit", font=("Arial", 12, "bold"), bg="green", fg="white",
          width=12, command=deposit_money).grid(row=0, column=0, padx=10, pady=5)

tk.Button(button_frame, text="Withdraw", font=("Arial", 12, "bold"), bg="orange", fg="white",
          width=12, command=withdraw_money).grid(row=0, column=1, padx=10, pady=5)

tk.Button(button_frame, text="History", font=("Arial", 12, "bold"), bg="blue", fg="white",
          width=12, command=show_history).grid(row=1, column=0, padx=10, pady=5)

tk.Button(button_frame, text="Summary", font=("Arial", 12, "bold"), bg="purple", fg="white",
          width=12, command=show_summary).grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="red", fg="white",
          width=15, command=exit_app).pack(pady=20)

root.mainloop()
