# Chapter 1 Further Exercise II - Sum of Digits in a number

# Function to calculate the sum of digits
def sum_of_digits(number):
    # Convert the number to a string to iterate through each digit
    str_number = str(number)
    
    # Initialize sum
    digit_sum = 0
    
    # Iterate through each digit and add it to the sum
    for digit in str_number:
        digit_sum += int(digit)
    
    return digit_sum

# Input from the user
user_number = int(input("Enter a number: "))

# Calculate the sum of digits using the function
result = sum_of_digits(user_number)

# Display the result
print(f"The sum of digits in {user_number} is: {result}")