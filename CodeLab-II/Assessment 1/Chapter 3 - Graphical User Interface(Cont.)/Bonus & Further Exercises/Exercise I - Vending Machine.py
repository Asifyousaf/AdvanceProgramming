from tkinter import *
from tkinter import messagebox

# Vending machine data
items = ["Snickers Bar", "Sun Chips", "Cold Coffee"]
prices = {"Snickers Bar": 2.00, "Sun Chips": 3.00, "Cold Coffee": 2.50}
stock = {"Snickers Bar": 10, "Sun Chips": 5, "Cold Coffee": 8}

# Create the main window
root = Tk()

# Setting the title for the window
root.title("Simple Vending Machine")

# Setting the window size
root.geometry("300x300")

# Variables
selected_item = StringVar()
selected_item.set(items[0])  # Default selection
quantity_var = StringVar()
amount_paid_var = DoubleVar()

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
def process_purchase():
    item = selected_item.get()
    quantity = int(quantity_var.get())
    amount_paid = amount_paid_var.get()

    # Calculate the total cost
    if item in prices:
        price = prices[item]
        current_stock = stock[item]
    else:
        messagebox.showerror("Invalid Item", "Please select a valid item.")
        return

    total_cost = price * quantity

    # Check if there is enough stock
    if quantity > current_stock:
        messagebox.showerror("Out of Stock", f"We're out of stock for {item}. Please enter a lower quantity.")
        return

    # Check if the amount paid is sufficient
    if amount_paid >= total_cost:
        remaining_stock = current_stock - quantity
        messagebox.showinfo("Purchase Successful", f"Thank you for your purchase!\nTotal Cost: {total_cost:.2f}\nRemaining Stock: {remaining_stock}")
        # Update the stock
        stock[item] = remaining_stock
    else:
        messagebox.showerror("Insufficient Funds", "You have not paid enough for your purchase.")

purchase_button = Button(root, text="Purchase", command=process_purchase, bg="#5d432c", fg="white", font=("Roboto", 12, 'bold'))
purchase_button.pack(pady=10)

# Starting the Tkinter event loop
root.mainloop()
