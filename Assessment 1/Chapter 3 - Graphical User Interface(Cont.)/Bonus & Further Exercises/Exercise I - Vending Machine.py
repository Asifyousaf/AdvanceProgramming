# Chapter 3 Exercise i - Vending machine

# using the tkinter libraryand messagebox
from tkinter import *
from tkinter import messagebox

# Vending machine data
items = ["Snickers Bar", "Sun Chips", "Cold Coffee"]
prices = {"Snickers Bar": 2.00, "Sun Chips": 3.00, "Cold Coffee": 2.50}
stock = {"Snickers Bar": 10, "Sun Chips": 5, "Cold Coffee": 8}

def process_purchase():
    # Getting user input: selected item, quantity, and amount paid
    item = selected_item.get()
    quantity = int(quantity_var.get())
    amount_paid = amount_paid_var.get()

    # Calculates the total cost
    if item in prices:
        price = prices[item]
        current_stock = stock[item]
    else:
        # Show an error message for invalid item selection
        messagebox.showerror("Invalid Item", "Please select a valid item.")
        return

    total_cost = price * quantity

    # Checking if there is enough stock
    if quantity > current_stock:
        messagebox.showerror("Out of Stock", f"We're out of stock for {item}. Please enter a lower quantity.")
        return

    # Checking if the amount paid is sufficient
    if amount_paid >= total_cost:
        remaining_stock = current_stock - quantity
        messagebox.showinfo("Purchase Successful", f"Thank you for your purchase!\nTotal Cost: {total_cost:.2f}\nRemaining Stock: {remaining_stock}")
        # Updating the stock
        stock[item] = remaining_stock
    else:
        messagebox.showerror("Insufficient Funds", "You have not paid enough for your purchase.")

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Simple Vending Machine")

# Setting the window size
root.geometry("300x300")

# Variables
selected_item = StringVar()

# Default selection
selected_item.set(items[0])  
quantity_var = StringVar()
amount_paid_var = DoubleVar(value='')

# Labels
welcome_label = Label(root, text="Vending Machine", font=("Roboto", 16, "bold"))
welcome_label.pack(pady=10)

item_label = Label(root, text="Select Item:")
item_label.pack()

# Option menu for selecting item
item_option = OptionMenu(root, selected_item, *items)
item_option.pack()

quantity_label = Label(root, text="Enter Quantity:")
quantity_label.pack()

# Entry for entering quantity
quantity_entry = Entry(root, textvariable=quantity_var)
quantity_entry.pack()

amount_paid_label = Label(root, text="Enter Amount Paid:")
amount_paid_label.pack()

# Entry for entering amount paid
amount_paid_entry = Entry(root, textvariable=amount_paid_var)
amount_paid_entry.pack()

# Button to process the purchase
purchase_button = Button(root, text="Purchase", command=process_purchase, bg="#5d432c", fg="white", font=("Roboto", 12, 'bold'))
purchase_button.pack(pady=10)

# Starting the Tkinter event loop
root.mainloop()

# End marker