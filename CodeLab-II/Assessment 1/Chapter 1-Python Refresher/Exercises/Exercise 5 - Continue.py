# Counter for loop
count = 0

# using while loop
while True:
    # Ask the user if they want to continue
    user_input = input("Do you want to continue? Enter 'Y' for yes, any other key to exit: ").upper()

    # Check if the user wants to continue
    if user_input == 'Y':
        # Adding the loop count
        count += 1
    else:
        # Exiting the loop if user enters anything else 
        break

# Output the number of times the loop was executed
print(f"The loop was executed {count} times.")
