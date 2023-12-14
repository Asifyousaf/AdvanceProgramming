# Chapter 5 Bonus Exercise A - Playing around in class

# Defining a class called Animal
class Animal:
    def set_data(animal, animal_type, name, colour, age, weight, noise):
        # Setting values for the members of the Animal class
        animal.type = animal_type
        animal.name = name
        animal.colour = colour
        animal.age = age
        animal.weight = weight
        animal.noise = noise

    def say_hello(animal):
        # to Return a greeting message using the animal's name
        return f"{animal.name} says hello!"

    def make_noise(animal):
        # Return the noise the animal makes along with its name
        return f"{animal.name} makes the noise: {animal.noise}"

    def animal_details(animal):
        # Return all details of the animal
        details = f"Type: {animal.type}\nName: {animal.name}\nColour: {animal.colour}\nAge: {animal.age}\nWeight: {animal.weight}\nNoise: {animal.noise}"
        return details

# function to create Animal objects and invoke class functions
def create_animal_objects():
    # Getting values from user input in the console
    animal_type = input("Enter Type: ")
    name = input("Enter Name: ")
    colour = input("Enter Colour: ")
    age = input("Enter Age: ")
    weight = input("Enter Weight: ")
    noise = input("Enter Noise: ")

    # Creating an instance of the Animal class
    animal_object = Animal()

    # Setting data for the Animal instance
    animal_object.set_data(animal_type, name, colour, age, weight, noise)

    # Print the results directly to the console
    print(animal_object.say_hello())
    print(animal_object.make_noise())
    print(animal_object.animal_details())

# Calling the function to create Animal objects
create_animal_objects()
