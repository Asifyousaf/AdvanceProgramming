# using the tkinter library,messagebox and math
from tkinter import *
from tkinter import messagebox
import math

# Defining the base class Shape for geometric shapes
class Shape:
    def input_sides():

        #Placeholder method for gathering side inputs. To be overridden by subclasses.
        pass

    def area():

        #Placeholder method for calculating the area. To be overridden by subclasses.
        pass

# Defining the Circle subclass of Shape
class Circle(Shape):
    def input_sides():

        #Get the radius from the user input. Returns float: The radius of the circle.
        return float(side1_entry.get())

    def area():
        
        #Calculate the area of a circle using the input radius. Returns float: The area of the circle.
        return math.pi * Circle.input_sides() ** 2

# Definung the Rectangle subclass of Shape
class Rectangle(Shape):
    def input_sides():

        #Get the length and width from the user input. Returns tuple: The length and width of the rectangle.
        return float(side1_entry.get()), float(side2_entry.get())

    def area():

        #Calculate the area of a rectangle using the input length and width. Returns float: The area of the rectangle.
        side1, side2 = Rectangle.input_sides()
        return side1 * side2

# Define the Triangle subclass of Shape
class Triangle(Shape):

    def input_sides():

        #Get the base and height from the user input. Returns tuple: The base and height of the triangle.
        return float(side1_entry.get()), float(side2_entry.get())


    def area():
        #Calculate the area of a triangle using the input base and height.  Returns  float: The area of the triangle.
        side1, side2 = Triangle.input_sides()
        return 0.5 * side1 * side2

def calculate_area():

    #Calculate and display the area of the selected shape.
    selected_shape = shape_var.get()

    if selected_shape == "Circle":
        area_result = Circle.area()
    elif selected_shape == "Rectangle":
        area_result = Rectangle.area()
    elif selected_shape == "Triangle":
        area_result = Triangle.area()
    else:
        messagebox.showerror("Error", "Please select a shape.")
        return

    messagebox.showinfo("Area Result", f"Area: {area_result:} square units")

# Creating a root window
root = Tk()

# Setting the title for the window
root.title("Shape Area Calculator")

# Setting the dimensions of the window
root.geometry("400x300")

# Creating a Frame for the Shape tab with background color and padding
shape_tab = Frame(root, bg="#E6E6FA", pady=20)

# Label for selecting the shape with specified font and background color
label_shape = Label(shape_tab, text='Select Shape:', font=("Helvetica", 12), bg="#E6E6FA")
label_shape.pack()

# Options for the shapes presented in a drop-down menu
shapes = ["Circle", "Rectangle", "Triangle"]
shape_var = StringVar()
shape_var.set(shapes[0])
shape_option = OptionMenu(shape_tab, shape_var, *shapes)
shape_option.pack(pady=10)

# Labels and Entry widgets for inputting side values
side1_label = Label(shape_tab, text="Enter Side 1:", font=("Helvetica", 12), bg="#E6E6FA")
side1_label.pack(pady=5)
side1_entry = Entry(shape_tab, font=("Helvetica", 12))
side1_entry.pack(pady=5)

side2_label = Label(shape_tab, text="Enter Side 2:", font=("Helvetica", 12), bg="#E6E6FA")
side2_label.pack(pady=5)
side2_entry = Entry(shape_tab, font=("Helvetica", 12))
side2_entry.pack(pady=5)

# Button to trigger the area calculation with specified text, command, font, and color
calculate_button = Button(shape_tab, text='Calculate Area', command=calculate_area, font=("Helvetica", 12), bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Packing the Shape tab
shape_tab.pack(fill=BOTH, expand=YES)

# Run the main event loop
root.mainloop()

# End Marker