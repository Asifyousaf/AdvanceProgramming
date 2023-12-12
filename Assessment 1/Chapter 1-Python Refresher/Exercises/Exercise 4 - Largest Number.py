# Chapter 1 Exercise 4 - Largest Number

# Prompt the user to enter three numbers and store them in variables
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

# Checking which number is the largest among the three using if-elif-else statements
if num1 > num2 and num1 > num3:
    print(f"The Number {num1} is the biggest")  # Print the result if num1 is the largest

elif num2 > num1 and num2 > num3:
    print(f"The Number {num2} is the biggest")  # Print the result if num2 is the largest

elif num3 > num1 and num3 > num2:
    print(f"The Number {num3} is the biggest")  # Print the result if num3 is the largest

else:
    print("Wrong input")  # Print an error message if the inputs are not valid

# End marker