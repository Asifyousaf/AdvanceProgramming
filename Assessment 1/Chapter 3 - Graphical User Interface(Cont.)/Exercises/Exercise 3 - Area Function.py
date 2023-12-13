# Chapter 3 Exercise 3 - Area fucntion

# using the tkinter library and messagebox
from tkinter import *
from tkinter import ttk, messagebox # tkk for notebook

# Function to calculate the area of a circle
def calculate_circle_area():
    # Getting the radius value from the entry widget
    radius_str = circle_radius_entry.get()
    # Checking if the input is a valid number
    if radius_str.isdigit():
        # Converting the radius to a float
        radius = float(radius_str)
        # Calculate the area of the circle
        area = 3.14 * radius**2
        # Update the result label with the calculated area
        circle_result_label.config(text=f"Area: {area} square units", fg="green", font=("Roboto", 12, 'bold'))
    else:
        # Showing an error message if the input is not valid
        messagebox.showerror("Error", "Please enter a valid radius.")

# Function to calculate the area of a square
def calculate_square_area():
    # Getting the side length value from the entry widget
    side_str = square_side_entry.get()
    # Checking if the input is a valid number
    if side_str.isdigit():
        # Converting the side length to a float
        side = float(side_str)
        # Calculate the area of the square
        area = side**2
        # Update the result label with the calculated area
        square_result_label.config(text=f"Area: {area} square units", fg="#9370DB", font=("Roboto", 12, 'bold'))
    else:
        # Show an error message if the input is not valid
        messagebox.showerror("Error", "Please enter a valid side length.")

# Function to calculate the area of a rectangle
def calculate_rectangle_area():
    # Getting the length and width values from the entry widgets
    length_str = rectangle_length_entry.get()
    width_str = rectangle_width_entry.get()
    # Checking if the inputs are valid numbers
    if length_str.isdigit() and width_str.isdigit():
        # Converting the length and width to floats
        length = float(length_str)
        width = float(width_str)
        # Calculate the area of the rectangle
        area = length * width
        # Update the result label with the calculated area
        rectangle_result_label.config(text=f"Area: {area} square units", fg="#4169E1", font=("Roboto", 12, 'bold'))
    else:
        # Show an error message if the inputs are not valid
        messagebox.showerror("Error", "Please enter valid length and width.")

# Creating main window
root = Tk()

# Setting the title for the window
root.title("Area Calculator")

# Setting the window size 
root.geometry("400x300")

# Creating a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Tab for Circle
circle_tab = Frame(notebook, bg="#E6E6FA")  
notebook.add(circle_tab, text='Circle')

# Widgets for Circle tab
# Label for entering the radius
label_radius = Label(circle_tab, text='Enter Radius:', font=('Roboto', 12, 'bold'), bg="#E6E6FA")
label_radius.pack(pady=5)
# Entry widget for entering the radius
circle_radius_entry = Entry(circle_tab, font=("Helvetica", 12))
circle_radius_entry.pack(pady=5)
# Button to calculate the circle area
button_calculate_circle = Button(circle_tab, text='Calculate', command=calculate_circle_area, font=('Roboto', 12, 'bold'), bg="#9370DB", fg="white")
button_calculate_circle.pack(pady=10)
# Result label for displaying the circle area
circle_result_label = Label(circle_tab, text='Area:', font=('Roboto', 12, 'bold'), bg="#E6E6FA")
circle_result_label.pack()

# Tab for Square
square_tab = Frame(notebook, bg="#87CEEB")  
notebook.add(square_tab, text='Square')

# Widgets for Square tab
# Label for entering the side length
label_square_side = Label(square_tab, text='Enter Side Length:', font=('Roboto', 12, 'bold'), bg="#87CEEB")
label_square_side.pack(pady=5)
# Entry widget for entering the side length
square_side_entry = Entry(square_tab, font=('Roboto', 12, 'bold'))
square_side_entry.pack(pady=5)
# Button to calculate the square area
button_calculate_square = Button(square_tab, text='Calculate', command=calculate_square_area, font=('Roboto', 12, 'bold'), bg="#4169E1", fg="white")
button_calculate_square.pack(pady=10)
# Result label for displaying the square area
square_result_label = Label(square_tab, text='Area:', font=('Roboto', 12, 'bold'), bg="#87CEEB")
square_result_label.pack()

# Tab for Rectangle
rectangle_tab = Frame(notebook, bg="#F08080")  
notebook.add(rectangle_tab, text='Rectangle')

# Widgets for Rectangle tab
# Label for entering the length
label_rectangle_length = Label(rectangle_tab, text='Enter Length:', font=('Roboto', 12, 'bold'), bg="#F08080")
label_rectangle_length.pack(pady=5)
# Entry widget for entering the length
rectangle_length_entry = Entry(rectangle_tab, font=('Roboto', 12, 'bold'))
rectangle_length_entry.pack(pady=5)
# Label for entering the width
label_rectangle_width = Label(rectangle_tab, text='Enter Width:', font=('Roboto', 12, 'bold'), bg="#F08080")
label_rectangle_width.pack(pady=5)
# Entry widget for entering the width
rectangle_width_entry = Entry(rectangle_tab, font=('Roboto', 12, 'bold'))
rectangle_width_entry.pack(pady=5)
# Button to calculate the rectangle area
button_calculate_rectangle = Button(rectangle_tab, text='Calculate', command=calculate_rectangle_area, font=('Roboto', 12, 'bold'), bg="#CD5C5C", fg="white")
button_calculate_rectangle.pack(pady=10)
# Result label for displaying the rectangle area
rectangle_result_label = Label(rectangle_tab, text='Area:', font=('Roboto', 12, 'bold'), bg="#F08080")
rectangle_result_label.pack()

# Pack for the notebook
notebook.pack(fill=BOTH, expand=YES)

# Starting the Tkinter event loop
root.mainloop()

# End marker