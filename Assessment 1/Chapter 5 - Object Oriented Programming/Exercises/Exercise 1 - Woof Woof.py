# Chapter 5 Exercise 1 - Woof Woof

# using the tkinter library and messagebox
from tkinter import *
from tkinter import messagebox


# Defining a simple Dog class
class Dog:
    name = ""
    age = 0
    breed = ""

# Function to get information about a dog
def info(dog):
    return f"{dog.name} is {dog.age} years old and is a {dog.breed}."

# Function to make a dog woof
def woof(dog):
    return f"{dog.name} says: Woof!"

# Creating two dog objects
dog1 = Dog()
dog1.name = "Buddy"
dog1.age = 3
dog1.breed = "Labrador"

dog2 = Dog()
dog2.name = "Max"
dog2.age = 5
dog2.breed = "Golden Retriever"

# Display the information of each dog in the console
print(info(dog1))
print(info(dog2))

# Finding the oldest dog and make it woof
oldest_dog = dog1 if dog1.age > dog2.age else dog2
print(woof(oldest_dog))

# Creating a simple Tkinter GUI to display the dog information
root = Tk()
root.title('Dog Information')

# Setting the dimensions of the window
root.geometry('350x150')

# Creating the main heading
head1 = Label(root, font=('Roboto', 22, 'bold'), text="Dog Information", fg='#4CAF50', bg="#f2f2f2")
head1.pack(pady=10)

# Labels to display information about each dog and the woof of the oldest dog
label1 = Label(root, text=info(dog1), font=("Arial", 10, "bold"))
label1.pack()

label2 = Label(root, text=info(dog2), font=("Arial", 10, "bold"))
label2.pack()

oldest_dog_label = Label(root, text=woof(oldest_dog), font=("Arial", 10, "bold"))
oldest_dog_label.pack()

# Run the main event loop
root.mainloop()

# End Marker