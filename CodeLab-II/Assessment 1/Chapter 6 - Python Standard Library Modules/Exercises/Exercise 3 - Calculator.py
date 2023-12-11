# Importing the math module to use arithmetic operations
import math

# Function to create a simple calculator
def calculator():
    # Displaying the calculator menu
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Enter Q to quit")

    # Main loop for the calculator
    while True:
        try:
            # Getting user input for the operation choice
            choice = input("Enter your choice (1-6): ")

            # Checking if the user wants to quit
            if choice == "Q" or choice == "q":
                print("Closing program")
                break

            # Converting the choice to an integer
            choice = int(choice)

            # Validating the user's choice
            if 1 <= choice <= 6:
                # Getting user input for the numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Performing the selected operation based on the user's choice
                if choice == 1:
                    result = num1 + num2
                elif choice == 2:
                    result = num1 - num2
                elif choice == 3:
                    result = num1 * num2
                elif choice == 4:
                    result = num1 / num2
                elif choice == 5:
                    result = num1 % num2
                elif choice == 6:
                    result = max(num1, num2)

                # Displaying the result of the calculation with quit option
                print("Result:", result)
                print("Enter Q to quit")
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            # Handling invalid input errors
            print("Invalid input. Please enter a valid number.")

# Calling the calculator function to run the program
calculator()

# End marker