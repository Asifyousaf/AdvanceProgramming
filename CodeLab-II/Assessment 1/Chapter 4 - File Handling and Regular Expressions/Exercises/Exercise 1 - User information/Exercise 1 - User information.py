# using the tkinter library
from tkinter import *

# Makign fucntion to read & write data
def save_to_file(name, age, hometown):
    # Saving user information to the bio.txt file
    with open('Chapter 4 - File Handling and Regular Expressions/Exercises/Exercise 1 - User information/bio.txt', 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hometown: {hometown}\n")

def read_from_file():
    try:
        # Reading user information from the bio.txt file
        with open('bio.txt', 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found. Please create your file first."

def submit_form():
    # Getting user input from the entry fields
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    # Save user information to the file
    save_to_file(name, age, hometown)

    # Display the content in a label
    result_label.config(text=read_from_file())

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("User Information root")

# Creating and place the form elements
label_name = Label(root, text="Name:")   # Name
label_name.grid(row=0, column=0, padx=10, pady=10, sticky=E)
entry_name = Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = Label(root, text="Age:")   # Age
label_age.grid(row=1, column=0, padx=10, pady=10, sticky=E)
entry_age = Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

label_hometown = Label(root, text="Hometown:")  # Hometown
label_hometown.grid(row=2, column=0, padx=10, pady=10, sticky=E)
entry_hometown = Entry(root)
entry_hometown.grid(row=2, column=1, padx=10, pady=10)

# Button to submit the form
submit_button = Button(root, text="Submit", command=submit_form,bg='#22263d',fg='white') # Submit button
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = Label(root, text="")  # display data
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()

# End Marker