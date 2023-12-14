# Chapter 1 Further Exercise III - Arrows

# Number of rows
num = 5
# Outer loop for the number of rows
for i in range(0, num):
    # Inner loop for printing spaces before the asterisks
    for j in range(0, num - i - 1):
        print(end=" ")

    # Inner loop for printing asterisks
    for j in range(0, 2 * i + 1):
        print("*", end="")

    # Move to the next line after completing a row
    print()

# End marker