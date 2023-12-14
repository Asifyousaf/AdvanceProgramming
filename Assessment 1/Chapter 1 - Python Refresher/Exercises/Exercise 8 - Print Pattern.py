# Chapter 1 Exercise 8 - Print Pattern

# Loop through a range to control the number of rows in the pattern
for i in range(1, 5):
    # Loop through a range to control the number of columns in each row
    for j in range(1, i + 1):
        print(j, end=" ")  # Print the value of 'j' followed by a space, without moving to a new line
    print()  # Move to a new line after printing each row

    # End marker