# Define the number of rows for the pattern
num = 5

# Iterate through each row
for i in range(num):
    # Print spaces before the asterisks for the current row
    for j in range(0, num - i - 1):
        print(" ", end="")
    
    # Print asterisks for the current row
    for j in range(0, 2 * i + 1):
        print("*", end="")
    
    # Move to the next line after printing the row
    print()
