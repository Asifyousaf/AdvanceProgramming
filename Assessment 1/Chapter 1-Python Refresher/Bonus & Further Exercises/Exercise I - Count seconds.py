# Chapter 1 Further Exercise I - Count seconds

while True:
    # Getting user input for the number of days
    user_day_input = input("Enter the number of days: ")

    # Checking if the input is of digits 
    if user_day_input.isdigit():
        # Converting the input to an integer
        user_day = int(user_day_input)

        # Calculating the number of seconds if the input is a valid integer
        day = user_day * 24
        minutes = day * 60
        seconds = minutes * 60

        # Displaying the result
        print(f"The seconds in {user_day} days is: {seconds} seconds")

        # Exiting the loop
        break
    else:
        # Informing the user about invalid input and prompting to try again
        print("Invalid input. Please enter a valid integer for the number of days. Try again.")

# End marker