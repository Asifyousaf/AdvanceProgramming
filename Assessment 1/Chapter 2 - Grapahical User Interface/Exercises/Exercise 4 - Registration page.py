# Chapter 2  Exercise 4 - Registration Page

# using the tkinter library
from tkinter import *

# Creating a root window
root = Tk()

# Setting the title for the window
root.title('Registration Page')

# Setting the size of the window
root.geometry('500x850')  # Smaller window size

# Disable resizing of the window
root.resizable(0, 0)

# Adding background color to the window
root.configure(bg="white")

# Creating a frame for the entire content with adjusted width
content_frame = Frame(root, width=480, height=600, bg="#f2f2f2")  # Adjusted width and height
content_frame.grid(padx=10, pady=10)

# Creating a label for the image (banner)
banner = PhotoImage(file='Chapter 2 - Grapahical User Interface\Exercises\RAK.png', width=480, height=120)  # Adjusted width and height
banner_lbl = Label(content_frame, image=banner, bg="white")
banner_lbl.grid(row=0, column=0, columnspan=2)

# Creating the main heading
head1 = Label(content_frame, font=('Roboto', 18, 'bold'), text="Student Management System", fg='#22263d', bg="#f2f2f2")
head1.grid(row=1, column=0, columnspan=2, pady=(10, 0))

# Creating the sub heading
head2 = Label(content_frame, font=('Roboto', 16, 'bold'), text="New Student Registration", fg='#22263d', bg="#f2f2f2")
head2.grid(row=2, column=0, columnspan=2, pady=(0, 5))

# Labels and Entry Widgets with adjusted layout
label_login = Label(content_frame, font=('Roboto', 12, 'bold'), text="Student Name", fg="gray", bg="#f2f2f2")
entry_name = Entry(content_frame, width=18, bg='#ADAEB7', font=('Roboto', 12))

label_password = Label(content_frame, font=('Roboto', 12, 'bold'), text="Mobile Number", fg="gray", bg="#f2f2f2")
entry_mobile = Entry(content_frame, width=18, bg='#ADAEB7', font=('Roboto', 12))

label_mail = Label(content_frame, font=('Roboto', 12, 'bold'), text="Email Id", fg="gray", bg="#f2f2f2")
entry_email = Entry(content_frame, width=18, bg='#ADAEB7', font=('Roboto', 12))

label_add = Label(content_frame, font=('Roboto', 12, 'bold'), text="Home Address", fg="gray", bg="#f2f2f2")
entry_home_address = Entry(content_frame, width=18, bg='#ADAEB7', font=('Roboto', 12))

label_gender = Label(content_frame, font=('Roboto', 12, 'bold'), text="Gender", fg="gray", bg="#f2f2f2")
entry_gender = Entry(content_frame, width=18, bg='#ADAEB7', font=('Roboto', 12))

label_course = Label(content_frame, font=('Roboto', 11, 'bold'), text="Course Enrolled", fg="gray", bg="#f2f2f2")
label_radiobtn = Radiobutton(content_frame, text="BSc CC", fg='#545869', font=('Roboto', 12, 'bold'))

label_radiobtn1 = Radiobutton(content_frame, text="BSc CY", fg='#545869', font=('Roboto', 12, 'bold'))
label_radiobtn2 = Radiobutton(content_frame, text="BSc PSY", fg='#545869', font=('Roboto', 12, 'bold'))
label_radiobtn3 = Radiobutton(content_frame, text="BA & BM", fg='#545869', font=('Roboto', 12, 'bold'))

label_lang = Label(content_frame, font=('Roboto', 11, 'bold'), text="Languages known", fg="gray", bg="#f2f2f2")
label_box = Checkbutton(content_frame, text='English', fg='#545869', font=('Roboto', 12, 'bold'))
label_box1 = Checkbutton(content_frame, text='Tagalog', fg='#545869', font=('Roboto', 12, 'bold'))
label_box2 = Checkbutton(content_frame, text='Hindi/Urdu', fg='#545869', font=('Roboto', 12, 'bold'))

label_rate = Label(content_frame, font=('Roboto', 11, 'bold'), text="Rate your English communication skills", fg="gray", bg="#f2f2f2")
scale = Scale(content_frame, from_=0, to=100, orient="horizontal", length=250, fg='blue')

submit_button = Button(content_frame, text="Submit", bg="#22263d", fg="white", width=12, font=('Roboto', 12, 'bold'))
clear_button = Button(content_frame, text="Clear", bg="#22263d", fg="white", width=12, font=('Roboto', 12, 'bold'))

# Displaying the forum text and entry widgets on the same row
label_login.grid(row=3, column=0, pady=12, padx=10, sticky=E)
entry_name.grid(row=3, column=1, pady=12, padx=10, sticky=W)

label_password.grid(row=4, column=0, pady=12, padx=10, sticky=E)
entry_mobile.grid(row=4, column=1, pady=12, padx=10, sticky=W)

label_mail.grid(row=5, column=0, pady=12, padx=10, sticky=E)
entry_email.grid(row=5, column=1, pady=12, padx=10, sticky=W)

label_add.grid(row=6, column=0, pady=12, padx=10, sticky=E)
entry_home_address.grid(row=6, column=1, pady=12, padx=10, sticky=W)

label_gender.grid(row=7, column=0, pady=12, padx=10, sticky=E)
entry_gender.grid(row=7, column=1, pady=12, padx=10, sticky=W)

label_course.grid(row=8, column=0, pady=5, padx=10, sticky=E)
label_radiobtn.grid(row=8, column=1, padx=10, sticky=W)

label_radiobtn1.grid(row=9, column=1, padx=10, sticky=W)
label_radiobtn2.grid(row=10, column=1, padx=10, sticky=W)
label_radiobtn3.grid(row=11, column=1, padx=10, sticky=W)

label_lang.grid(row=12, column=0, padx=10, sticky=E)
label_box.grid(row=12, column=1, padx=10, sticky=W)

label_box1.place(x=355, y=572)
label_box2.grid(row=13, column=1, padx=10, sticky=W)

label_rate.grid(row=14, column=0, columnspan=2, pady=(10, 0))
scale.grid(row=15, column=0, columnspan=2, pady=(10, 0))

submit_button.grid(row=16, column=0, pady=20, padx=(15, 30), sticky=E)
clear_button.grid(row=16, column=1, pady=20, padx=(10, 50), sticky=W)

# Run the main event loop
root.mainloop()
