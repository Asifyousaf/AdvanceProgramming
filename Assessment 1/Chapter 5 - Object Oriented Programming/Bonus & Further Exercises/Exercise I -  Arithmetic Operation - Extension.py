# Chapter 4 Further Exercise i - User information

# Importing modules from the tkinter library
from tkinter import *
from tkinter import messagebox

# Class for performing operations
class Operations:
    def calculate_arithmetic(operation, value1, value2):
        try:
            if operation == "Addition":
                return value1 + value2
            elif operation == "Subtraction":
                return value1 - value2
            elif operation == "Multiplication":
                return value1 * value2
            elif operation == "Division":
                return value1 / value2 if value2 != 0 else messagebox.showerror("Error", "Cannot divide by zero.")
            elif operation == "Exponentiation":
                return value1 ** value2
        except ValueError:
            messagebox.showinfo("Error", "Please enter valid numeric values.")
            return None

    def calculate_relational(operation, value1, value2):
        try:
            if operation == "Equal":
                return value1 == value2
            elif operation == "Not Equal":
                return value1 != value2
            elif operation == "Greater Than":
                return value1 > value2
            elif operation == "Less Than":
                return value1 < value2
            elif operation == "Greater Than or Equal To":
                return value1 >= value2
            elif operation == "Less Than or Equal To":
                return value1 <= value2
        except ValueError:
            messagebox.showinfo("Error", "Please enter valid numeric values.")
            return None

# Function to perform calculation when the "Calculate" button is clicked
def perform_calculation():
    selected_operation = operation_var.get()
    value1 = float(value1_entry.get())
    value2 = float(value2_entry.get())

    if selected_operation in arithmetic_operations:
        result = Operations.calculate_arithmetic(selected_operation, value1, value2)
    elif selected_operation in relational_operations:
        result = Operations.calculate_relational(selected_operation, value1, value2)
    else:
        messagebox.showinfo("Error", "Invalid operation selected.")
        return

    if result is not None:
        messagebox.showinfo("Result", f"The result is: {result}")

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Operations Calculator")

# Setting the window size
root.geometry("400x300")

# Widgets for Operations tab
operations_tab = Frame(root, bg="#E6E6FA", pady=20)

# Label for selecting the operation
operation_label = Label(operations_tab, text='Select Operation:', font=("Helvetica", 12), bg="#E6E6FA")
operation_label.pack()

# Options for the operations presented in a drop-down menu
arithmetic_operations = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]
relational_operations = ["Equal", "Not Equal", "Greater Than", "Less Than", "Greater Than or Equal To", "Less Than or Equal To"]
all_operations = arithmetic_operations + relational_operations

operation_var = StringVar()
operation_var.set(all_operations[0])
operation_option = OptionMenu(operations_tab, operation_var, *all_operations)
operation_option.pack(pady=10)

# Labels and Entry widgets for inputting numeric values
value1_label = Label(operations_tab, text="Enter Value 1:", font=("Helvetica", 12), bg="#E6E6FA")
value1_label.pack(pady=5)
value1_entry = Entry(operations_tab, font=("Helvetica", 12))
value1_entry.pack(pady=5)

value2_label = Label(operations_tab, text="Enter Value 2:", font=("Helvetica", 12), bg="#E6E6FA")
value2_label.pack(pady=5)
value2_entry = Entry(operations_tab, font=("Helvetica", 12))
value2_entry.pack(pady=5)

# Button to trigger the calculation with specified text, command, font, and color
calculate_button = Button(operations_tab, text='Calculate', command=perform_calculation, font=("Helvetica", 12), bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Packing the Operations tab
operations_tab.pack(fill=BOTH, expand=YES)

# Run the main event loop
root.mainloop()

# End Marker
