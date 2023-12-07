import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("400x450")
root.configure(bg="#f0f0f0")  # Set background color

# Function to handle user input
def process_order():
    coffee_type = coffee_var.get()
    sugar = int(sugar_var.get())
    milk = int(milk_var.get())

    try:
        amount_paid = float(amount_paid_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid amount.")
        return

    # Assume cost of coffee is $2, with an additional $0.50 for each sugar and milk
    cost = 2 + (sugar * 0.5) + (milk * 0.5)

    if amount_paid >= cost:
        change = amount_paid - cost
        order_message = f"You ordered a {coffee_type} coffee with {sugar} sugar and {milk} milk. The cost is ${cost:.2f} and your change is ${change:.2f}."
        messagebox.showinfo("Order Received", order_message)
    else:
        messagebox.showerror("Insufficient Funds", "You have not paid enough for your order.")

# Variables to store user inputs
coffee_var = tk.StringVar()
sugar_var = tk.StringVar()
milk_var = tk.StringVar()

# Create a drop-down menu for coffee type
coffee_label = tk.Label(root, text="Coffee Type:", bg="#f0f0f0")
coffee_label.pack(pady=5)
coffee_option = tk.OptionMenu(root, coffee_var, "Regular", "Americano", "Latte")
coffee_option.pack(pady=5)

# Create radio buttons for sugar and milk options
sugar_label = tk.Label(root, text="Sugar:", bg="#f0f0f0")
sugar_label.pack(pady=5)
sugar_1 = tk.Radiobutton(root, text="1", variable=sugar_var, value="1", bg="#f0f0f0")
sugar_1.pack(anchor='w')
sugar_2 = tk.Radiobutton(root, text="2", variable=sugar_var, value="2", bg="#f0f0f0")
sugar_2.pack(anchor='w')
sugar_3 = tk.Radiobutton(root, text="3", variable=sugar_var, value="3", bg="#f0f0f0")
sugar_3.pack(anchor='w')

milk_label = tk.Label(root, text="Milk:", bg="#f0f0f0")
milk_label.pack(pady=5)
milk_1 = tk.Radiobutton(root, text="1", variable=milk_var, value="1", bg="#f0f0f0")
milk_1.pack(anchor='w')
milk_2 = tk.Radiobutton(root, text="2", variable=milk_var, value="2", bg="#f0f0f0")
milk_2.pack(anchor='w')
milk_3 = tk.Radiobutton(root, text="3", variable=milk_var, value="3", bg="#f0f0f0")
milk_3.pack(anchor='w')

# Create an entry box for the amount paid
amount_paid_label = tk.Label(root, text="Amount Paid:", bg="#f0f0f0")
amount_paid_label.pack(pady=5)
amount_paid_entry = tk.Entry(root)
amount_paid_entry.pack(pady=5)

# Create a label to display the total cost
total_cost_label = tk.Label(root, text="Total Cost: $0.00", bg="#f0f0f0", font=("Arial", 12, "bold"))
total_cost_label.pack(pady=5)

# Create a button to process the order with some style
order_button = tk.Button(root, text="Order", command=process_order, bg="#4CAF50", fg="white", padx=10, pady=5)
order_button.pack(pady=20)

# Function to update the total cost dynamically
def update_cost(*args):
    coffee_type = coffee_var.get()
    sugar = int(sugar_var.get())
    milk = int(milk_var.get())

    # Assume cost of coffee is $2, with an additional $0.50 for each sugar and milk
    cost = 2 + (sugar * 0.5) + (milk * 0.5)
    
    total_cost_label.config(text=f"Total Cost: ${cost:.2f}")

# Bind the update_cost function to changes in coffee type, sugar, and milk
coffee_var.trace_add("write", update_cost)
sugar_var.trace_add("write", update_cost)
milk_var.trace_add("write", update_cost)

# Run the app
root.mainloop()