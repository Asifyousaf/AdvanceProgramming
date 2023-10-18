# Import the tkinter module
from tkinter import *

# Create a root window
root = Tk()

# Set the title for the window
root.title('Widgets example')

# Set the dimensions of the window
root.geometry('600x600')

# Disable resizing of the window
root.resizable(0, 0)

# Create a button widget
mybutton = Button(root, text="Button")

# Create a label widget
mylabel = Label(root, text="WELCOME")

# Pack the label widget into the window
mylabel.pack()

# Pack the button widget into the window
mybutton.pack()

# Run the main event loop
root.mainloop()
