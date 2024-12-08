import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import random

# Database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="PASSWORD",  # Replace with your database password
    database="bank_management",
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = connection.cursor()

# Functions
def create_account():
    username = username_entry.get()
    contact_no = contact_entry.get()
    amount = amount_entry.get()
    city = city_entry.get()
    state = state_entry.get()

    if not username or not contact_no or not amount or not city or not state:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        amount = float(amount)
        if amount < 1000:
            messagebox.showerror("Error", "Minimum amount must be ₹1000.")
            return

        account_number = str(random.randint(1000000000, 9999999999))
        query = """
        INSERT INTO customers (account_number, username, contact_no, amount, city, state) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (account_number, username, contact_no, amount, city, state)
        mycursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Success", f"Account created successfully! Your Account Number: {account_number}")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount!")

def login():
    username = login_username_entry.get()
    account_number = login_account_entry.get()

    if not username or not account_number:
        messagebox.showerror("Error", "All fields are required!")
        return

    query = "SELECT * FROM customers WHERE username=%s AND account_number=%s"
    mycursor.execute(query, (username, account_number))
    result = mycursor.fetchone()

    if result:
        show_dashboard(result)
    else:
        messagebox.showerror("Error", "Account not found!")

# Utility Functions
def clear_entries():
    username_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)

def show_dashboard(user):
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("400x350")

    tk.Label(dashboard, text=f"Welcome, {user['username']}!", font=("Arial", 16)).pack(pady=10)
    
    def credit_amount():
        amount = credit_entry.get()
        if not amount:
            messagebox.showerror("Error", "Enter an amount to credit.")
            return
        
        try:
            amount = float(amount)
            query = "UPDATE customers SET amount = amount + %s WHERE account_number=%s"
            mycursor.execute(query, (amount, user['account_number']))
            connection.commit()
            messagebox.showinfo("Success", f"₹{amount} credited successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount!")

    def debit_amount():
        amount = debit_entry.get()
        if not amount:
            messagebox.showerror("Error", "Enter an amount to debit.")
            return
        
        try:
            amount = float(amount)
            if amount > user['amount']:
                messagebox.showerror("Error", "Insufficient balance!")
                return

            query = "UPDATE customers SET amount = amount - %s WHERE account_number=%s"
            mycursor.execute(query, (amount, user['account_number']))
            connection.commit()
            messagebox.showinfo("Success", f"₹{amount} debited successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount!")

    def delete_account():
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this account?")
        if confirm:
            query = "DELETE FROM customers WHERE account_number=%s"
            mycursor.execute(query, (user['account_number'],))
            connection.commit()
            messagebox.showinfo("Deleted", "Account deleted successfully!")
            dashboard.destroy()

    # Display user info
    tk.Label(dashboard, text=f"Account Number: {user['account_number']}").pack()
    tk.Label(dashboard, text=f"Contact No: {user['contact_no']}").pack()
    tk.Label(dashboard, text=f"Balance: ₹{user['amount']}").pack()
    tk.Label(dashboard, text=f"City: {user['city']}").pack()
    tk.Label(dashboard, text=f"State: {user['state']}").pack()

    # Credit Section
    tk.Label(dashboard, text="Credit Amount:").pack(pady=5)
    credit_entry = tk.Entry(dashboard, width=20)
    credit_entry.pack()
    tk.Button(dashboard, text="Credit", command=credit_amount).pack(pady=5)

    # Debit Section
    tk.Label(dashboard, text="Debit Amount:").pack(pady=5)
    debit_entry = tk.Entry(dashboard, width=20)
    debit_entry.pack()
    tk.Button(dashboard, text="Debit", command=debit_amount).pack(pady=5)

    # Delete Button
    tk.Button(dashboard, text="Delete Account", command=delete_account, fg="red").pack(pady=10)

# Create Main Window
root = tk.Tk()
root.title("Bank Management System")
root.geometry("500x500")

# Interface Layout
tk.Label(root, text="Bank Management System", font=("Arial", 18)).pack(pady=10)

# New Account Section
tk.Label(root, text="Create Account", font=("Arial", 14)).pack(pady=5)
username_entry = tk.Entry(root, width=30)
contact_entry = tk.Entry(root, width=30)
amount_entry = tk.Entry(root, width=30)
city_entry = tk.Entry(root, width=30)
state_entry = tk.Entry(root, width=30)

tk.Label(root, text="Username:").pack()
username_entry.pack()
tk.Label(root, text="Contact No.:").pack()
contact_entry.pack()
tk.Label(root, text="Amount (Min ₹1000):").pack()
amount_entry.pack()
tk.Label(root, text="City:").pack()
city_entry.pack()
tk.Label(root, text="State:").pack()
state_entry.pack()

tk.Button(root, text="Create Account", command=create_account).pack(pady=5)

# Login Section
tk.Label(root, text="Login", font=("Arial", 14)).pack(pady=5)
login_username_entry = tk.Entry(root, width=30)
login_account_entry = tk.Entry(root, width=30)

tk.Label(root, text="Username:").pack()
login_username_entry.pack()
tk.Label(root, text="Account No.:").pack()
login_account_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=5)

# Run the App
root.mainloop()

# Close the database connection
mycursor.close()
connection.close()

