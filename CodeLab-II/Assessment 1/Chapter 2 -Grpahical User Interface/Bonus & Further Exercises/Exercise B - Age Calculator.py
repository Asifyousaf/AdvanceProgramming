# using the tkinter library and datetime
from tkinter import *
from datetime import datetime

# Function to calculate the age
def calculate_age():
    try:
        # Getting the day, month, and year from the input entries
        dob_day = int(dob_day_entry.get())
        dob_month = int(dob_month_entry.get())
        dob_year = int(dob_year_entry.get())

        # Creating a datetime object for the input date of birth
        dob = datetime(dob_year, dob_month, dob_day)
        
        # Getting the current date
        today = datetime.today()

        # Calculatingg the age, adjusting for whether the birthday has occurred this year by using '<'
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        # Display the result
        result_label.config(text=f"Your age is {age} years.", fg="white")
    except ValueError:
        # if the input date is not in the correct format to show error msg
        result_label.config(text="Invalid date format", fg="red")


# Creating the main window
root = Tk()
root.title("Age Calculator")

# Adding a blue background to the main window
root.configure(bg='#22263d')

# Heading
head1 = Label(root, font=('Roboto', 20, 'bold'), text="Age Calculator", bg='#22263d',fg="white")
head1.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Age Calculation
# Label for Day input
dob_day_label = Label(root, text="Day:", font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
dob_day_label.grid(row=1, column=0, padx=10, pady=10)

# Entry field for Day input
dob_day_entry = Entry(root, font=('Roboto', 12,'bold'), bg='#B0C4DE', fg='black')
dob_day_entry.grid(row=1, column=1, padx=10, pady=10)

# Label for Month input
dob_month_label = Label(root, text="Month:", font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
dob_month_label.grid(row=1, column=2, padx=10, pady=10)

# Entry field for Month input
dob_month_entry = Entry(root, font=('Roboto', 12,'bold'), bg='#B0C4DE', fg='black')
dob_month_entry.grid(row=1, column=3, padx=10, pady=10)

# Label for Year input
dob_year_label = Label(root, text="Year:", font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
dob_year_label.grid(row=2, column=0, padx=10, pady=10)

# Entry field for Year input
dob_year_entry = Entry(root, font=('Roboto', 12,'bold'), bg='#B0C4DE', fg='black')
dob_year_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate age
calculate_button = Button(root, text="Calculate Age", command=calculate_age, font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
calculate_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Result
result_label = Label(root, text="", font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
result_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
