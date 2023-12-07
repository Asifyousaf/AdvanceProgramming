# Using the tkinter library
from tkinter import *

# Making function
def draw_shape():
    # Getting the selected shape
    shape = shape_var.get()
    # used to clear the canvas before drawing a new shape
    canvas.delete("all")
    # Draw the selected shape on the canvas
    if shape == "Oval":
        canvas.create_oval(50, 50, 350, 350, outline="black")
    elif shape == "Rectangle":
        canvas.create_rectangle(50, 50, 250, 350, outline="black")  
    elif shape == "Square":
        canvas.create_rectangle(50, 50, 150, 50, outline="black")
    elif shape == "Triangle":
        canvas.create_polygon(50, 350, 200, 50, 350, 350, outline="black")

# Creating the main window
root = Tk()

# Setting the window size 
root.geometry("550x550")

# Setting the title for the window
root.title("Draw Shapes")

# Setting the background color of the main window
root.configure(bg="#1aa7ec")  

# Creating canvas for drawing shapes
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=10)

# Label for selecting the shape
shape_label = Label(root, text="Select Shape:",bg="#1aa7ec",font=("Roboto", 15))  # Creating a label with the text "Select Shape:"
shape_label.pack(pady=10)  # Pack the label into the main window

# List of shapes for the dropdown menu
shapes = ["Oval", "Rectangle", "Square", "Triangle"]

# Variable to store the selected shape default is the first shape in the list
shape_var = StringVar(value=shapes[0])  # Creating a StringVar and set its initial value to the default shape

# Dropdown menu for selecting the shape
shape_dropdown = OptionMenu(root, shape_var, *shapes)  # Creating an OptionMenu with the shape_var variable and the shapes list
shape_dropdown.pack()  # Pack the dropdown menu into the main window

# Button to draw the selected shape
draw_button = Button(root, text="Draw", command=draw_shape, width=10, bg="#22263d", fg="white")  # Set the background color to #22263d
draw_button.pack(pady=10)

# Starting the Tkinter event loop
root.mainloop()
# End marker