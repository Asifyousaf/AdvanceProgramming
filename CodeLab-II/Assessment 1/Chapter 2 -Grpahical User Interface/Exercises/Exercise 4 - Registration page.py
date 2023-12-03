from tkinter import *

# Creating a root window
root = Tk()

# Setting the title for the window
root.title('Registration Page')

# Setting the size of the window
root.geometry('750x1000')

# Adding background color to the window
root.configure(bg="white")

# Creating the frame for the image
form_frame = Label(root, width=750, height=500, border=5)
form_frame.grid()

# Creating the frame for the input section
form_frame2 = Label(root, width=750, height=740, bg='#f5f5f5')
form_frame2.grid(padx=10, pady=10)

# Creating a label for the image
banner = PhotoImage(file='Chapter 2 -Grpahical User Interface\Exercises\RAK.png', width=750, height=245)
banner_lbl = Label(form_frame, image=banner, bg="white")
# Using pack to place the image at the top of the window
banner_lbl.grid(row=0, column=0, pady=10)


# Creating the main heading for the input section
head1 = Label(form_frame2, font=('Roboto', 25, 'bold'), text="Student Management System", fg='#22263d')
head1.grid(padx=110, pady=10)

head2 = Label(form_frame2, font=('Sans', 20, 'bold'), text="New Student Registration", fg='#22263d')
head2.grid(padx=10, pady=0)

# Creating and placing labels and entry widgets in separate rows
label_login = Label(form_frame2, font=('Sans', 15, 'bold'), text="Student Name", fg="gray")
label_password = Label(form_frame2, font=('Sans', 15, 'bold'), text="Mobile Number", fg="gray")
label_mail = Label(form_frame2, font=('Sans', 15, 'bold'), text="Email Id", fg="gray")
entry_name = Entry(form_frame2, width=30)  # Use form_frame2 as the parent
entry_mobile = Entry(form_frame2, width=30)  # Use form_frame2 as the parent
entry_email = Entry(form_frame2, width=30)  # Use form_frame2 as the parent

# Displaying the login and password text and entry widgets on the same row
label_login.grid(row=2, column=0, pady=10, padx=10)
entry_name.grid(row=2, column=1, pady=10, padx=10)  # Use the same row for the entry widget
label_password.grid(row=3, column=0, pady=10, padx=10)  # Move to the next row for the next label
entry_mobile.grid(row=3, column=1, pady=10, padx=10)  # Use the same row for the next entry widget
label_mail.grid(row=4, column=0, pady=10, padx=10)  # Move to the next row for the next label
entry_email.grid(row=4, column=1, pady=10, padx=10)  # Use the same row for the last entry widget



root.mainloop()
