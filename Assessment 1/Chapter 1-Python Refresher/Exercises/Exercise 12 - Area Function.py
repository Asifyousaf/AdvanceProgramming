# Chapter 1 Exercise 12 - Area Fucntion

# Using math to do operations
import math

def calculate_square_area():
    # Function to calculate the area of a square
    side_length = float(input("Enter the side length of the square: "))
    area = side_length ** 2
    print(f"The area of the square is: {area}")

def calculate_circle_area():
    # Function to calculate the area of a circle
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area}")

def calculate_triangle_area():
    # Function to calculate the area of a triangle
    base_length = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base_length * height
    print(f"The area of the triangle is: {area}")

def main():
    # Main program to display a menu and calculate area based on user input
    while True:
        print("Menu:")
        print("1: Calculate the area of a square")
        print("2: Calculate the area of a circle")
        print("3: Calculate the area of a triangle")
        print("4: Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_square_area()
        elif choice == '2':
            calculate_circle_area()
        elif choice == '3':
            calculate_triangle_area()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Call the main function directly
main()
