# Chapter 2 Bonus Exercise A - Temperature Converter

# using the tkinter library
from tkinter import *

# Making a Function to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit():
    user_input = celsius_entry.get()
    if user_input.isdigit():
        celsius = float(user_input)
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F", fg="white")
    else:
        result_label.config(text="Invalid input", fg="red")

# Making a Function to convert from Fahrenheit to Celsius
def fahrenheit_to_celsius():
    user_input = fahrenheit_entry.get()
    if user_input.isdigit():
        fahrenheit = float(user_input)
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit:.2f}°F = {celsius:.2f}°C", fg="white")
    else:
        result_label.config(text="Invalid input", fg="red")


# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Temperature Converter")

# Adding a white background to the main window
root.configure(bg='#22263d')

# Making a heading
head1 = Label(root, font=('Roboto', 20, 'bold'), text="Temperature Converter", bg='#22263d',fg="white")
head1.grid(row=0, column=0, columnspan=3, pady=10,padx=10)

# Text and entry feild for Celsius to Fahrenheit Conversion
celsius_label = Label(root, text="Input Celsius:", font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
celsius_label.grid(row=1, column=0, padx=10, pady=10)

celsius_entry = Entry(root, font=('Roboto', 12,'bold'), bg='#B0C4DE', fg='black')
celsius_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to convert
celsius_to_fahrenheit_button = Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit, font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
celsius_to_fahrenheit_button.grid(row=1, column=2, padx=10, pady=10)

# Text and entry feild Fahrenheit to Celsius Conversion
fahrenheit_label = Label(root, text="Input Fahrenheit:", font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
fahrenheit_label.grid(row=2, column=0, padx=10, pady=10)

fahrenheit_entry = Entry(root, font=('Roboto', 12, 'bold'), bg='#B0C4DE', fg='black')
fahrenheit_entry.grid(row=2, column=1, padx=10, pady=10)

fahrenheit_to_celsius_button = Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius,font=('Roboto', 12,'bold'), bg='#22263d', fg='white')
fahrenheit_to_celsius_button.grid(row=2, column=2, padx=10, pady=10)

# Display the result
result_label = Label(root, text="", font=("Helvetica", 15), bg='#22263d', fg="white")
result_label.grid(row=3, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()

# End marker