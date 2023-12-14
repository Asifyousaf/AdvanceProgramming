# Chapter 2  Exercise 1 - Welcome

# Import the tkinter module
from tkinter import *

# Creating a root window
root = Tk()

# Setting the title for the window
root.title('Welcome GUI')

# Setting the dimensions of the window
root.geometry('600x600')

# Disable resizing of the window
root.resizable(0, 0)

# Adding background color to the window
root.configure(bg="lightblue")

# Creating a custom font for the label
welcome_label = Label(root, text="Welcome to the GUI!!!", font=("Arial", 16, "bold"))
# to display label using pack
welcome_label.pack()

# Run the main event loop
root.mainloop()

#End marker 