from tkinter import *

def check_password(password):
    # Function to check the validity of the password
    # Returns a tuple (is_valid, message)
    
    if not (6 <= len(password) <= 12):
        return False, "Password length must be between 6 and 12 characters."

    # Check if the password satisfies all the criteria
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special_char = any(char in "$#@ " for char in password)

    if has_lowercase and has_number and has_uppercase and has_special_char:
        return True, "Password is valid."
    else:
        return False, "Password does not meet the criteria."

def submit_form():
    # Function to handle form submission
    password = entry_password.get()
    is_valid, message = check_password(password)

    if is_valid:
        result_label.config(text="Password is valid.")
        root.destroy()  # Close the window if the password is valid
    else:
        attempts_left = 5 - int(attempts_var.get())
        result_label.config(text=f"{message} Attempts left: {attempts_left}")
        attempts_var.set(str(attempts_left))

        if attempts_left == 0:
            result_label.config(text="The authorities have been alerted!")
            submit_button.config(state=DISABLED)  # Disable the submit button

# Creating the main window
root = Tk()
root.title("Password Checker")

# Variables
attempts_var = StringVar()
attempts_var.set("5")

# Label and Entry for password input
label_password = Label(root, text="Enter Password:")
label_password.pack(pady=10)

entry_password = Entry(root, show="*")
entry_password.pack(pady=10)

# Button to submit the form
submit_button = Button(root, text="Check Password", command=submit_form)
submit_button.pack(pady=10)

# Label to display the result and attempts left
result_label = Label(root, text="")
result_label.pack(pady=10)

attempts_label = Label(root, text="Attempts left:")
attempts_label.pack()

attempts_display = Label(root, textvariable=attempts_var)
attempts_display.pack()

# Run the main event loop
root.mainloop()
