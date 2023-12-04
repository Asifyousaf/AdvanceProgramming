# using the tkinter library
from tkinter import *

# Function to perform addition
def add():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    # Checking if both inputs are valid numbers
    if num1.isdigit() and num2.isdigit():
        result = float(num1) + float(num2)
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid input")

# Function to perform subtraction
def subtract():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    # Checking if both inputs are valid numbers
    if num1.isdigit() and num2.isdigit():
        result = float(num1) - float(num2)
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid input")

# Function to perform multiplication
def multiply():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    # Checking if both inputs are valid numbers
    if num1.isdigit() and num2.isdigit():
        result = float(num1) * float(num2)
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid input")

# Function to perform division
def divide():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    # Check if both inputs are valid numbers
    if num1.isdigit() and num2.isdigit():
        # Checking if the divisor is not zero
        if float(num2) != 0:
            result = float(num1) / float(num2)
            result_label.config(text=f"Result: {result}")
        else:
            result_label.config(text="Cannot divide by zero")
    else:
        result_label.config(text="Invalid input")

# Function to perform modulo division
def modulo():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    # Checking if both inputs are valid numbers
    if num1.isdigit() and num2.isdigit():
        # Checking if the divisor is not zero
        if float(num2) != 0:
            result = float(num1) % float(num2)
            result_label.config(text=f"Result: {result}")
        else:
            result_label.config(text="Cannot calculate modulo with zero")
    else:
        result_label.config(text="Invalid input")


# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Simple Calculator")

# Setting the size of the window
root.geometry('320x320')

# Disable resizing of the window
root.resizable(0, 0)

# Adding a white background to the main window
root.configure(bg='white')

head1 = Label(root, font=('Roboto', 10, 'bold'), text="Simple Calculator", fg='#22263d', bg="#f2f2f2")
head1.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Making Entry widgets for numbers
entry_num1 = Entry(root, width=15, font=('Arial', 12), bg='#ADAEB7')
entry_num1.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = Entry(root, width=15, font=('Arial', 12), bg='#ADAEB7')
entry_num2.grid(row=1, column=1, padx=15, pady=10)

# Making Buttons to perform operations
add_button = Button(root, text="Add", command=add, bg='#22263d', fg='white', height=2, width=10)
add_button.grid(row=2, column=0, padx=10, pady=10)

subtract_button = Button(root, text="Subtract", command=subtract, bg='#22263d', fg='white', height=2, width=10)
subtract_button.grid(row=2, column=1, padx=10, pady=10)

multiply_button = Button(root, text="Multiply", command=multiply, bg='#22263d', fg='white', height=2, width=10)
multiply_button.grid(row=3, column=0, padx=10, pady=10)

divide_button = Button(root, text="Divide", command=divide, bg='#22263d', fg='white', height=2, width=10)
divide_button.grid(row=3, column=1, padx=10, pady=10)

modulo_button = Button(root, text="Modulo", command=modulo, bg='#22263d', fg='white', height=2, width=20)
modulo_button.grid(row=4, column=0, columnspan=2, pady=20)

# Making Label to display the result
result_label = Label(root, text="Result: ", font=('Arial', 14))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()

# End marker