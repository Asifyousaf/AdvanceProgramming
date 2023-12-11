# using the tkinter library and messagebox
from tkinter import *
from tkinter import messagebox

# Defining a class for representing a student
class Student:
    # Method to set data for a student
    def set_data(student, name, mark1, mark2, mark3):
        student.name = name
        student.mark1 = mark1
        student.mark2 = mark2
        student.mark3 = mark3

    # Method to calculate the average grade of a student
    def calc_grade(student):
        # Calculate the average of the three marks
        return (student.mark1 + student.mark2 + student.mark3) / 3

    # Method to display student information
    def display(student):
        # Return a formatted string with student name and average grade
        return f"Student Name: {student.name}\nAverage Grade: {student.calc_grade():.2f}"

# Function to create a student object and display information
def create_student_object():
    # Getting values from entry boxes
    name = name_entry.get()
    mark1 = float(mark1_entry.get())
    mark2 = float(mark2_entry.get())
    mark3 = float(mark3_entry.get())
    
    # Creating a Student object with the provided values
    student_object = Student()
    student_object.set_data(name, mark1, mark2, mark3)
    
    # Displaying the student information using a messagebox popup
    messagebox.showinfo("Student Information", student_object.display())

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Student Class GUI")

# Setting the window size
root.geometry("400x350")

# Labels and Entry Boxes
name_label = Label(root, text="Enter Name:") # Asking Name
name_label.pack(pady=5)
name_entry = Entry(root, font=("Helvetica", 12)) 
name_entry.pack(pady=5)

mark1_label = Label(root, text="Enter Mark 1:") # Asking Mark 1
mark1_label.pack(pady=5)
mark1_entry = Entry(root, font=("Helvetica", 12))
mark1_entry.pack(pady=5)

mark2_label = Label(root, text="Enter Mark 2:") # Asking Mark 2
mark2_label.pack(pady=5)
mark2_entry = Entry(root, font=("Helvetica", 12))
mark2_entry.pack(pady=5)

mark3_label = Label(root, text="Enter Mark 3:") # Asking Mark 3
mark3_label.pack(pady=5)
mark3_entry = Entry(root, font=("Helvetica", 12))
mark3_entry.pack(pady=5)

# Button to create a student object and display information
create_student_button = Button(root, text="Create Student", command=create_student_object, bg="#4CAF50", fg="white", font=("Roboto", 12, 'bold'))
create_student_button.pack(pady=20)

# Run the main event loop
root.mainloop()

# End Marker