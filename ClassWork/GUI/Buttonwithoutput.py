# Import the tkinter module
from tkinter import *

# Define function to be called when the button is clicked
def button():
    print("Button was pushed")

# Creating a root window
root = Tk()

# Settin the title for the window
root.title('Widgets example')

# the dimensions of the window
root.geometry('600x600')

#a button with widget and assign the "button" function to it
my_button = Button(root, text="Button", command=button)

#  the button widget into the window at the top position
my_button.pack(side=TOP)

# Run the main event loop
root.mainloop()
