# A loop for the menu
while True:
    try:
        # Asking user to choose an operation
        operation_choice = int(input("Calculator Menu:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n"))
    except ValueError:
        # Error for non-integer input
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    if operation_choice not in [1, 2, 3, 4, 5]:
        # If the user inputs an invalid choice, ask again
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    # Getting values for calculation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation_choice == 1:
        result = num1 + num2
        operation_name = "Addition"
    elif operation_choice == 2:
        result = num1 - num2
        operation_name = "Subtraction"
    elif operation_choice == 3:
        result = num1 * num2
        operation_name = "Multiplication"
    elif operation_choice == 4:
        if num2 != 0:
            result = num1 / num2
            operation_name = "Division"
        else:
            print("Cannot divide by zero.")
            continue
    elif operation_choice == 5:
        if num2 == 0:
            result = num1 % num2
            operation_name = "Modulus"
        else:
            print("Cannot calculate modulus with zero divisor.")
            continue

    print(f"The result of {operation_name} is {result}")

    another_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
    if another_calculation.lower() == 'n':
        print("Exiting the calculator. 4Goodbye!")
        break

