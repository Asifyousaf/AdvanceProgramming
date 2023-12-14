# Chapter 2 Further Exercise II - Capitalize Letters

# using the tkinter library
from tkinter import *

def capitalize_text():
    # Getting the text entered by the user
    user_input = entry.get()

    # Converting the text to uppercase
    capitalized_text = user_input.upper()

    # the result label with the capitalized text
    result_label.config(text=f"Capitalized Text: {capitalized_text}")


# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Text Capitalizer")

# Adding a white background to the main window
root.configure(bg='#FFFFFF')

# Heading
heading_label = Label(root, font=('Roboto', 20, 'bold'), text="Text Capitalizer", bg='#FFFFFF', fg='#22263d')
heading_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Input label and entry
input_label = Label(root, text="Enter text:", font=('Roboto', 12, 'bold'), bg='#FFFFFF', fg='#22263d')
input_label.grid(row=1, column=0, pady=10, padx=10)

entry = Entry(root, font=('Roboto', 12), bg='#B0C4DE', fg='#000000')
entry.grid(row=1, column=1, pady=10, padx=10)

# Button to capitalize text
capitalize_button = Button(root, text="Capitalize Text", command=capitalize_text, font=('Roboto', 12, 'bold'), 
                           bg='#22263d', fg='#FFFFFF')
capitalize_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result
result_label = Label(root, text="", font=('Roboto', 12), bg='#FFFFFF', fg='#000000')
result_label.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

# Start the Tkinter event loop
root.mainloop()

#End marker