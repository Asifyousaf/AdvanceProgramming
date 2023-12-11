# using the tkinter library and messagebox
from tkinter import *
from tkinter import messagebox

# Defining a class for representing an employee
class Employee:
    # Method to set data for an employee
    def set_data(employee, name, position, salary, employee_id):
        employee.name = name
        employee.position = position
        employee.salary = salary
        employee.employee_id = employee_id

    # Method to get data for an employee
    def get_data(employee):
        # Return a formatted string with employee data
        return f"{employee.name}\t{employee.position}\t{employee.salary}\t{employee.employee_id}"

# Function to create an employee object and display information
def add_employee():
    # Get values from entry boxes
    name = name_entry.get()
    position = position_entry.get()
    
    # Handle potential ValueError for invalid input for salary
    try:
        salary = float(salary_entry.get())
    except ValueError:
        # Display an error message in red
        error_label.config(text="Invalid input for Salary. Please enter a valid number.", fg="red")
        return

    # Get employee ID as an integer
    try:
        employee_id = int(id_entry.get())
    except ValueError:
        # Display an error message in red
        error_label.config(text="Invalid input for ID. Please enter a valid number.", fg="red")
        return

    # Clear the error label
    error_label.config(text="")

    # Create an Employee object with the provided values
    employee_object = Employee()
    employee_object.set_data(name, position, salary, employee_id)
    
    # Add the employee object to the list
    employees.append(employee_object)

    # Clear the entry boxes
    name_entry.delete(0, END)
    position_entry.delete(0, END)
    salary_entry.delete(0, END)
    id_entry.delete(0, END)

# Function to display employee information in the console
def display_employees():
    # Display header
    result_text = "Name\tPosition\tSalary\tID\n"

    # Iterate through the list of employees and append their data
    for employee in employees:
        result_text += employee.get_data() + "\n"

    # Display the result in a messagebox popup
    messagebox.showinfo("Employee Information", result_text)

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Employee Class GUI")

# Setting the window size
root.geometry("400x400")

# List to store employee objects
employees = []

# Labels and Entry Boxes
name_label = Label(root, text="Enter Name:")
name_label.pack(pady=5)
name_entry = Entry(root, font=("Helvetica", 12))
name_entry.pack(pady=5)

position_label = Label(root, text="Enter Position:")
position_label.pack(pady=5)
position_entry = Entry(root, font=("Helvetica", 12))
position_entry.pack(pady=5)

salary_label = Label(root, text="Enter Salary:")
salary_label.pack(pady=5)
salary_entry = Entry(root, font=("Helvetica", 12))
salary_entry.pack(pady=5)

id_label = Label(root, text="Enter ID:")
id_label.pack(pady=5)
id_entry = Entry(root, font=("Helvetica", 12))
id_entry.pack(pady=5)

# Error label for displaying error messages
error_label = Label(root, text="", fg="red")
error_label.pack(pady=5)

# Button to add an employee and display information
add_employee_button = Button(root, text="Add Employee", command=add_employee, bg="#4CAF50", fg="white", font=("Roboto", 12, 'bold'))
add_employee_button.pack(pady=10)

# Button to display employee information
display_employees_button = Button(root, text="Display Employees", command=display_employees, bg="#4CAF50", fg="white", font=("Roboto", 12, 'bold'))
display_employees_button.pack(pady=10)

# Run the main event loop
root.mainloop()

# End Marker