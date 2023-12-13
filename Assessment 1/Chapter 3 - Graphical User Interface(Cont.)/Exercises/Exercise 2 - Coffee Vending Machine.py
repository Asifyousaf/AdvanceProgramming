# Chapter 3 Exercise 2 - Coffee Vending Machine

# using the tkinter library 
from tkinter import *
from tkinter import messagebox

# Creating main window
root = Tk()

# Setting the title for the window
root.title("Coffee Vending Machine")

# Setting the window size 
root.geometry("350x340")

# Adding background image
image_path = PhotoImage(file="Chapter 3 - Graphical User Interface(Cont.)\images\Coffee-bg.png")
bg = Label(root, image=image_path)
bg.place(relheight=1, relwidth=1)

# Function to handle user input
def process_order():
    coffee_type = coffee_var.get()
    sugar = int(sugar_var.get())
    milk = int(milk_var.get())

    try:
        amount_paid = float(amount_paid_entry.get()) 
        # will Display an error message if the entered amount is not a valid number
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid amount.")
        return

    # it will Calculate the cost of coffee
    cost = 2 + (sugar * 0.5) + (milk * 0.5)

    # Checking if the amount paid is sufficient
    if amount_paid >= cost:
        change = amount_paid - cost # substracting the cost
        order_message = f"You ordered a {coffee_type} coffee with {sugar} sugar and {milk} milk. The cost is $
        {cost:.2f} and your change is ${change:.2f}."
        messagebox.showinfo("Order Received", order_message)
    else:
        messagebox.showerror("Insufficient Funds", "You have not paid enough for your order.")

# Variables to store user inputs
coffee_var = StringVar()
sugar_var = StringVar()
milk_var = StringVar()

# Creating and placing a label for the welcome message
welcome_label = Label(root, text="Coffee Page", font=("Roboto", 19, "bold"), bg="#3d2800", fg="white")
welcome_label.grid(row=0, column=1, pady=11, padx=10)

# Creating a drop-down menu for coffee type
coffee_label = Label(root, text="Coffee Type:", bg="#3d2800", font=("Roboto", 12, 'bold'), fg="white")
coffee_label.grid(row=1, column=0, pady=5, padx=5)
coffee_option = OptionMenu(root, coffee_var, "Regular - $2", "Americano - $2", "Latte - $2")
coffee_option.config(font=("Roboto", 12, 'bold'), bg="#3d2800", fg="white")
coffee_option.grid(row=1, column=1, pady=5)

# Creating option menus for sugar and milk
sugar_label = Label(root, text="Sugar:", bg="#3d2800", font=("Roboto", 12, 'bold'), fg="white")
sugar_label.grid(row=2, column=0, pady=5)
sugar_option = OptionMenu(root, sugar_var, "1", "2", "3")
sugar_option.config(font=("Roboto", 12, 'bold'), bg="#3d2800", fg="white")
sugar_option.grid(row=2, column=1, pady=5)

# Creating label for Milk
milk_label = Label(root, text="Milk:", bg="#3d2800", font=("Roboto", 12, 'bold'), fg="white")
milk_label.grid(row=3, column=0, pady=5)

# Creating option menu for selecting Milk quantity
milk_option = OptionMenu(root, milk_var, "1", "2", "3")
milk_option.config(font=("Roboto", 12, 'bold'), bg="#3d2800", fg="white")
milk_option.grid(row=3, column=1, pady=5)


# Creating an entry box for the amount paid
amount_paid_label = Label(root, text="Enter Amount:", bg="#3d2800", font=("Roboto", 12, 'bold'), fg="white")
amount_paid_label.grid(row=4, column=0, pady=5)
amount_paid_entry = Entry(root, font=("Roboto", 10, 'bold'), bg="#3d2800", fg="white")
amount_paid_entry.grid(row=4, column=1, pady=5)

# Creating a button to process the order with some style
order_button = Button(root, text="Order", command=process_order, bg="#5d432c", fg="white", 
                      font=("Roboto", 14, 'bold'), padx=10, pady=5)
order_button.grid(row=5, column=1, columnspan=2, pady=20)

# Starting the Tkinter event loop
root.mainloop()

# End marker