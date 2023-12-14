# Chapter 3 Exercise 1 - Greeting App

# using the tkinter library
from tkinter import *

def update_greeting():
    # Getting the name from the entry widget
    name = name_entry.get()

    # Getting the selected color from the dropdown menu
    color = color_var.get()

    # Creating a personalized greeting message
    greeting_text = f"Hello, {name}!"

    # Updating the display label with the greeting message and selected color
    display_label.config(text=greeting_text, fg=color)


# Creating the main window
root = Tk()

# Setting the title of the window
root.title("Greeting App")

# Setting the window size 
root.geometry("310x250")

# Disabling window resizable
root.resizable(0, 0)

# Adding background image
image_path = PhotoImage(file="Chapter 3 - Graphical User Interface(Cont.)\images\Greeting-bg.png")
bg = Label(root, image=image_path)
bg.place(relheight=1, relwidth=1)

# InputFrame
input_frame = Frame(root, bg='white', width=300, height=150)  
input_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Title Label
title_label = Label(input_frame, text="Greeting App", font=('Helvetica', 18, 'bold'), fg='#22263d', bg='white') 
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Entry for user's name
name_label = Label(input_frame, text="Enter your name:", font=('Roboto', 12, 'bold'), bg='#FFFFFF', fg='#22263d')
name_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

# Displaying the entry field
name_entry = Entry(input_frame, bg='white', fg='black', font=('Helvetica', 12))
name_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# Dropdown menu for color selection using OptionMenu
color_label = Label(input_frame, text="Select a color:", font=('Roboto', 12, 'bold'), bg='#FFFFFF', fg='#22263d')
color_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

# Setting the color list 
colors = ['black', 'red', 'green', 'blue']  # Color
color_var = StringVar(value=colors[0])  # Starting color

# Using dropdown to display the list of color
color_dropdown = OptionMenu(input_frame, color_var, *colors)
color_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')

# Button to update greeting
update_button = Button(input_frame, text="Update Greeting", command=update_greeting, bg='#22263d', fg='white', font=('Helvetica', 12, 'bold'))
update_button.grid(row=3, column=0, columnspan=2, padx=10, sticky='n')

# DisplayFrame
display_frame = Frame(root, bg='white', width=300, height=150) 
display_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label to display personalized greeting
display_label = Label(display_frame, text="", font=('Helvetica', 16,'bold'), bg='white', fg='black')  
display_label.pack(padx=5, pady=5)

# Starting the Tkinter event loop
root.mainloop()

# End marker