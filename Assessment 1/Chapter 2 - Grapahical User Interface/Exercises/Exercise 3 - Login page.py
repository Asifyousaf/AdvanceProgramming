# using the tkinter library
from tkinter import *

# Creating a root window
root = Tk()

# Setting the title for the window
root.title('Login GUI')

# Setting the dimensions of the window
root.geometry('400x200')

# Disable resizing of the window
root.resizable(0, 0)

# Adding background color to the window
root.configure(bg="#22263d")

# Creating a custom font for the labels
font_style = ("Arial", 12, "bold")

# Creating and placing a label for welcome message
welcome_label = Label(root, text="Login Page", font=("Arial", 16, "bold"), bg="#22263d", fg="white")
welcome_label.grid(row=0, column=1, pady=11, padx=1)

# Creating and placing labels and entry widgets in separate rows
label_login = Label(root, text="Username:", font=font_style, bg="#22263d", fg="white")
label_password = Label(root, text="Password:", font=font_style, bg="#22263d", fg="white")

# Displaing the login and password text
label_login.grid(row=1, column=0, pady=10, padx=10)
label_password.grid(row=2, column=0, pady=10, padx=10)

# Creating and placing labels and entry widgets in separate rows
entry_login = Entry(root)
entry_password = Entry(root, show="*")

# Displaing the login and password field
entry_login.grid(row=1, column=1, pady=10, padx=10)
entry_password.grid(row=2, column=1, pady=10, padx=10)

# Creating and placing a button
btn_submit = Button(root, text="Submit", bg="darkgreen", fg="white",font=("Arial", 12, "bold"))
btn_submit.grid(row=3, column=1, pady=10)

# Creating and placing a label to display results
result_label = Label(root, text="", font=font_style, bg="#22263d", fg="white")
result_label.grid(row=4, column=1, pady=10)

# Run the main event loop
root.mainloop()

# End Marker